## Ingestão e Manipulação de Dados Meteorológicos

Este projeto tem o objetivo de medir a persistência do clima em múltiplos municípios do Paraná. A persistência é a tendência de um padrão climático se manter por vários dias seguidos, ou seja, quanto maior essa tendência mais previsível é o clima da região a curto prazo.
<br>
<br>
Para chegar a essas conclusões, o sistema irá ingerir 86 anos de temperatura diária a partir de uma fonte pública de dados meteorológicos, a [Open-Meteo](https://open-meteo.com/en/docs/historical-weather-api), e com base nos comportamentos típicos de cada data irá aplicar 3 métodos estatísticos que medem a persistência das temperaturas.
<br>
<br>
O resultado final deverá ser uma comparação entre municípios e estações do ano.

## Como funciona

```
CSV (Open-Meteo) → validação → climatologia → anomalia → pareamento → persistência → comparação
```

- **`reader.py`**: lê o CSV e verifica nulos, duplicatas, valores extremos e dias ausentes.
- **`anomalia.py`**: calcula a temperatura esperada para cada dia do ano (média suavizada em 15 dias) e a anomalia (temperatura do dia − esperada).
- **`persistencia.py`**: pareia cada dia com o dia N dias depois, descartando pares que atravessam falhas na série.

## Status

**Feito**
- Série de Curitiba (1940–2026) carregada e validada: 31.639 registros, sem falhas.
- Climatologia, anomalias e pareamento implementados e testados (`civ.csv` é uma cópia com dias removidos para teste).

**Em andamento**
- Métodos de persistência: autocorrelação por defasagem, probabilidade de o sinal da anomalia se manter e duração das sequências.

**A fazer**
- Incluir outros municípios do Paraná, com ingestão automática pela API.
- Comparar os resultados por estação do ano.
- Gráficos e relatório final.

## Como executar

```bash
pip install pandas matplotlib
python src/persistencia.py
```
