import os
import shutil

def mover_arquivo(origem, base_destino, categoria):
    destino_final = os.path.join(base_destino, categoria)

    try:
        # Cria a pasta de destino se ela não existir
        os.makedirs(destino_final, exist_ok=True)

        nome_arquivo = os.path.basename(origem)
        destino_arquivo = os.path.join(destino_final, nome_arquivo)

        # Move o arquivo
        shutil.move(origem, destino_arquivo)

        print(f"[✔] Arquivo movido para: {destino_arquivo}")
        return destino_arquivo

    except Exception as e:
        print(f"[ERRO AO MOVER] {origem} → {destino_final}: {e}")
        return None
