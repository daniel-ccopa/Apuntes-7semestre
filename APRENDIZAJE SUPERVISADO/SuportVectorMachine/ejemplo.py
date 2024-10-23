import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Gráficos
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
from mlxtend.plotting import plot_decision_regions

# Preprocesado y modelado
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Configuración matplotlib
plt.rcParams['image.cmap'] = "bwr"
#plt.rcParams['figure.dpi'] = "100"
plt.rcParams['savefig.bbox'] = "tight"
style.use('ggplot') or plt.style.use('ggplot')

# Configuración warnings
import warnings
warnings.filterwarnings('ignore')

datos = pd.read_excel("boston.xlsx")
datos.head(3)

datos.shape

# eliminando las variables Unnmed y chas
#del datos['Unnamed: 0']
del datos['chas']
#datos = datos.drop(["Unnamed: 0","chas"])

# resumen de las variables
datos.describe()

# Gráfico de Histograma
%matplotlib inline
# Univariate Histograms
import matplotlib.pyplot as ptl
fig=ptl.figure(figsize=(15,10)) # tamaño de figura
ax=fig.gca()#agranda la figura
datos.hist(ax=ax)
ptl.show()

# Gráfico de dispersión
fig,ax = plt.subplots(3,4,figsize=(15,8))
ax = ax.ravel()
for i in range(12):
    ax[i].scatter(datos[datos.columns[i]],datos['medv'],edgecolor='k',color='red',alpha=0.50)
    ax[i].set_title(f"{datos.columns[i]} vs. y",fontsize=10)
    ax[i].grid(True)
plt.show()

# definimos la variable dependiente
X = datos.drop(columns = 'medv')
Y = datos['medv']

# separamos la data en train y test
X_train, X_test, y_train, y_test = train_test_split(
                                        X,
                                        Y.values.reshape(-1,1),
                                        train_size   = 0.8,
                                        random_state = 1234,
                                        shuffle      = True
                                    )


# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


from sklearn.svm import SVR


from sklearn.metrics import mean_squared_error, make_scorer
# probando valores de C
print ('C',' RMSE',' MSE')
for i in range (1, 50, 2):
  svmlinear = SVR(kernel = 'linear', C=i)
  svmlinear.fit(X_train, y_train)
  svmlinearpred = svmlinear.predict(X = X_test)
  rmse = mean_squared_error(
      y_true  = y_test,
      y_pred  = svmlinearpred,
      squared = False
      )
  mse = rmse*rmse
  print(i, f"  {rmse:.4f}", f"  {mse:.4f}" )


# Modelo
svmlinear = SVR(kernel = 'linear', C=7)
svmlinear.fit(X_train_scaled, y_train)
#SVR(C=7, kernel='linear')


# Prediccion
y_pred = svmlinear.predict(X = X_test)
y_pred


# Error de raíz cuadrada media (RMSE)
rmse = mean_squared_error(
        y_true  = y_test,
        y_pred  = y_pred,
squared = False
)
print(f"El error (rmse) de test es: {rmse}")


# Error cuadrático medio (MSE)
mse = rmse*rmse
print(f"El error (mse) de test es: {mse}")


# Calcular los límites para la línea x = y
min_val = min(min(y_test), min(y_pred))
max_val = max(max(y_test), max(y_pred))


plt.scatter(y_test, y_pred)
#plt.plot([0, max(y_test)], [0, max(y_test)], color='red', linestyle='--')  # Aggiungi la linea x = y
plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--')  # Aggiungi la linea x = y
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted Prices")
plt.show()


from sklearn.metrics import mean_squared_error, make_scorer

# Inicializar el valor mínimo de RMSE
min_rmse = float('inf')
min_rmse_C = None

# Probando valores de C
print('C', 'RMSE', 'MSE')
for i in np.arange(0.001, 0.1, 0.002):
    svmpoly = SVR(kernel='poly', C=i, gamma="auto", degree=2)
    svmpoly.fit(X_train, y_train)
    svmpolypred = svmpoly.predict(X_test)
    
    rmse = mean_squared_error(y_true=y_test, y_pred=svmpolypred, squared=False)
    mse = rmse * rmse
    
    print(f"{i:.3f}  {rmse:.4f}  {mse:.4f}")
    
    # Actualizar el valor mínimo de RMSE y el valor de C correspondiente
    if rmse < min_rmse:
        min_rmse = rmse
        min_rmse_C = i

# Imprimir el mínimo RMSE y el valor de C correspondiente
print(f"El mínimo RMSE es: {min_rmse:.4f} con C = {min_rmse_C:.3f}")


# Modelo
svmpoly = SVR(kernel="poly", C=0.099, gamma=0.1, degree=2)
svmpoly.fit(X_train, y_train)


# Predicción
svmpolypred = svmpoly.predict(X_test)

# Crear un DataFrame si no existe
if 'datapredict' not in locals():
    datapredict = pd.DataFrame(X_test, columns=[f'Feature_{i}' for i in range(X_test.shape[1])])

# Asignar las predicciones al DataFrame
datapredict["svmpolypred"] = svmpolypred
datapredict



