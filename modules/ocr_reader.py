import pdfplumber
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os

# Caminho para o Tesseract OCR instalado no Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extrair_texto_pdf(caminho_pdf):
    try:
        texto_comum = ''
        with pdfplumber.open(caminho_pdf) as pdf:
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                texto_comum += texto if texto else ''
    except Exception as e:
        print("Erro ao extrair texto do PDF:", e)
        texto_comum = ''
    
    return texto_comum
