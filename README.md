# Evaluación Final Módulo 3

Antes de empezar, hay que crear un nuevo repositorio desde GitHub Classroom usando este enlace. Una vez creado, hay que clonar en nuestro ordenador y
en la carpeta creada empezaremos a trabajar en el ejercicio.
Esta evaluación consta de una serie de preguntas que evalúan tu comprensión y habilidades en relación con el temario del módulo 3.
Puedes usar recursos externos, incluyendo internet y materiales de referencia o tus propias notas.
Completa los ejercicios en un repositorio con la estructura correcta para todos los archivos de la evaluación.
EDA: Entender el proceso de EDA. *
Métodos Pandas. *
Limpieza. Uso de "apply" para tranformar datos. *
Visualización: Creación e interpretación de gráficas. *
Proceso de ETL y Pipeline
A/B Testing

##  Ejercicios incluidos

### ➡️ Fase 1: Exploración y Limpieza

- **Descripción**

### ➡️ Fase 2: Visualización

- **Descripción**:

### ➡️ Fase 3: Evaluación de Diferencias en Reservas de Vuelos por Nivel Educativo

- **Descripción**:

## 💻 Tecnologías empleadas:
[![Python Version](https://img.shields.io/badge/Python-3.9.7-yellow?style=flat&logo=python&logoColor=white&color=3776AB)](https://www.python.org/downloads/release/python-397/) 
[![Jupyter Notebooks](https://img.shields.io/badge/Jupyter-Notebooks-orange?style=flat&logo=jupyter&logoColor=white&color=F37626)](https://jupyter.org/)


### 📚 Bibliotecas específicas:
-# importamos las librerías que necesitamos
import pandas as pd
import numpy as np

# Visualización
# ------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

# Evaluar linealidad de las relaciones entre las variables
# y la distribución de las variables
# ------------------------------------------------------------------------------
import scipy.stats as stats

from scipy.stats import shapiro, levene, mannwhitneyu
from scipy.stats import ttest_ind, norm, chi2_contingency

# Configuración
# -----------------------------------------------------------------------
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

# Gestión de los warnings
# -----------------------------------------------------------------------
import warnings
warnings.filterwarnings("ignore")

## 🛠️ Instalación

- Clona el repositorio: "https://github.com/Adalab/bda-modulo-3-evaluacion-final-mirnaospinobarrios.git"
- Accede al directorio del repositorio: 'Adalab/bda-modulo-3-evaluacion-final-mirnaospinobarrios'

## 🙌 Contribuciones

Actualmente no se aceptan contribuciones externas al equipo de desarrollo.

## ⚖️ Licencia

Este proyecto está bajo la [Licencia MIT](https://es.wikipedia.org/wiki/Licencia_MIT).

## 👾 Equipo de desarrollo


- **[mirnaospinobarrios](https://github.com/mirnaospinobarrios)**


## ⚙️ Estado del proyecto

Actualmente en desarrollo. 