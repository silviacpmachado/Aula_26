# import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

ENDERECO_DADOS = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Obtendo os dados

try:
    print('Obtendo os dados...')
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')

    # delimitando por cisp, roubo_veiculo e recuperacao_veiculos
    df_lesoes = df_ocorrencias[['cisp', 'lesao_corp_dolosa', 'lesao_corp_morte']]

    # agrupando por cisp e somando os valores de lesão corporal dolosa e lesão corporal com morte
    df_lesoes = df_lesoes.groupby('cisp', as_index=False)[['lesao_corp_dolosa', 'lesao_corp_morte']].sum()
    print(df_lesoes)
    print('Dados obtidos com sucesso!') 

except Exception as e:
    print(f'Erro ao obter os dados; {e}')


# Calculando a correlação entre lesão corporal dolosa e lesão corporal com morte
try:
    correlacao = np.corrcoef(df_lesoes['lesao_corp_dolosa'], df_lesoes['lesao_corp_morte'])
    print(f' Correlação entre Lesão Corporal Dolosa e Lesão Corporal Com Morte: {correlacao}')

    #plotando o grafico de dispersão
    plt.scatter(df_lesoes['lesao_corp_dolosa'], df_lesoes['lesao_corp_morte'])
    plt.title('Correlação entre as Lesões')
    plt.xlabel('Lesão Corporal Dolosa') 
    plt.ylabel('Lesão Corporal com Morte')
    plt.show()


except Exception as e:
    print(f'Erro ao calcular a correlação: {e}')   
