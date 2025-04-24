import os
import pandas as pd

CAMINHO_RELATORIO = "relatorio_movimentacoes.xlsx"

def registrar_acao(origem, destino, categoria):
    # Verifica se o relatório já existe
    if os.path.exists(CAMINHO_RELATORIO):
        df = pd.read_excel(CAMINHO_RELATORIO)
    else:
        df = pd.DataFrame(columns=["Arquivo", "Categoria", "Origem", "Destino"])

    # Nome do arquivo
    nome_arquivo = os.path.basename(origem)

    # Adiciona nova linha
    nova_linha = {
        "Arquivo": nome_arquivo,
        "Categoria": categoria,
        "Origem": origem,
        "Destino": destino
    }

    df = df._append(nova_linha, ignore_index=True)
    df.to_excel(CAMINHO_RELATORIO, index=False)
    print(f"[LOG] Registro salvo: {nome_arquivo} → {categoria}")
