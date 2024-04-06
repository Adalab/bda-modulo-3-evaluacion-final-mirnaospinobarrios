# Evaluación Final Módulo 3

Para comenzar con la evaluación final del Módulo 3, sigue estos pasos:

## 🛠️ Instalación
- Crea un nuevo repositorio desde GitHub Classroom utilizando el enlace proporcionado en el archivo "Evaluación final mod_3.pdf", disponible en el canal Slack Promo_g_da.
- Clona el repositorio: "https://github.com/Adalab/bda-modulo-3-evaluacion-final-mirnaospinobarrios.git"
- Accede al directorio del repositorio: 'Adalab/bda-modulo-3-evaluacion-final-mirnaospinobarrios' y comienza a trabajar en los ejercicios en la carpeta correspondiente.

## 🛠️ Ejercicios

Esta evaluación abarca una serie de preguntas que evalúan la comprensión y habilidades relacionadas con el temario del Módulo 3, centrándose en los siguientes aspectos:

- **EDA (Análisis Exploratorio de Datos):** Comprender el proceso de EDA.
- **Métodos de Pandas:** Utilizar Pandas para manipulación y análisis de datos.
- **Limpieza de Datos:** Aplicar métodos de limpieza y transformación de datos utilizando "apply".
- **Visualización:** Crear e interpretar gráficos.
- **Proceso ETL y Pipeline**
- **A/B Testing**

### Fases

#### Fase 1: Exploración y Limpieza

#### Fase 2: Visualización

#### Fase 3: Evaluación de Diferencias en Reservas de Vuelos por Nivel Educativo

## 💻 Tecnologías empleadas

- **Python Version:** [![Python Version](https://img.shields.io/badge/Python-3.9.7-yellow?style=flat&logo=python&logoColor=white&color=3776AB)](https://www.python.org/downloads/release/python-397/) 
- **Jupyter Notebooks:** [![Jupyter Notebooks](https://img.shields.io/badge/Jupyter-Notebooks-orange?style=flat&logo=jupyter&logoColor=white&color=F37626)](https://jupyter.org/)

## 📚 Bibliotecas específicas:

#### Tratamiento de datos
import pandas as pd
import numpy as np

#### Visualización
import matplotlib.pyplot as plt
import seaborn as sns

#### Evaluar linealidad de las relaciones entre las variables y la distribución de las variables
import scipy.stats as stats
from scipy.stats import shapiro, levene, mannwhitneyu
from scipy.stats import ttest_ind, norm, chi2_contingency

#### Configuración
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

##### import warnings
warnings.filterwarnings("ignore")

##### imputacion valores nulos
from sklearn.impute import KNNImputer


## 🙌 Contribuciones

Actualmente no se aceptan contribuciones externas al equipo de desarrollo.

## ⚖️ Licencia

Este proyecto está bajo la [Licencia MIT](https://es.wikipedia.org/wiki/Licencia_MIT).

## 👾 Equipo de desarrollo

- **[mirnaospinobarrios](https://github.com/mirnaospinobarrios)**

## ⚙️ Estado del proyecto

Actualmente en desarrollo. 

