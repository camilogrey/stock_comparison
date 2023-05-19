import seaborn as sns
import pandas as pd
pd.set_option('display.max_columns', None)
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
from scipy.stats import zscore

# Leer el archivo
pref = pd.read_excel("Route stock 1", sheet_name="ACCION_Preferencial") 
ordi = pd.read_excel("Route stock 2", sheet_name="ACCION_Ordinaria") 

# Data wrangling

print(pref.head())

pref = pref[["Nemotécnico", "Variación porcentual", "Fecha"]]
ordi = ordi[["Nemotécnico", "Variación porcentual", "Fecha"]]

# Obtener colores únicos basados en las variaciones porcentuales de las acciones
colors = np.where(pref['Variación porcentual'] >= 0, 'green', 'red')

# Crear el gráfico de dispersión con dos colores
plt.scatter(ordi['Variación porcentual'], pref['Variación porcentual'], c=colors)
plt.xlabel('Variación Acción Ordinaria')
plt.ylabel('Variación Acción Preferencial')
plt.title('Scatter Plot de Variación de Acciones')
plt.show()

# Combinar los dataframes en uno solo
pref_ordi = pd.merge(pref, ordi, on="Fecha", suffixes=("_pref", "_ordi"))


# Crear el pair plot
sns.pairplot(pref_ordi.dropna(), vars=["Variación porcentual_pref", "Variación porcentual_ordi"])
plt.show()


# Calcular el coeficiente de correlación
correlation_coef = np.corrcoef(pref_ordi["Variación porcentual_pref"], pref_ordi["Variación porcentual_ordi"])[0, 1]

print("Coeficiente de correlación (coeficiente de correlación solo mide la relación lineal):", correlation_coef, """indica una correlación positiva moderada entre las variables
a medida que una variable aumenta, es probable que la otra variable también aumente en cierta medida, aunque como no
es fuerte, implica que los cambios en una variable no predicen perfectamente los cambios en la otra variable.
Por lo tanto, es importante analizar el contexto y considerar otras variables o factores antes de hacer interpretaciones 
más amplias sobre la relación entre las variables""")
