# Novo agente OCR local com suporte expandido
# Arquivo: agente_ocr_local.py

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from modules.analyzer import analisar_arquivo as processar_arquivo
from modules.utils import salvar_resultados_multiformato

PASTA_ENTRADA = "entrada"
PASTA_SAIDA = "saida"

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        caminho = event.src_path
        nome = os.path.basename(caminho)
        print(f"\n📄 Novo arquivo detectado: {nome}")

        conteudo, extensao = processar_arquivo(caminho)

        if conteudo:
            salvar_resultados_multiformato(nome, conteudo, PASTA_SAIDA)
        else:
            print("❌ Formato não suportado ou erro ao processar o arquivo.")

if __name__ == "__main__":
    print("🚀 Monitorando a pasta 'entrada/'...")
    os.makedirs(PASTA_ENTRADA, exist_ok=True)
    os.makedirs(PASTA_SAIDA, exist_ok=True)

    observer = Observer()
    observer.schedule(Handler(), path=PASTA_ENTRADA, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
