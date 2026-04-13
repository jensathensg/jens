data(cars)

plot(cars$speed, cars$dist,
     pch = 19,
     col = "black",
     main = "Stopping Distance vs. Speed",
     xlab = "Speed (mph)",
     ylab = "Stopping Distance (ft)")

quad_model <- lm(dist ~ speed + I(speed^2), data = cars)

speed_seq <- seq(min(cars$speed), max(cars$speed), length.out = 100)
quad_pred <- predict(quad_model, newdata = data.frame(speed = speed_seq))

lines(speed_seq, quad_pred, col = "lightblue", lwd = 3)

lin_model <- lm(dist ~ speed, data = cars)

abline(lin_model, col = "pink", lwd = 2)