import os
from modules.onedrive_connector import get_token, listar_arquivos
from modules.analyzer import analisar_arquivo
from modules.mover import mover_arquivo
from modules.relatorio import registrar_acao

# Caminho onde os arquivos serão salvos temporariamente (você pode ajustar)
PASTA_TEMPORARIA = "downloads"
BASE_DESTINO = "Pessoa Jurídica"

def baixar_arquivo(url_download, nome_arquivo, token):
    import requests
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url_download, headers=headers)
    
    os.makedirs(PASTA_TEMPORARIA, exist_ok=True)
    caminho_local = os.path.join(PASTA_TEMPORARIA, nome_arquivo)
    
    with open(caminho_local, "wb") as f:
        f.write(response.content)

    return caminho_local

def main():
    print("🔐 Autenticando no OneDrive...")
    token = get_token()
    
    print("📂 Buscando arquivos do OneDrive...")
    arquivos = listar_arquivos(token)

    if not arquivos:
        print("⚠️ Nenhum arquivo encontrado.")
        return

    for arquivo in arquivos:
        nome = arquivo.get("name")
        url_download = arquivo.get("@microsoft.graph.downloadUrl")

        print(f"\n📄 Arquivo encontrado: {nome}")
        caminho_local = baixar_arquivo(url_download, nome, token)

        categoria = analisar_arquivo(caminho_local)
        print(f"📚 Categoria sugerida: {categoria}")

        if input("Deseja mover este arquivo? (s/n): ").lower() == "s":
            destino = mover_arquivo(caminho_local, BASE_DESTINO, categoria)
            registrar_acao(caminho_local, destino, categoria)
        else:
            print("⏭️ Arquivo ignorado.")

if __name__ == "__main__":
    main()
