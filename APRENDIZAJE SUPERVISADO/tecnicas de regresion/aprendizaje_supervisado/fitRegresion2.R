##################################################3
#.........................................#
#....Regresión con Árboles de Decisión...#
#.........................................#

library(rpart)
set.seed(1234)
regresor_decisiontree <- rpart(Y ~ X, data = train,
                               control = rpart.control(minsplit = 2))

y_dt_predict <- predict(regresor_decisiontree, train)
ggplot() + geom_point(data = train, aes(x = X, y = Y), size = 0.9) +
  geom_line(aes(x = train$X, y = y_dt_predict), color = "red") +
  xlab("Índice de accesibilidad a carreteras (X)") +
  ylab("Valor medio de viviendas (Y)") +
  ggtitle("Curva de Ajuste sobre Conjunto de Entrenamiento (train)")

cor(train$Y, y_dt_predict)

x_grid <- seq(min(train$X), max(train$X), 0.01)
ggplot() + geom_point(data = train, aes(x = X, y = Y), size = 0.9) +
  geom_line(aes(x = x_grid, y = predict(regresor_decisiontree, data.frame(X = x_grid))),
            color = "red") +
  xlab("Índice de accesibilidad a carreteras (X)") +
  ylab("Valor medio de viviendas (Y)") +
  ggtitle("Curva de Ajuste sobre Conjunto de Entrenamiento (train)")


y_dt_test_predict <- predict(regresor_decisiontree, Test)

x_grid <- seq(min(Test$X), max(Test$X), 0.01)

ggplot() + geom_point(data = Test, aes(x = X, y = Y), size = 0.9) +
  geom_line(aes(x = x_grid, y = predict(regresor_decisiontree, data.frame(X = x_grid))),
            color = "red") +
  xlab("Índice de accesibilidad a carreteras (X)") +
  ylab("Valor medio de viviendas (Y)") +
  ggtitle("Curva de Ajuste sobre Conjunto de Validación (Test)")

cor(Test$Y, y_dt_test_predict)

predict_value_dt <- predict(regresor_decisiontree, data.frame(X = 10))
predict_value_dt


# Cálculo del error
error <- predict_value_dt - Test$Y
error

# Cálculo del error cuadrático medio RMSE:
sqrt(mean(error^2))

# Estructura del árbol
library(tree)
set.seed(123)
arbol_regresion <- tree::tree(
  formula = Y ~ X,
  data = train,
  split = "deviance",
  mincut = 5,
  minsize = 10
)
summary(arbol_regresion)

plot(x = arbol_regresion, type = "proportional")
text(x = arbol_regresion, splits = TRUE, pretty = 0, cex = 0.80, col = "firebrick")


#..........................
#...Regresión con Bosques Aleatorios

library(randomForest)
set.seed(1234)
regresor_randomForest <- randomForest(Y ~ X, data = train, ntree = 10)

y_rf_predict <- predict(regresor_randomForest, train)
cor(train$Y, y_rf_predict)

x_grid <- seq(min(train$X), max(train$X), 0.01)
ggplot() + geom_point(data = train, aes(x = X, y = Y), size = 0.9) +
  geom_line(aes(x = x_grid, y = predict(regresor_randomForest, data.frame(X = x_grid))),
            color = "red") +
  xlab("Índice de accesibilidad a carreteras (X)") +
  ylab("Valor medio de viviendas (Y)") +
  ggtitle("Curva de Ajuste sobre Conjunto de Entrenamiento (train)")


y_rf_test_predict <- predict(regresor_randomForest, Test)

cor(Test$Y, y_rf_test_predict)

x_grid <- seq(min(Test$X), max(Test$X), 0.01)
ggplot() + geom_point(data = Test, aes(x = X, y = Y), size = 0.9) +
  geom_line(aes(x = x_grid, y = predict(regresor_randomForest, data.frame(X = x_grid))),
            color = "red") +
  xlab("Índice de accesibilidad a carreteras (X)") +
  ylab("Valor medio de viviendas (Y)") +
  ggtitle("Curva de Ajuste sobre Conjunto de Validación (Test)")

predict_value_rf <- predict(regresor_randomForest, data.frame(X = 10))
predict_value_rf

# Cálculo del error
error <- predict_value_rf - Test$Y


error

# Cálculo del error cuadrático medio RMSE:
sqrt(mean(error^2))


#####################################################
# Validación simple - lm
### LOOCV
# Se genera el modelo lineal con GLM, dado que se va a emplear LOOCV no es necesario
# dividir las observaciones en dos grupos
modelo <- glm(Y ~ X, data = datos1)
summary(modelo)

MSE <- mean(regresor$residuals^2)
MSE

RMSE <- sqrt(MSE)

RMSE

# Se emplea la función cv.glm() para la validación LOOCV
library(boot)
cv_error <- cv.glm(data = datos1, glmfit = modelo)
MSE1 <- cv_error$delta
MSE1

RMSE1 <- sqrt(MSE1)
RMSE1

# K-fold Cross-Validation
# Se genera el modelo lineal con GLM
modelo <- glm(Y ~ X, data = datos1)
# Se emplea la función cv.glm() para la validación, empleando en este caso k = 10
set.seed(1)
cv_error <- cv.glm(data = datos1, glmfit = modelo, K = 10)
MSE2 <- cv_error$delta
MSE2

RMSE2 <- sqrt(MSE2)
RMSE2

### Bootstrapping
dim(datos1)



# Se define la función que devuelve el estadístico de interés, los coeficientes
# de regresión
fun_coeficientes <- function(data, index){
  return(coef(lm(Y ~ X, data = data, subset = index)))
}
# Se implementa un bucle que genere los modelos de forma iterativa y almacene
# los coeficientes.
beta_0 <- rep(NA, 9999)
beta_1 <- rep(NA, 9999)
for(i in 1:9999) {
  coeficientes <- fun_coeficientes(data = datos1,
                                   index = sample(1:506, 506, replace = TRUE))
  beta_0[i] <- coeficientes[1]
  beta_1[i] <- coeficientes[2]
}
coeficientes

# Se muestra la distribución de los coeficientes
p5 <- ggplot(data = data.frame(beta_0 = beta_0), aes(beta_0)) +
  geom_histogram(colour = "firebrick3") +
  theme_bw()
p6 <- ggplot(data = data.frame(beta_1 = beta_1), aes(beta_1)) +
  geom_histogram(colour = "firebrick3") +
  theme_bw()
library(gridExtra)
grid.arrange(p5, p6, ncol = 2, top = "Bootstrap distribution de los coeficientes")

# Para comparar con lm
summary(lm(Y ~ X, data = datos1))$coef

# O utilizando la función boot
boot(data = datos1, statistic = fun_coeficientes, R = 9999)

