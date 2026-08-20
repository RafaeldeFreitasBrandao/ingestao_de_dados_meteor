from reader import carregar
from anomalia import climatologia_function, anomalia_function
import pandas as pd

df = carregar('data/curitiba.csv')
climatologia, df_filtrado = climatologia_function(df)
df_anomalia = anomalia_function(climatologia, df_filtrado)

def pareamento_function(dados, intervalo_N):

    df_anomalia_copia = dados.copy()

    df_anomalia_copia['anomalia_depois'] = df_anomalia_copia['anomalia'].shift(-intervalo_N)
    df_anomalia_copia['data_depois']= df_anomalia_copia['data'].shift(-intervalo_N)

    df_anomalia_copia['diferenca_data'] = df_anomalia_copia['data_depois'] - df_anomalia_copia['data']
    df_anomalia_copia['diferenca_data'] = pd.Timedelta(days=intervalo_N)

    

