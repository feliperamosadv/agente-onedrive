import os
import requests
from msal import ConfidentialClientApplication
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

def get_token():
    app = ConfidentialClientApplication(
        client_id=os.getenv("CLIENT_ID"),
        client_credential=os.getenv("CLIENT_SECRET"),
        authority=os.getenv("AUTHORITY")
    )
    result = app.acquire_token_for_client(scopes=[os.getenv("SCOPE")])
    print("[DEBUG] Conteúdo da resposta:", result)
    return result["access_token"]

def listar_arquivos(token, pasta_id=None):
    url_base = "https://graph.microsoft.com/v1.0/drives"

    if pasta_id:
        url = f"{url_base}/items/{pasta_id}/children"
    else:
        url = f"{url_base}/root/children"

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get("value", [])
    else:
        print(f"[ERRO] Falha ao listar arquivos: {response.status_code}")
        return []
