#%%
import pandas as pd
import numpy as np
import os

pd.set_option("display.max_columns", 5)

endereco_programa = os.path.join(os.path.abspath("."), "src") # raiz do projeto
endereco_programa = os.path.dirname(os.path.abspath(__file__))
endereco_projeto = os.path.dirname(endereco_programa)
endereco_dados = os.path.join(endereco_projeto, "data")

# %%
df_candidatura = pd.read_csv(os.path.join(endereco_dados, "tb_candidatura_2018.csv"), sep=";")
df_candidatura

#%%
df_candidatura.head()

#%% 
# Combinando e modificando colunas
df_candidatura.columns

#%%
df_candidatura[["idade_data_eleicao", "idade_data_posse"]]

#%%
df_candidatura[["idade_data_eleicao", "idade_data_posse"]].dtypes

#%%
tipos_colunas = df_candidatura[["idade_data_eleicao", "idade_data_posse"]].info()
type(tipos_colunas)
print(tipos_colunas)

#%%

idades_nova = ["idade_eleicao", "idade_posse"]
idades_velha = ["idade_data_eleicao", "idade_data_posse"]

# Aqui da pal!!! Tem dado faltando
df_candidatura[idades_nova] = df_candidatura[idades_velha].astype(int)

#%%
df_candidatura[idades_velha].describe()

#%%
# Forma 1 de remover faltantes
del df_candidatura["idade_data_eleicao"] # Deleta a coluna

#%%
df_candidatura.columns

#%%
# Forma 2 de remover faltantes
df_candidatura_novo = df_candidatura.dropna(how="all", axis=1).copy() # Retorna um DataFrame novo!!
df_candidatura_novo.head()

#%%
df_candidatura_novo.columns

#%%
# Finarmente arteramo a coluna!!
df_candidatura_novo["idade_data_posse"] = df_candidatura_novo["idade_data_posse"].astype(int)

#%%
df_candidatura_novo["idade_data_posse"].dtypes

#%%
# Calculando o log da idade?
df_candidatura_novo["idade_data_posse_log"] = np.log(df_candidatura_novo["idade_data_posse"])

#%%
df_candidatura_novo[["idade_data_posse", "idade_data_posse_log"]].head()

#%%
# Inventando moda, isso não faz sentido
df_candidatura_novo["campo_maluco"] = (df_candidatura_novo["idade_data_posse"] + df_candidatura_novo["idade_data_posse_log"]) * 2
df_candidatura_novo

#%%
df_candidatura_novo[["idade_data_posse", "idade_data_posse_log", "campo_maluco"]].head()

#%%
# Vamos elaborar mais...
def pega_primeiro_nome(nome:str):
    return nome.lstrip(" ").split(" ")[0]

df_candidatura_novo["primeiro_nome"] = df_candidatura_novo["nome"].apply(pega_primeiro_nome)

#%%
df_candidatura_novo[["nome", "primeiro_nome"]].head()

#%%
# Brincar com email
df_candidatura_novo["provedor"] = df_candidatura_novo["email"].fillna("").apply(lambda x: x.rstrip(" ").split("@")[-1])

#%%
df_candidatura_novo[["email", "provedor"]]