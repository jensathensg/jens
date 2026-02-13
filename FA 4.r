normal <- c(
  67,70,63,65,68,60,70,64,69,61,65,71,62,66,68,64,67,62,66,63,
  65,63,66,65,63,69,62,59,66,65,63,60,65,60,67,68,61,63,67,63,
  65,62,66,68,69,57,58,60
)

skewed_right <- c(
  69,62,59,59,66,65,63,65,60,67,68,61,69,65,63,67,70,64,63,63,
  61,63,60,63,57,35,34,30,38,26,29,46,26,57,34,34,36,40,28,38,
  66,63,64,63,53,24,33,35,34,28
)

skewed_left <- c(
  31,43,30,30,38,26,29,55,38,26,29,57,34,41,35,40,34,66,63,33,
  23,28,30,33,31,25,32,28,40,24,27,33,38,29,75,35,41,35,26,37,
  28,19,23,28,26,33,25,35
)

uniform <- c(
  40,24,29,24,27,35,33,75,38,34,85,29,40,41,35,38,19,63,28,33,
  23,28,26,31,22,10,44,92,102,55,90,73,60,73,89,85,72,76,73,97,
  70,85,93,58,92,10,92,82
)


raw_moment <- function(x, r) {
  n <- length(x); if (n == 0) return(NaN)
  mean(x^r)
}

central_moment <- function(x, r) {
  n <- length(x); if (n == 0) return(NaN)
  mu <- mean(x)
  mean((x - mu)^r)
}

moment_about_c <- function(x, r, c) {
  n <- length(x); if (n == 0) return(NaN)
  mean((x - c)^r)
}

fmt4 <- function(x) {
  if (is.nan(x)) return("nan")
  sprintf("%.4f", x)
}


datasets <- list(
  "Normal" = normal,
  "Skewed-right" = skewed_right,
  "Skewed-left" = skewed_left,
  "Uniform" = uniform
)

summary <- lapply(datasets, function(x) {
  list(
    raw = setNames(sapply(1:4, function(r) raw_moment(x, r)), 1:4),
    cen = setNames(sapply(1:4, function(r) central_moment(x, r)), 1:4)
  )
})


W_DATASET <- 14
W_NUM <- 12

print_row <- function(values, widths) {
  parts <- mapply(function(v, w) sprintf(paste0("%", w, "s"), v), values, widths, USE.NAMES = FALSE)
  cat(paste(parts, collapse = " "), "\n", sep = "")
}

print_sep <- function(total_cols, dataset_width, num_width) {
  total_width <- dataset_width + (total_cols - 1) * (num_width + 1)
  cat(paste(rep("-", total_width), collapse = ""), "\n", sep = "")
}


# MOMENTS

headers <- c("dataset","m'1", "m'2", "m'3", "m'4", "m1", "m2", "m3", "m4")
widths  <- c(W_DATASET, rep(W_NUM, length(headers) - 1))

cat("MOMENTS\n")
print_row(headers, widths)
print_sep(length(headers), W_DATASET, W_NUM)

for (name in c("Normal", "Skewed-right", "Skewed-left", "Uniform")) {
  rp <- summary[[name]]$raw
  cm <- summary[[name]]$cen
  row <- c(
    name,
    fmt4(rp["1"]), fmt4(rp["2"]), fmt4(rp["3"]), fmt4(rp["4"]),
    fmt4(cm["1"]), fmt4(cm["2"]), fmt4(cm["3"]), fmt4(cm["4"])
  )
  print_row(row, widths)
}
                  
print_sep(length(headers), W_DATASET, W_NUM)


# MOMENTS ABOUT 75 

headers2 <- c("k", "E[(X-75)^k]")
widths2  <- c(6, 18)
cat("\nMOMENTS ABOUT 75\n")
print_row(headers2, widths2)
print_sep(length(headers2), widths2[1], widths2[2])

for (k in 1:4) {
  val <- moment_about_c(normal, k, 75)
  print_row(c(as.character(k), fmt4(val)), widths2)
}
print_sep(length(headers2), widths2[1], widths2[2])


# VERIFY THE RELATION BETWEEN MOMENTS

m1p <- as.numeric(unname(summary$Normal$raw[["1"]]))
m2p <- as.numeric(unname(summary$Normal$raw[["2"]]))
m3p <- as.numeric(unname(summary$Normal$raw[["3"]]))
m4p <- as.numeric(unname(summary$Normal$raw[["4"]]))

if (any(!is.finite(c(m1p, m2p, m3p, m4p)))) {
  stop()
}


val_m2 <- m2p - m1p^2
val_m3 <- m3p - 3*m1p*m2p + 2*(m1p^3)
val_m4 <- m4p - 4*m1p*m3p + 6*(m1p^2)*m2p - 3*(m1p^4)

cat("\n VERIFY \n")

headers3 <- c("Relation", "Value")
widths3  <- c(50, 12)

print_row(headers3, widths3)
print_sep(length(headers3), widths3[1], widths3[2])

print_row(c("m2 = m2' - (m1')^2",                      sprintf("%.4f", val_m2)), widths3)
print_row(c("m3 = m3' - 3 m1' m2' + 2 (m1')^3",        sprintf("%.4f", val_m3)), widths3)
print_row(c("m4 = m4' - 4 m1' m3' + 6 (m1')^2 m2' - 3 (m1')^4", sprintf("%.4f", val_m4)), widths3)

print_sep(length(headers3), widths3[1], widths3[2])
