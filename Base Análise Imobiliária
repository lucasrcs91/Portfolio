#Importando a base conforme instruído na plataforma
#pip install ucimlrepo

from ucimlrepo import fetch_ucirepo

# fetch dataset
apartment_for_rent_classified = fetch_ucirepo(id=555)

# data (as pandas dataframes)
x_base = apartment_for_rent_classified.data.features
y_base = apartment_for_rent_classified.data.targets

# metadata
print(apartment_for_rent_classified.metadata)

# variable information
print(apartment_for_rent_classified.variables)

#Verificando tamanho da matriz
print(np.size(x_base.price))

#importando biliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#Verificando os valores que temos em X
print(x_base[0:5])

#Definindo como Y a variável a ser analisada (preço do aluguel)
y = x_base.price
print(y)

#Análise inicial dos dados
print(f"Valor Mínimo de Preço: {min(y)}\nValor Máximo de Preço: {max(y)}\nValor médio de Preço: {round(np.mean(y),2)}\nDesvio padrão de: {round(np.std(y),2)}")

#Distribuição dos preços
plt.scatter(np.arange(len(y)),y)
plt.xlabel('Número do Registro')
plt.ylabel('Preços')
plt.title('Distruição de preços pela tabela')
plt.show()

#Histograma dos preços
plt.hist(y,bins = 30, rwidth=0.5)
plt.xlabel('Preços')
plt.ylabel('Frequência Absoluta')
plt.title('Histograma de preços')
plt.show()

#Selecionando variáveis para o modelo
print(f"Banheiros: {set(x_base.bathrooms)}")
print(f"Quartos: {set(x_base.bedrooms)}")
print(f"Pets liberados: {set(x_base.pets_allowed)}")
print(f"Metros quadrados: {set(x_base.square_feet)}")

#Trabalhando variáveis que serão utilizadas no modelo

#Função para converter valores em numéricos, substituindo respostas incorretas por NaN
def to_numeric(n):
    try:
        return float(n)
    except:
        return np.nan

n_banheiros = x_base.bathrooms.apply(to_numeric)
n_quartos = x_base.bedrooms.apply(to_numeric)
n_metros = x_base.square_feet.apply(to_numeric)

#Transformando a pets em uma variável dummy
pets = x_base.pets_allowed.apply(lambda x: 1 if x in ['Dogs','Cats,Dogs','Cats'] else 0)

print(f"Banheiros: {set(n_banheiros)}")
print(f"Quartos: {set(n_quartos)}")
print(f"Pets liberados: {set(pets)}")
print(f"Metros quadrados: {set(n_metros)}")

#montando a base do modelo
modelo_geral = {
    'banheiros': n_banheiros,
    'quartos': n_quartos,
    'metros': n_metros,
    'pets': pets,
    'preço': y
  }

print(modelo_geral)
df_modelo_geral = pd.DataFrame(modelo_geral)

#Analisando a correlação entre as variáveis:
df_modelo_geral.corr()

plt.figure(figsize=(20,8))
sns.heatmap(df_modelo_geral.corr(), annot = True, cmap= "RdYlGn");
plt.title('Correlação de Pearson',size=15);

#Análise dos dados:
df_modelo_geral.describe()

#Analisando os box plots
df_modelo_geral[['banheiros', 'quartos', 'metros', 'pets', 'preço']].plot.box(figsize=(10,10))

#Analisando os histogramas
df_modelo_geral[['banheiros', 'quartos', 'metros', 'pets', 'preço']].hist(figsize=(20,8), bins=50)

#Plotando a distribuição de cada variável com o preço
fig,ax = plt.subplots(2,2, figsize=(20,10))
sns.scatterplot(x='banheiros',y='preço',data = df_modelo_geral,ax=ax[0][0]);
sns.scatterplot(x='quartos',y='preço',data = df_modelo_geral,ax=ax[0][1]);
sns.scatterplot(x='metros',y='preço',data = df_modelo_geral,ax=ax[1][0]);
sns.scatterplot(x='pets',y='preço',data = df_modelo_geral,ax=ax[1][1]);

# Remover linhas com NaN em qualquer das colunas relevantes para poder rodar a análise
base_limpa = df_modelo_geral.dropna(subset=['banheiros', 'quartos', 'metros', 'pets', 'preço'])

# Separar variáveis independentes e dependente
x_model = base_limpa[['banheiros', 'quartos', 'metros', 'pets']]
y = base_limpa['preço']

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(x_model, y, test_size=0.5, random_state=42)

# Criar e treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões e avaliar o modelo
y_pred = model.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

print(f"Intercepto: {model.intercept_}\nCoeficientes, em ordem de banheiros, quartos, metros e pets: {model.coef_}")

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
plt.figure(figsize=(20,5))
plt.plot(y_pred, linewidth=2, color='r')
plt.plot(y, linewidth=0.5,color='b')
plt.title('Valores preditos e os valores reais',size=15)
plt.legend(['Predições','Real'],fontsize=15)
plt.show()

#Analisando outras variavéis
#Preço por UF (amostra)
plt.bar(x_base.state[1:100],df_modelo_geral.preço[1:100])
plt.xticks(rotation=90)
plt.xlabel('Estado')
plt.ylabel('Preço')
plt.title('Preço por Estado')
plt.show()

#Preço por cidade (amostra)
plt.bar(x_base.cityname[1:20],df_modelo_geral.preço[1:20])
plt.xticks(rotation=90)
plt.xlabel('Cidade')
plt.ylabel('Preço')
plt.title('Preço por cidade')
plt.show()
