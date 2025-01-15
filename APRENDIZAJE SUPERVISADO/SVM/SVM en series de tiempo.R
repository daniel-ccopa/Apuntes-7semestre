data(AirPassengers) 
monthly_data <- unclass(AirPassengers)
monthly_data

months <- 1:144

DF <- data.frame(months,monthly_data)
colnames(DF)<-c("x","y")
DF

library(e1071)

# train an svm model, consider further tuning parameters for lower MSE
svmodel <- svm(y ~ x,data=DF, type="eps-regression",kernel="radial",cost=10000, gamma=10)
#specify timesteps for forecast, eg for all series + 24 months ahead
nd <- 1:168
nd

#compute forecast for all the 156 months 
prognoza <- predict(svmodel, newdata=data.frame(x=nd))
prognoza

#plot the results
ylim <- c(min(DF$y), max(DF$y))
xlim <- c(min(nd),max(nd))
plot(DF$y, col="blue", ylim=ylim, xlim=xlim, type="l")
par(new=TRUE)
plot(prognoza, col="red", ylim=ylim, xlim=xlim, type="l")
