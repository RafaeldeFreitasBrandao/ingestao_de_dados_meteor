import pandas as pd


path = 'data/curitiba.csv'



def carregar (path):

    linha_metadados = 3

    #Lê o arquivo, pula 3 linhas (os metadados), e formata a coluna "time" para datetime 
    df = pd.read_csv(path, skiprows=linha_metadados, parse_dates=['time'])

    #Renomeia as colunas 
    df.rename(columns={'time':'data','temperature_2m_mean (°C)':'temperatura'}, inplace=True)

    #Organiza as linhas por data 
    df = df.sort_values('data').reset_index(drop=True)

    return df


def validar (df):

    #verifica se existe valores vazios
    vazio = df["temperatura"].isna().sum()

    #verfica a temperatura mínima e máxima
    minimo = (df["temperatura"].min())
    maximo = (df["temperatura"].max())

    #verfifica se existe alguma duplicata nos dados 
    duplicata = (df["data"].duplicated().sum())

    #verifica se existe algum número falatando 
    calendario = pd.date_range(df["data"].min(), df["data"].max(), freq="D")
    ausentes = calendario.difference(df["data"])

    return {
        'temp_nulos' :vazio,
        'temp_minimo': minimo,
        'temp_maximo': maximo,
        'duplicadas' :duplicata,
        'dias_ausentes':len(ausentes),
        'registros': len(df),
    }


df = carregar(path)
resultado = validar(df)

for chave, valor in resultado.items():
    print(f"{chave}: {valor}")