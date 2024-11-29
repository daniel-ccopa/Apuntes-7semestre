library(car)
library(agricolae)
library(ggplot2)
library(rstatix)
library(stats)
library(nortest)
library(outliers)
library(astsa)
library(ggpubr)

data1 = read.csv('/home/danidevtech/Downloads/RUPTURA.csv', header = TRUE)
attach(data1)
data1

# para realizar el anova

str(TIPO)
tipo = factor(TIPO)
metodo = factor(METODO)

# el modelo lineal aditivo es:


modelo = aov(YR ~ tipo + metodo+tipo:metodo, data=data1)
summary(modelo)
cv.model(modelo)

 #validacion de los supuestos de normalidad de los errores
resid2 = residuals(modelo)
resid2

sum(resid2)

#grafica de residuos

qqplot(resid2)
ggqqplot(residuals(modelo))

# normalidad de los Errores

shapiro.test(resid2)
hist(modelo$residuals)
qqnorm(modelo$residuals)
qqline(modelo$residuals, lwd=c(3), col=c("blue"))


ad.test(residuals(modelo))
lillie.test(residuals(modelo))

# homogeneidad de varianzas

bartlett.test(x=data1$YR,g=tipo:metodo,data=data1)

# comparacion de promedios para el tratamiento
trat = factor(TRAT)
modelo2 = aov(YR ~TRAT, data=data1)
summary(modelo2)
cv.model(modelo2)

# comparar con la prueba de DUNCAN

duncan = duncan.test(modelo2, "TRAT")
duncan

pairwise.t.test(x=data1$YR, g=TRAT, p.adjust.method="bonf")
