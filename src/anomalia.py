from reader import carregar, validar
import matplotlib.pyplot as plt
import pandas as pd


df = carregar('data/curitiba.csv')

def climatologia_function (df):

    df['mes']=df['data'].dt.month
    df['dia_mes']=df['data'].dt.day


    df_filtrado=df[~((df['mes'] == 2) & (df['dia_mes'] == 29))].copy()

    print(type(df_filtrado))

    temp_media_dia = df_filtrado.groupby(['mes','dia_mes'])['temperatura'].mean()

    tripla = pd.concat([temp_media_dia,temp_media_dia,temp_media_dia])

    suave = tripla.rolling(window=15, center=True).mean()

    #Plota um gráfico

    #suave.iloc[365:730].plot(x='DATA', y='temp', kind='bar', color='blue')
    #plt.title('Gráfico de Vendas')
    #plt.show()

    climatologia = suave.iloc[365:730].reset_index()

    climatologia.rename(columns={'temperatura':'climatologia'}, inplace=True)

    return climatologia, df_filtrado




def anomalia_function (climatologia, df_filtrado):

    df_anomalia = df_filtrado.merge(climatologia, on=['mes', 'dia_mes'], how='left')


    df_anomalia['anomalia']= df_anomalia['temperatura'] - df_anomalia['climatologia']

    print(df_anomalia[['data','temperatura','anomalia']])
    return df_anomalia


#Exibe a tabela 
#climatologia, df_filtrado = climatologia_function(df)
#anomalia_function(climatologia, df_filtrado)

#df_anomalia = anomalia_function(climatologia, df_filtrado)


#Verifica o tamanho das colunas, se for diferente algo deu errado.
#print(len(df_filtrado), len(df_anomalia))

#Verifica se existe valores nulos, se for maior que zero está errado.
#print(f"\nnulos ----------------> {df_anomalia['anomalia'].isna().sum()}")

#Verifica a média das anomalias, se não for próximo algo deu errado.
#print(f"\nmédia ---------------->{df_anomalia['anomalia'].mean()}")

#Verifica a média da anomalia por mês, se não for próximo de zero tem algo de errado.
#print(f"média-mês -------------->{df_anomalia.groupby('mes')['anomalia'].mean()}")

#Verifica os mínimos e máximos, se tiver valores absurdos algo deu errado
#print(f"\nminímo---------------->{df_anomalia['anomalia'].min()}")
#print(f"\nmáximo---------------->{df_anomalia['anomalia'].max()}")

#Exibe todos os valores da coluna "anomalia"
#print(df_anomalia['anomalia'])


