import glob
import os
import pandas as pd

diretorio_dados = "."

arquivos_mensais = glob.glob(os.path.join(diretorio_dados, "dados_mensais_*.csv"))

if arquivos_mensais:
    lista_df_mensais = []
    for arquivo in arquivos_mensais:
        df = pd.read_csv(arquivo)
        lista_df_mensais.append(df)
    df_mensal_completo = pd.concat(lista_df_mensais, ignore_index=True)
    if "Ano" in df_mensal_completo.columns:
        df_mensal_completo = df_mensal_completo.sort_values(by=["Ano"]).reset_index(
            drop=True
        )
    df_mensal_completo.to_csv(
        "dados_mensais_consolidado.csv", index=False, encoding="utf-8"
    )

arquivos_anuais = glob.glob(os.path.join(diretorio_dados, "dados_anuais_*.csv"))

if arquivos_anuais:
    lista_df_anuais = []
    for arquivo in arquivos_anuais:
        df = pd.read_csv(arquivo)
        lista_df_anuais.append(df)
    df_anual_completo = pd.concat(lista_df_anuais, ignore_index=True)
    if "Ano" in df_anual_completo.columns:
        df_anual_completo = df_anual_completo.sort_values(by=["Ano"]).reset_index(
            drop=True
        )
    df_anual_completo.to_csv(
        "dados_anuais_consolidado.csv", index=False, encoding="utf-8"
    )