# Error de raíz cuadrada media (RMSE)
rmse = mean_squared_error(
        y_true  = y_test,
        y_pred  = svmpolypred,
        squared = False
)
print(f"El error (rmse) de test es: {rmse}")


# Error cuadrático medio (MSE)
mse = rmse*rmse
print(f"El error (mse) de test es: {mse}")


#probando valores de C
print ('C','RMSE','MSE')
for i in range (2, 15,1):
  svmrbf = SVR(kernel = 'rbf',C=i, gamma=1, epsilon=1)
  svmrbf.fit(X_train, y_train)
  svmrbfpred = svmrbf.predict(X = X_test)rmse = mean_squared_error(
      y_true  = y_test,
      y_pred  = svmrbfpred,
      squared = False
      )
  mse = rmse*rmse
  print(f"{i:.4f}", f"  {rmse:.4f}", f"  {mse:.4f}" )

#probando valores de Gamma

print ('Gamma','    RMSE','    MSE')

for i in np.arange (0.0001, 0.01, 0.0002):
  svmrbf = SVR(kernel = 'rbf',C=10, gamma=i, epsilon=1)
  svmrbf.fit(X_train, y_train)

  svmrbfpred = svmrbf.predict(X = X_test)
  rmse = mean_squared_error(
          y_true  = y_test,
          y_pred  = svmrbfpred,
          squared = False
        )
  mse = rmse*rmse
  print(f"{i:.4f}", f"  {rmse:.4f}", f"  {mse:.4f}" )


#probando valores de Epsilon

print ('Epsilon','    RMSE','    MSE')

for i in np.arange (0.00001, 0.65, 0.01):
  svmrbf = SVR(kernel = 'rbf',C=10, gamma=0.0019, epsilon=i)
  svmrbf.fit(X_train, y_train)

  svmrbfpred = svmrbf.predict(X = X_test)
  rmse = mean_squared_error(
          y_true  = y_test,
          y_pred  = svmrbfpred,
          squared = False
        )
  mse = rmse*rmse
  print(f"{i:.4f}", f"  {rmse:.4f}", f"  {mse:.4f}" )



#Modelo
svmrbf = SVR(kernel = 'rbf',C=10, gamma=0.0019, epsilon=0.4)
svmrbf.fit(X_train, y_train)

# Make predictions
y_pred = svr.predict(X_test) # ojo ver escalado



# Make predictions
y_pred = svr.predict(X_test) # ojo ver escalado


# Error de raíz cuadrada media (RMSE)
rmse = mean_squared_error(
        y_true  = y_test,
        y_pred  = svmrbfpred,
        squared = False
       )
print(f"El error (rmse) de test es: {rmse}")


# Error cuadrático medio (MSE)
mse = rmse*rmse
print(f"El error (mse) de test es: {mse}")


#probando valores de C

print ('C','    RMSE','    MSE')

for i in range (1, 15,1):
  svmsigmoid = SVR(kernel = 'sigmoid',C=i, gamma=1)
  svmsigmoid.fit(X_train, y_train)

  svmsigmoidpred = svmsigmoid.predict(X = X_test)
  rmse = mean_squared_error(
          y_true  = y_test,
          y_pred  = svmsigmoidpred,
          squared = False
        )
  mse = rmse*rmse
  print(f"{i:.0f}", f"  {rmse:.4f}", f"  {mse:.4f}" )



# Modelo
svmsigmoid = SVR(kernel = 'sigmoid',C=5, gamma=1)
svmsigmoid.fit(X_train, y_train)
SVR(C=5, gamma=1, kernel='sigmoid')


# Predicción
svmsigmoidpred = svmsigmoid.predict(X = X_test)
datapredict["svmsigmoidpred"]=svmsigmoidpred
datapredict


# Error de raíz cuadrada media (RMSE)
rmse = mean_squared_error(
        y_true  = y_test,
        y_pred  = svmsigmoidpred,
        squared = False
       )
print(f"El error (rmse) de test es: {rmse}")

# Error cuadrático medio (MSE)
mse = rmse*rmse
print(f"El error (mse) de test es: {mse}")


C=1e3
svr_lin = SVR(kernel="linear", C=C)
svr_rbf = SVR(kernel="rbf", C=C, gamma=0.1)
svr_pol = SVR(kernel="poly", C=C, degree=3)


y_lin = svr_lin.fit(X_train,Y_train).predict(X)
y_rbf = svr_rbf.fit(X_train,Y_train).predict(X)
y_pol = svr_pol.fit(X_train,Y_train).predict(X)


# Test score
svr_lin.score(X_test,Y_test)


svr_rbf.score(X_test,Y_test)



# Linear Regresion
from sklearn.linear_model import LinearRegression
linear = LinearRegression()
linear.fit(X_train,Y_train)
linear.score(X_test,Y_test)


from sklearn.metrics import mean_squared_error
print("RMSE for linear SVR:",np.sqrt(mean_squared_error(Y_test,svr_lin.predict(X_test))))
#print("RMSE for RBF kernelized SVR:",np.sqrt(mean_squared_error(Y_test,svr_lin.predict(X_test))))



#5 Predicting a new result
#y_pred = svr_lin.predict(6.5)