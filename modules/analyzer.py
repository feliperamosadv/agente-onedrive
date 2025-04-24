import os
from modules.ocr_reader import extrair_texto_pdf
from modules.classifier import classificar_documento

def analisar_arquivo(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"[ERRO] Arquivo não encontrado: {caminho_arquivo}")
        return None

    try:
        texto_extraido = extrair_texto_pdf(caminho_arquivo)
        categoria = classificar_documento(texto_extraido)
        return categoria
    except Exception as e:
        print(f"[ERRO AO ANALISAR] {caminho_arquivo}: {e}")
        return None
