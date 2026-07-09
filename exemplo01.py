# import pandas as pd
import numpy as np
import pandas as pd

ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Obtendo os dados

try:
    print('Obtendo os dados...')
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # delimitando por cisp, roubo_veiculo e recuperacao_veiculos
    df_veiculos = df_ocorrencias[['cisp', 'roubo_veiculo', 'recuperacao_veiculos']]

    # agrupando por cisp e somando os valores de roubo_veiculo e recuperacao_veiculos
    df_veiculos = df_veiculos.groupby('cisp', as_index=False)[['roubo_veiculo', 'recuperacao_veiculos']].sum()
    print(df_veiculos)
    print('Dados obtidos com sucesso!') 

except Exception as e:
    print(f'Erro ao obter os dados; {e}')


# Calculando a correlação entre roubo_veiculo e recuperacao_veiculos
try:
    correlacao = np.corrcoef(df_veiculos['roubo_veiculo'], df_veiculos['recuperacao_veiculos'])
    print(correlacao)


except Exception as e:
    print(f'Erro ao calcular a correlação: {e}')   
