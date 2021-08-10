# Previsão a necessidade de leitos de UTI com Machine Learnig.

## 1- Introdução

Uma das grandes preocupações durante a pandemia da COVID-19 foi sobrecarga nos sistemas de saúde, que afetou a disponibilidade de leitos de UTI nos hospitais. Pensando nisso a equipe de Data Intelligence do hospital Sírio-Libanês disponibilizou uma base de dados de pacientes com COVID-19 no Kaggle para o desenvolvimento de modelos de machine learning capazes de prever se um dado paciente iria precisar ou não de um leito de UTI.

O presente prejeto apresenta a implementação de dois modelos distintos da biblioteca Scikit-learn, o Logistic Regression e Random Forest. Foram feitas buscas dos hiperparâmetros que otimizassem ambos os modelos e os resultados apontoram uma ligeira vantagem do Random Forest em relação ao Logistic Regression.

## 2- Dados

Os dados utilizados foram disponibilizados no Kaggle (plataforma de campeonatos de machine learning) pela equipe de Data Intelligence do hospital Sírio-Libanês. Neles podemos encontrar informações sobre:

* Informação demográfica - 3 variáveis (gênero e idade)
* Doenças pré-existentes - 9 variáveis (6 grupos, pressão alta, imunossuprimido e outros)
* Resultados do exame de sangue - 36 variáveis
* Sinais vitais - 6 variáveis

A variável resposta e se o paciente foi ou não para UTI. 

## 3- Tratamento dos Dados

Antes de começar a utilizar os modelos foi feito um tratamento da base. No notebook de limpeza é mostrado com foi feito esse tratamento. Embora existam informações de várias janelas de tempo para cada paciente, após a limpeza foram mantidas apenas informações da primeira janela. Embora isso diminua a acurácia do modelo, isso simula uma situação com mais utilidade prática para o hospital, que é determinar em um curto período de tempo se existirá uma demanda por leito de UTI, permitindo assim um melhor planejamento para uma eventual necessidade de transferência.
