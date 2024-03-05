#%%
import pandas as pd

#%%
# Series
serie_receita = pd.Series(data=[1, 4, 10, 100000, 200, None],
                          name="receita")

#%%
# Mostrando a série criada
print("Nossa serie: ", serie_receita)
print("Tipo da nossa série: ", type(serie_receita))

#%%
# DataFrame
dados = {"nome": ["Téo", "Nah", "Code", "Karlla"],
         "sobrenome": ["Calvo", "Ataide", "Show", "Mag"],
         "idade": [28, 30, 32, 30]}

df_pessoas = pd.DataFrame(dados)

#%%
## Começando a aula...

#%%
# Lendo um csv...
df_candidatura = pd.read_csv("../data/tb_candidatura_2018.csv", sep=";")
df_candidatura.head()

#%%
# Lendo um xlsx
df_declaracao = pd.read_excel("../data/tb_declaracao_2018.xlsx")
df_declaracao.head()

#%%
#############################
# Brincando com o DataFrame...
#############################

#%%
# Número de linhas para serem exibidas a partir da primeira
df_candidatura.head(2) # Isso é um método

#%%
# Número de linhas para serem exibidas a partir da última
df_candidatura.tail(2) # Isso é um método

#%%
# Número de linhas e colunas de um DataFrame (tupla)
df_candidatura.shape[0] # Isso é um atributo

# %%
# Quais são as colunas do DataFrame?? Sabemos que temos 45 colunas
df_candidatura.columns # Isso é um atributo

# %%
# Navegando pelas colunas do DataFrame...
df_candidatura["nome"] # Retorna séries com do nome, ou coluna , melhor dizendo

#%%
colunas_selecionadas = ["nome", "cpf", "descricao_ocupacao"]
df_candidatura[colunas_selecionadas].head()

#%%
# del df_candidatura
# apaga um objeto

#%%
# Navegando pelas colunas e linhas do DataFrame
df_candidatura["nome"][29140] # df[column][index]

#%%
# Informações do DataFrame...
df_candidatura.info()

#%%
# Navegando apenas nas linhas
df_candidatura.iloc[29140:29145]

# %%

