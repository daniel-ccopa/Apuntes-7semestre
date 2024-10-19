# 1. Cargar los datos y bibliotecas necesarias
# Importar las bibliotecas necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, confusion_matrix

# Cargar los datos desde el archivo Excel
data = pd.read_excel('datos_naive_bayes.xlsx')

# 2. Exploración de los datos
# Distribución de la variable objetivo (V2)
plt.figure(figsize=(6,4))
sns.countplot(x='V2', data=data)
plt.title('Distribución de la variable objetivo (V2)')
plt.show()

# 3. Preprocesamiento de los datos
# Convertir la variable categórica V2 a numérica
data['V2'] = data['V2'].map({'Logro destacado': 2, 'Logro previsto': 1, 'En proceso': 0})

# Definir las variables predictoras (X) y la variable objetivo (y)
X = data[['S1', 'S2', 'S3', 'ST1']]
y = data['V2']

# Dividir los datos en conjunto de entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ver las dimensiones de los conjuntos de entrenamiento y prueba
print(f"Conjunto de entrenamiento: {X_train.shape}")
print(f"Conjunto de prueba: {X_test.shape}")


# 4. Entrenamiento del modelo Naive Bayes
# Crear el modelo Naive Bayes
model = GaussianNB()

# Entrenar el modelo
model.fit(X_train, y_train)

#predicciones
y_pred = model.predict(X_test)


# 5. Evaluación del modelo
# Matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred)

# Graficar la matriz de confusión
plt.figure(figsize=(6,4))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=['En proceso', 'Logro previsto', 'Logro destacado'], yticklabels=['En proceso', 'Logro previsto', 'Logro destacado'])
plt.title('Matriz de confusión')
plt.ylabel('Actual')
plt.xlabel('Predicho')
plt.show()

# Informe de clasificación
print(classification_report(y_test, y_pred, target_names=['En proceso', 'Logro previsto', 'Logro destacado']))


# 6. Curva ROC
from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve, auc
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import roc_auc_score

# Binarizamos las clases para la curva ROC
y_bin = label_binarize(y, classes=[0, 1, 2])  # 0: En proceso, 1: Logro previsto, 2: Logro destacado
n_classes = y_bin.shape[1]

# Separar los datos de nuevo si no los tienes a mano
X_train, X_test, y_train_bin, y_test_bin = train_test_split(X, y_bin, test_size=0.2, random_state=42)

# Entrenamos el modelo
model = OneVsRestClassifier(GaussianNB())
model.fit(X_train, y_train_bin)

# Predecir probabilidades
y_score = model.predict_proba(X_test)

# Calcular la curva ROC para cada clase
fpr = dict()
tpr = dict()
roc_auc = dict()

for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test_bin[:, i], y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Graficar la curva ROC
plt.figure()
colors = ['blue', 'green', 'red']
for i, color in zip(range(n_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=2,
             label='ROC curve (area = %0.2f) for class %d' % (roc_auc[i], i))

plt.plot([0, 1], [0, 1], 'k--', lw=2)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Curva ROC para cada clase')
plt.legend(loc="lower right")
plt.show()