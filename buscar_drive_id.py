import os
import requests
from dotenv import load_dotenv
from msal import ConfidentialClientApplication

# Carregar variáveis do .env
load_dotenv()

# Autenticação MS Graph
app = ConfidentialClientApplication(
    client_id=os.getenv("CLIENT_ID"),
    client_credential=os.getenv("CLIENT_SECRET"),
    authority=os.getenv("AUTHORITY")
)

scopes = [os.getenv("SCOPE")]
result = app.acquire_token_for_client(scopes=scopes)

if "access_token" in result:
    token = result["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Buscar drives
    url = "https://graph.microsoft.com/v1.0/drives"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("\n✅ [INFO] Drives encontrados:")
        for drive in response.json().get("value", []):
            print(f"\n📁 Nome: {drive.get('name')}")
            print(f"🆔 ID:   {drive.get('id')}")
    else:
        print(f"\n❌ [ERRO] Código {response.status_code}")
        print(response.text)
else:
    print("\n❌ [ERRO] Falha ao obter token.")
    print(result.get("error_description"))
