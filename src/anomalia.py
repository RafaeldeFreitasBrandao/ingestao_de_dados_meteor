from reader import carregar, validar
import pandas as pd

df = carregar('data/curitiba.csv')

df['mes']=df['data'].dt.month
df['dia_mes']=df['data'].dt.day

df_filtrado=df[~((df['mes'] == 2) & (df['dia_mes'] == 29))].copy()

print(type(df_filtrado))

temp_media_dia = df_filtrado.groupby(['mes','dia_mes'])['temperatura'].mean()



