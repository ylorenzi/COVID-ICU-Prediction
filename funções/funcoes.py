import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RepeatedStratifiedKFold

# Funções para limpeza e preparação dos dados

def preenche_tabela(dados):
    """Preenche as features contínuas da base 
    
    Preenche os dados contínuos faltantes da base repetindo o mesmo valor de 
    uma janela seguinte ou anterior.

    Parameters
    ----------
    dados : dataframe

    Returns
    -------
    dados_finais : dataframe

    """
    features_continuas_colunas = dados.iloc[:, 13:-2].columns
    features_continuas = dados.groupby("PATIENT_VISIT_IDENTIFIER", as_index=False)[features_continuas_colunas].fillna(method='bfill').fillna(method='ffill')
    features_categoricas = dados.iloc[:, :13]
    saida = dados.iloc[:, -2:]
    dados_finais = pd.concat([features_categoricas, features_continuas, saida], ignore_index=True,axis=1)
    dados_finais.columns = dados.columns
    return dados_finais

def prepare_window(rows):
    """Retorna um dataframe apenas com a primeira janela
    
    Transforma ICU = 1 na primeira janela de todos pacientes que em alguma
    janela tiveram ICU = 1. Retorna um dataframe apenas com as informações
    da primeira janela.

    Parameters
    ----------
    rows : linhas dataframe

    Returns
    -------
    dataframe

    """
    if(np.any(rows["ICU"])):
        rows.loc[rows["WINDOW"]=="0-2", "ICU"] = 1
    return rows.loc[rows["WINDOW"] == "0-2"]

def remove_corr_var(dados, valor_corte):
    """Remove colunas altamente correlacionadas
    
    Identifica pares de variáveis com valor absoluto correlação acima de um 
    valor de corte e remove umas delas.
    
    Parameters
    ----------
    dados : dataframe
    valor_corte : valor máximo de correlação desejado

    Returns
    -------
    dataframe

    """
      
    matrix_corr = dados.iloc[:,4:-2].corr().abs()
    matrix_upper = matrix_corr.where(np.triu(np.ones(matrix_corr.shape).astype(bool), k=1))
    excluir = [coluna for coluna in matrix_upper.columns if any(matrix_upper[coluna] > valor_corte)]

    return dados.drop(excluir, axis=1)

# Funções dos modelos de machine learning

def busca_hiperparametros(modelo, x, y, n_splits, n_repeats, param_grid):
    """Realiza gridsearch para obter os melhores hiperparâmetros
    
    Recebe um modelo de machine learning e aplica o GridSearchCV para buscar
    os melhores hiperparâmetros. O cross validation utilizado é 
    RepeatedStratifiedKFold
    
    Parameters
    ----------
    modelo : modelo do scikit-learn
    x : matrix de parâmetros
    y : variável de objetivo
    n_splits : número de divisões do cross validation
    n_repeats : número de repetições do cross valition
    param_grid : grid de parâmetros a serem explorados no grid search

    Returns
    -------
    auc_medio : média do parâmetro AUC do melhor modelo
    auc_medio_treino : média no treino do parâmetro AUC do melhor modelo

    """
    
    cv = RepeatedStratifiedKFold(n_splits = n_splits, n_repeats = n_repeats)
    
    busca = GridSearchCV(modelo, param_grid=param_grid,
                         cv = cv, scoring='roc_auc',
                         return_train_score=True, verbose = False)
    
    busca.fit(x, y)
    
    resultados = pd.DataFrame(busca.cv_results_).iloc[busca.best_index_]
    
    auc_medio = resultados['mean_test_score']
    auc_medio_treino = resultados['mean_train_score']

    auc_std = resultados['std_test_score']
    
    print(f'AUC medio treino:  {auc_medio_treino}')
    print(f'AUC medio teste:  {auc_medio}')
    print(f'Intervalo confiança 95% do AUC medio teste:  {auc_medio -2 * auc_std } - {auc_medio + 2 * auc_std }')
    return auc_medio, auc_medio_treino