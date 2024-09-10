datos1 <- read.csv("Boston.csv", head=T, sep=",")
head(datos1)
str(datos1)

# y = medv <- valor medio de la vivienda
# x = age <- edad

# as factor

library(dplyr)

datos <- select(datos1, age, medv)
str(datos)
datos <- rename(Y = medv , X = age,.data = datos)
str(datos)

boxplot(Y)
boxplot(X)


# attach(datos)
# representación gráfica
# histograma de frecuencias para las variables X e Y
require(ggplot2) 

par(mfrow = c(1,2)) # dos figuras en una fila 

hist(datos$X, breaks = 10, main = "Histograma X", xlab = "Age", 
     border = "darkred") 
hist(datos$Y, breaks = 10, main = "Histograma Y", xlab = "Medv", 
     border = "blue")

# estadísticos descriptivos 
summary(datos)

# diagrama de dispersión
require(ggplot2)
ggplot(data = datos, mapping = aes(x = X, y = Y)) + geom_point(color = "firebrick", size = 2) +
  (labs(title = "Diagrama de dispersión", x="Age", y= "Medv"))+
  theme_bw() +
  theme(plot.title = element_text(hjust =0.5))

# correlación de Pearson
cor.test(x = datos$X, y = datos$Y, method = "pearson")

# Calculo del modelo de regresión lineal simple
modelo_lineal <- lm(Y ~ X, data=datos) # selección de variables y data
summary(modelo_lineal)
names(modelo_lineal)
# Cálculo del error cuadrático medio RMSE:
sqrt(mean(modelo_lineal$residuals^2))

anova(modelo_lineal)

# Intervalos de confianza para los parámetros del modelo 
confint(modelo_lineal)

# Representación gráfica del modelo
ggplot(data = datos, mapping = aes(x = X, y = Y)) + geom_point(size=3) +
  (labs(title = "Diagrama de dispersión", x="Medv", y= "Age"))+
  geom_smooth(method = "lm", se = FALSE, color = "firebrick") + theme_bw() +
  theme(plot.title = element_text(hjust = 0.2))

names(modelo_lineal)

# predecir valores para Y con valores conocidos de X
nuevos_datos <- data.frame(X= seq(min(X),max(X))) 
predict_value <- predict(modelo_lineal) 
head(predict_value)# muestra 6 valores predichos

# solo una banda 
par(mfrow = c(1, 1)) 
puntos <- seq(from = min(datos$X), 
              to = max(datos$X), length.out = 100) 

limites_intervalo <- predict(object = modelo_lineal, 
                             newdata = data.frame(X = puntos), 
                             interval = "confidence", level = 0.95) 
head(limites_intervalo, 3)


plot(datos$X, datos$Y, col = "firebrick", pch = 19,
     ylab = "medv", xlab = "age",
     main = "age ~ medv")
abline(modelo_lineal, col = 1)
lines(x = puntos, y = limites_intervalo[, 2], type = "l", col = 2, lty = 3)
lines(x = puntos, y = limites_intervalo[, 3], type = "l", col = 3, lty = 3)


# con geom plot
ggplot(data = datos, mapping = aes(x = X, y = Y)) +
  geom_point(color = "firebrick", size = 2) +
  labs(title = "Diagrama de dispersion", x = "numerode bateos") +
  geom_smooth(method = "lm", se = TRUE, color = "black") +
  theme_bw() +
  theme(plot.title = element_text(hjust = 0.5))


# dos bandas de confianza
par(mfrow = c(1, 1))
# Grafico dispersion y recta
plot(datos$X, datos$Y, col = "firebrick", pch = 19,
     ylab = "Y", xlab = "X",
     main = "")
abline(modelo_lineal, col = 1)
# Intervalos de confianza de la respuesta media:
# valores medios
ic <- predict(modelo_lineal, nuevos_datos, interval = 'confidence')
lines(nuevos_datos$X, ic[, 2], lty = 2)
lines(nuevos_datos$X, ic[, 3], lty = 2)
# Intervalos de predicción
# para cualquier valor
ic <- predict(modelo_lineal, nuevos_datos, interval = 'prediction')
lines(nuevos_datos$X, ic[, 2], lty = 2, col = 'red')
lines(nuevos_datos$X, ic[, 3], lty = 2, col = 'red')


datos$prediccion <- modelo_lineal$fitted.values # valores predichos
datos$residuos <- modelo_lineal$residuals
# residuales
head(datos)


# linealidad
ggplot(data = datos, aes(x = prediccion, y = residuos)) +
  geom_point(aes( color = residuos)) +
  scale_color_gradient2(low = "blue3", mid = "grey", high = "red") +
  geom_hline(yintercept = 0) +
  geom_segment(aes(xend = prediccion, yend = 0), alpha = 0.2) +
  labs(title = "Distribucion de los residuos", x = "prediccion modelo", y = "residuo") +
  theme_bw() +
  theme(plot.title = element_text(hjust = 0.5), legend.position = "none")


# Distribución normal de los residuos:
ggplot(data = datos, aes(x = residuos)) +
  geom_histogram(aes(y = ..density..)) +
  labs(title = "Histograma de los residuos") +
  theme_bw() +
  theme(plot.title = element_text(hjust = 0.5))


# grafico de cuantiles
qqnorm(modelo_lineal$residuals)
qqline(modelo_lineal$residuals)


# test de normalidad
shapiro.test(modelo_lineal$residuals)


# Kolmogorov test
ks.test(modelo_lineal$residuals, "pnorm",
        mean = mean(modelo_lineal$residuals),
        sd = sd(modelo_lineal$residuals))

