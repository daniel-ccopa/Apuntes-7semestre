# Llamar a otro archivo R
source("regresion_linealSimple.R")

# X numero_bateos
# Y runs 


library(ggplot2)
library(lattice)
library(caret)
set.seed(100)
# Para reproducir los mismos resultados
# dividiendo la data en train y test
grupos <- createDataPartition(y = datos$Y,p = 0.8,list = FALSE)
train <- datos[grupos,]
Test <- datos[-grupos,]


str(train)
str(Test)


library(ggplot2)
ggplot() + geom_point(data = train, aes(X, Y)) +
  geom_point() +
  xlab("número de bateos") +
  ylab("número de corridas") +
  ggtitle("diagrama de dispersión (data train")


# regresion lineal simple
set.seed(1234)
regresor <- lm(Y ~ X, data = train)
regresor
summary(regresor)


confint(regresor)
y_predict <- predict(regresor, train)
head(y_predict)


head(cbind(train,y_predict))


ggplot() + geom_point(data = train, aes(x = X, y = Y), size =
                        0.9) +geom_line(aes( x = train$X, y = y_predict), color = "red") +
  xlab("Var Indep. numero de corridas") +
  ylab("Var Dep. numero de bateos") +
  ggtitle("Curva de Ajuste sobre Conjunto de Entrenamiento")


y_test_predict <- predict(regresor, Test)
y_test_predict


ggplot() + geom_point(data = Test, aes(x = X, y = Y), size = 0.9) +
  geom_line(aes( x = Test$X, y = y_test_predict), color = "red") +
  xlab("Var Indep. numero de corridas") +
  ylab("Var Dep número de bateos ") +
  ggtitle("Curva de Ajuste sobre Conjunto de Validación")


# Cálculo de los errores
error = y_test_predict - Test$Y
error


# Cálculo del error cuadrático medio RMSE:
sqrt(mean(error^2))

cor(Test$Y, y_test_predict)

predict_value <- predict(regresor, data.frame(X= c(5508)))
predict_value

# prediciendo una secuencia
predict_value2 <- predict(regresor, data.frame(X=seq(5508,5510)))
predict_value2

train$X2 <- train$X^2
str(train)

regresor_poly <- lm(Y ~ X + X2, data = train)
summary(regresor_poly)
