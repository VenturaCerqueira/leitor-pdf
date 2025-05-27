import pdfplumber
import pandas as pd
import re
# Caso de estudo: Extração de CPF e Nome de Servidores Públicos
# do PDF de Riachão do Jacuípe, BA
# Objetivo: Extrair os dados de CPF e Nome dos servidores públicos
# de Riachão do Jacuípe, BA, a partir de um PDF fornecido.
# O PDF contém uma lista de servidores com seus respectivos CPFs.
# O código irá ler o PDF, extrair os dados relevantes e salvar em um arquivo Excel.
# Importando as bibliotecas necessárias

# Caso de estudo: Erro funcionaria com dados estourando campo exemplo: Página 12, Linha 22: 

pdf_path = "80B72592-59B6-4E02-A0BA-39B9D1B2F7A2.pdf"
dados_servidores = []
linhas_ignoradas_log = [] 

cpf_pattern = re.compile(r"\d{3}\.\d{3}\.\d{3}-\d{2}")

def extrair_cpf_nome(linha):
    
    linha_limpa = linha.replace('"', '').replace(',', ' ').strip()
    
    
    cpf_match = cpf_pattern.search(linha_limpa)
    if not cpf_match:
        return None 
    
    cpf = cpf_match.group()
    
    
    
    partes = linha_limpa.split(cpf, 1) 
    
    antes_cpf = partes[0].strip() if len(partes) > 0 else ""
    
    nome = ""
    
    
    
    matricula_pattern = re.compile(r"^\d+") 
    matricula_match = matricula_pattern.search(antes_cpf)
    
    if matricula_match:
        
        nome = antes_cpf[matricula_match.end():].strip()
    else:
        
        nome = antes_cpf

    
    if not cpf or not nome:
        return None

    return {
        "Nome": nome.title(), 
        "CPF": cpf
    }

with pdfplumber.open(pdf_path) as pdf:
    total_linhas_lidas = 0
    total_registros_extraidos = 0
    
    for pagina_num, pagina in enumerate(pdf.pages): 
        texto = pagina.extract_text()
        if texto:
            for linha_idx, linha in enumerate(texto.split("\n")): 
                total_linhas_lidas += 1
                
                registro = extrair_cpf_nome(linha)
                if registro:
                    dados_servidores.append(registro)
                    total_registros_extraidos += 1
                else:
                    
                    linhas_ignoradas_log.append(f"Página {pagina_num + 1}, Linha {linha_idx + 1}: {linha.strip()}")

df = pd.DataFrame(dados_servidores)
output_file = "servidores_riachao_cpf_nome.xlsx" 


df.to_excel(output_file, index=False)


log_file = "linhas_ignoradas.txt"
with open(log_file, "w", encoding="utf-8") as f:
    for entrada in linhas_ignoradas_log:
        f.write(entrada + "\n")

print(f"✅ Total de linhas lidas do PDF: {total_linhas_lidas}")
print(f"✅ Total de registros (CPF e Nome) extraídos: {total_registros_extraidos}")
print(f"⚠️ Total de linhas ignoradas (não geraram um registro): {len(linhas_ignoradas_log)}")
print(f"📄 Arquivo de dados gerado: {output_file}")
print(f"📄 Log de linhas ignoradas gerado: {log_file}")