#%%
import pandas as pd
pd.set_option('display.max_columns', None)
#%%
df = pd.read_csv("files/df_clean.csv", index_col = 0)
#%%
from src import soporte as sp
#%%
# Realiza un análisis exploratorio básico de un DataFrame
eda = sp.eda(dataframe)
print(eda)
#%%
# Convierte los valores de una columna a minúsculas y reemplaza los espacios con '_'.
clean = sp.clean_column(column)
#%%
#%%
# Esta función convierte las columnas especificadas del DataFrame df en tipo de datos float.
convert = sp.convert_data_type(df, columns)
#%% Realiza un análisis exploratorio básico de un DataFrame, ademas de una columna de control
exp =sp.exploracion_dataframe(dataframe, columna_control)
print(exp)
