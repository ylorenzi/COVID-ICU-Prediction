# Prevendo necessidade de leitos de UTI com Machine Learnig 🏥
> Projeto Final do Bootcamp de Data Science da Alura

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

## 4 - Metodologia

São utilizados dois diferentes modelos de mahcine learning da biblioteca Scikit-learn. Para os dois modelos é feito um grid search, que nada mais é que uma busca exaustiva ao longo de várias combinações de hiperparâmetros, de forma a encontrar a melhor delas. A métrica utilizada para definir o melhor modelo é o AUC. Para cada combinação também é feito o cross validation, com o método Repeated Stratified K Fold. Nesse processo, o número de divisões dos dados escolhido foi de 5, o que ocorria 5 vezes, de forma a mitigar os efeitos da aleatoriedade.

## 5 - Resultados

Os melhores resultados encontrados pelo grid search para cada um dos modelos foram:

- Logistic Regression com AUC médio de 0,768
- Random Forest com AUC médio de 0,793

Vale destacar também que o Random Forest apresentou menos variâncias nos resutlados

## 6- Conclusão

Implementamos modelos de machine learning para tentar prever a necessidade de um leito de UTI a partir de características individuais de pacientes. Dos dois modelos testados, o Random Forest se mostrou levemente melhor que o Logistic Regression. Ainda assim, como se trata de um problema envolvendo vidas humanas os resultados não são bons o suficiente para implementação nos hospitais. Esse projeto possui algumas limitações:

* quantidade de dados é pequena;
* grid search não foi tão amplo por conta de limitações computacionais;
* apenas dois modelos diferentes foram testados.

Trabalhos futuros podem lidar com essas limitações para obter resultados superiores, e talvez, se tornaram viáveis para implementação em hospitais.
