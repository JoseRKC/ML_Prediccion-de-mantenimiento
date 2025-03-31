# Importar librerias para manipulacion de datos
import pandas as pd
import numpy as np

# Importar librerias para analisis de datos
from scipy.stats import pearsonr
from scipy.stats import f_oneway, kruskal, ttest_ind, mannwhitneyu

# Importar librerias para visualizacion
import seaborn as sns
import matplotlib.pyplot as plt


##Función para eliminar columnas innecesarias
def Eliminar_variables(df, columnas_eliminar):
    """
    Elimina las variables que no son necesarias para el modelo
    """
    df.drop(columns=['Columnas_eliminar'], inplace=True)
    return df

##Función para crear nuevas variables
def Crear_variable_potencia(df):
    """
    Crea nuevas variables a partir de las variables existentes
    """
    # Calculo de potencia
    # La potencia se calcula como el producto del par motor y la velocidad angular para ello se ha de convertir de rpm a rad/s
    df['Power_W'] = df.Torque * (df.Rotational_speed * (2 * np.pi / 60))
    return df

# Crear una nueva variable que sea la diferencia entre la temperatura del aire y la temperatura del proceso
def Crear_variable_dif_temperadra(df):    
    df['Temp_Diff'] =  df.Process_temperature-df.Air_temperature
    
    return df

#Tratamos la variable categorica Type para convertirla en variables dummy
# Se eliminan las variables innecesarias
def tratar_type(df):
    df =  pd.get_dummies(df, columns=['Type'], dtype=int)
    return df