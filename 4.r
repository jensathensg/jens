data(mtcars)

model <- lm(mpg ~ wt, data = mtcars)

plot(mtcars$wt, mtcars$mpg,
     pch = 21,
     bg = "black",
     col = "pink",
     cex = 1.2,
     main = "Scatter Plot",
     sub = "mtcars Data Set",
     xlab = "weight (1000 lbs)",
     ylab = "miles per gallon (mpg)",
     xlim = c(min(mtcars$wt) - 0.5, max(mtcars$wt) + 0.5),
     ylim = c(min(mtcars$mpg) - 2, max(mtcars$mpg) + 2))

grid()

abline(model, col = "pink", lwd = 3)

abline(h = mean(mtcars$mpg), col = "gray", lty = 2)
abline(v = mean(mtcars$wt), col = "gray", lty = 2)