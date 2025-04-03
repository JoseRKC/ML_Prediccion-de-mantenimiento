# ML_Prediccion-de-mantenimiento
 
Proyecto Machine Learning Prediccion de Mantenimiento.

El objetivo de este proycto es crear un modelo que prediga cuando una máquina puede fallar.

los datos obetidos son públicos y han sido obtenidos de:

https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset-ai4i-2020/data
S. Matzka, "Explainable Artificial Intelligence for Predictive Maintenance Applications," 2020 Third International Conference on Artificial Intelligence for Industries (AI4I), 2020, pp. 69-74, doi: 10.1109/AI4I49448.2020.00023.

The image of the milling process is the work of Daniel Smyth @ Pexels: https://www.pexels.com/de-de/foto/industrie-herstellung-maschine-werkzeug-10406128/

La solucion por la que optado finalmente ha sido la de hacer dos modelos.
El optado por esta opción ya que el dataset están altamente desbalanceados.
El primer modelo predice cuando una máquina va a fallar y en base a estos resultados el segundo modelo clasifica el fallo en los diferentes tipos de fallos que nos proporciona el dataset

La estructura del repositorio:
``src/data_sample``: Directorio donde se encuentran los datos empleados.
``src/img``: Directorio de imagenes.
``src/notebooks``: Notebooks usados para pruebas.
``src/results_notebook``: directorio donde se encuentra el notebook final
``src/models``: Directorio con los modelos guardados al ejecutar el código del proyecto.
``src/presentacion``: Directorio con documento de apoyo en la presentacion
``src/utils``: Directorio de herramientas utilizadas

