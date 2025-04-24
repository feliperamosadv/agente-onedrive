def classificar_documento(texto):
    texto = texto.lower()

    if "cartão cnpj" in texto or "cadastro nacional da pessoa jurídica" in texto:
        return "1 - DOCUMENTOS"
    elif "razão social" in texto and "cnpj" in texto:
        return "1 - DOCUMENTOS"
    elif "contrato social" in texto:
        return "1 - DOCUMENTOS"
    elif "petição" in texto or "excelentíssimo senhor juiz" in texto:
        return "2.4 PROCESSOS JUDICIAIS/03 - PETIÇÕES"
    elif "protocolo" in texto and "cartório" in texto:
        return "2.1 ALTERAÇÃO CONTRATUAL/02 - CUSTAS"
    elif "despacho" in texto:
        return "2.4 PROCESSOS JUDICIAIS/04 - DESPACHOS"
    elif "decisão" in texto or "decide-se" in texto:
        return "2.4 PROCESSOS JUDICIAIS/05 - DECISÕES"
    elif "recurso" in texto or "agravo" in texto or "apelação" in texto:
        return "2.4 PROCESSOS JUDICIAIS/06 - RECURSOS"
    elif "execução" in texto or "cumprimento de sentença" in texto:
        return "2.4 PROCESSOS JUDICIAIS/07 - EXECUÇÃO"
    
    return "outros"
