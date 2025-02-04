
import fitz

def extraer_texto_completo_pdf(ruta_pdf):
    doc = fitz.open(ruta_pdf)
    texto_completo = ""
    for page in doc:
        texto_completo += page.get_text()
    doc.close()
    return texto_completo