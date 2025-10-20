import pandas as pd
from bs4 import BeautifulSoup
import re


def extrair_vagas_estrutura_exata(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    vagas_data = []
    
    containers = soup.find_all('div', class_='container')
    
    for container in containers:
        card_body = container.find('div', class_='card-body')
        if not card_body:
            continue
        
        # Nome da vaga
        h5_tag = card_body.find('h5', style='color:#00F')
        if not h5_tag:
            continue
        nome_vaga = h5_tag.get_text(strip=True)
        
        # Email
        email = None
        email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
        email_match = re.search(email_pattern, card_body.get_text())
        if email_match:
            email = email_match.group()
        
        dados_vaga = {
            'Nome da Vaga': nome_vaga, 
            'Email': email,
            'Requisitos': '',
            'Atividades': '',
            'Benefícios': '',
            'Observações': ''
        }
        
        # Buscar por todas as tags h6 (se existirem)
        h6_tags = card_body.find_all('h6')
        
        for h6 in h6_tags:
            strong_tag = h6.find('strong')
            if not strong_tag:
                continue
                
            secao_nome = strong_tag.get_text(strip=True)
            
            # Encontrar o próximo elemento p que contém o texto real
            elemento_atual = h6
            
            while elemento_atual:
                elemento_atual = elemento_atual.find_next_sibling()
                if not elemento_atual:
                    break
                    
                if elemento_atual.name == 'p':
                    # Verificar se este é o p com conteúdo (não o vazio)
                    texto = elemento_atual.get_text(strip=True)
                    if texto and not elemento_atual.find('br'):
                        # Este é o p com conteúdo real
                        if 'Requisitos' in secao_nome:
                            dados_vaga['Requisitos'] = texto
                        elif 'Atividades' in secao_nome:
                            dados_vaga['Atividades'] = texto
                        elif 'Benefícios' in secao_nome:
                            dados_vaga['Benefícios'] = texto
                        elif 'Observações' in secao_nome:
                            dados_vaga['Observações'] = texto
                        break
        
        # Extrair datas
        data_pattern = r'(\d{2}/\d{2}/\d{4})'
        datas = re.findall(data_pattern, card_body.get_text())
        
        if len(datas) >= 2:
            dados_vaga['Data Inserida'] = datas[-2]
            dados_vaga['Data Limite'] = datas[-1]
        elif len(datas) == 1:
            dados_vaga['Data Inserida'] = datas[0]
            dados_vaga['Data Limite'] = None
        
        vagas_data.append(dados_vaga)
    
    return vagas_data

# Função alternativa que usa uma abordagem mais direta
def extrair_vagas_direto(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    vagas_data = []
    
    containers = soup.find_all('div', class_='container')
    
    for container in containers:
        card_body = container.find('div', class_='card-body')
        if not card_body:
            continue
        
        # Nome da vaga
        h5_tag = card_body.find('h5', style='color:#00F')
        if not h5_tag:
            continue
        nome_vaga = h5_tag.get_text(strip=True)
        
        # Email
        email = None
        email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
        email_match = re.search(email_pattern, card_body.get_text())
        if email_match:
            email = email_match.group()
        
        dados_vaga = {
            'Nome da Vaga': nome_vaga, 
            'Email': email,
            'Requisitos': '',
            'Atividades': '',
            'Benefícios': '',
            'Observações': ''
        }
        
        # Extrair conteúdo baseado na estrutura exata
        texto_completo = card_body.get_text()
        
        # Extrair Requisitos
        requisitos_match = re.search(r'Requisitos\s*(.*?)(?=Atividades|Benefícios|Observações|Inserida em:|$)', texto_completo, re.DOTALL)
        if requisitos_match:
            dados_vaga['Requisitos'] = requisitos_match.group(1).strip()
        
        # Extrair Atividades
        atividades_match = re.search(r'Atividades\s*(.*?)(?=Benefícios|Observações|Inserida em:|$)', texto_completo, re.DOTALL)
        if atividades_match:
            dados_vaga['Atividades'] = atividades_match.group(1).strip()
        
        # Extrair Benefícios
        beneficios_match = re.search(r'Benefícios\s*(.*?)(?=Observações|Inserida em:|$)', texto_completo, re.DOTALL)
        if beneficios_match:
            dados_vaga['Benefícios'] = beneficios_match.group(1).strip()
        
        # Extrair Observações
        observacoes_match = re.search(r'Observações\s*(.*?)(?=Inserida em:|É proibido|$)', texto_completo, re.DOTALL)
        if observacoes_match:
            dados_vaga['Observações'] = observacoes_match.group(1).strip()
        
        # Extrair datas
        data_pattern = r'(\d{2}/\d{2}/\d{4})'
        datas = re.findall(data_pattern, texto_completo)
        
        if len(datas) >= 2:
            dados_vaga['Data Inserida'] = datas[-2]
            dados_vaga['Data Limite'] = datas[-1]
        elif len(datas) == 1:
            dados_vaga['Data Inserida'] = datas[0]
            dados_vaga['Data Limite'] = None
        
        vagas_data.append(dados_vaga)
    
    return vagas_data

# Vamos testar com uma abordagem de debug primeiro
def debug_estrutura_vaga(html_content, numero_vaga=1):
    soup = BeautifulSoup(html_content, 'html.parser')
    containers = soup.find_all('div', class_='container')
    
    if numero_vaga <= len(containers):
        container = containers[numero_vaga-1]
        card_body = container.find('div', class_='card-body')
        
        if not card_body:
            print("Card body não encontrado para esta vaga")
            return
        
        print("=== DEBUG ESTRUTURA ===")
        print("Conteúdo completo da vaga:")
        print("-" * 50)
        
        # Mostrar todos os h6 e seus conteúdos seguintes (se existirem)
        h6_tags = card_body.find_all('h6')
        
        if h6_tags:
            for i, h6 in enumerate(h6_tags):
                print(f"\nH6 {i+1}:")
                print(f"Conteúdo H6: {h6.get_text(strip=True)}")
                
                # Mostrar próximos elementos
                next_elem = h6.next_sibling
                count = 0
                while next_elem and count < 5:
                    print(f"Próximo elemento {count+1}: {repr(str(next_elem))}")
                    next_elem = next_elem.next_sibling
                    count += 1
        else:
            print("Nenhuma tag h6 encontrada nesta vaga")
        
        print("\nTexto completo para regex:")
        print("-" * 50)
        texto = card_body.get_text()
        print(texto[:1000])  # Primeiros 1000 caracteres

# Usando as funções
try:
    with open('pagina_vagas.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Primeiro, vamos debugar a estrutura
    print("Debug da estrutura da primeira vaga:")
    debug_estrutura_vaga(html_content, 1)

    print("\n" + "="*50)
    print("Extraindo vagas com método direto (regex)...")
    vagas = extrair_vagas_direto(html_content)

    if vagas:
        # Criar DataFrame
        df = pd.DataFrame(vagas)

        # Reordenar colunas
        colunas_ordenadas = ['Nome da Vaga', 'Email', 'Data Inserida', 'Data Limite', 
                            'Requisitos', 'Atividades', 'Benefícios', 'Observações']
        
        # Garantir que todas as colunas existam no DataFrame
        for coluna in colunas_ordenadas:
            if coluna not in df.columns:
                df[coluna] = None
        
        df = df[colunas_ordenadas]

        # Salvar em Excel
        nome_arquivo = 'vagasExcel.xlsx'
        df.to_excel(nome_arquivo, index=False, engine='openpyxl')

        print(f"Foram extraídas {len(vagas)} vagas e salvas no arquivo '{nome_arquivo}'")

        # Mostrar preview detalhado
        print("\nPreview detalhado das primeiras vagas:")
        for i, vaga in enumerate(vagas[:3], 1):
            print(f"\n--- Vaga {i} ---")
            print(f"Nome: {vaga['Nome da Vaga']}")
            print(f"Email: {vaga['Email']}")
            print(f"Data Inserida: {vaga.get('Data Inserida', 'N/A')}")
            print(f"Data Limite: {vaga.get('Data Limite', 'N/A')}")
            print(f"Requisitos: {vaga['Requisitos'][:200] if vaga['Requisitos'] else 'NÃO CAPTURADO'}...")
            print(f"Atividades: {vaga['Atividades'][:200] if vaga['Atividades'] else 'NÃO CAPTURADO'}...")
            print(f"Benefícios: {vaga['Benefícios'][:150] if vaga['Benefícios'] else 'NÃO CAPTURADO'}...")
            print(f"Observações: {vaga['Observações'][:200] if vaga['Observações'] else 'NÃO CAPTURADO'}...")

        # Mostrar estatísticas
        print(f"\nEstatísticas:")
        print(f"Total de vagas: {len(vagas)}")
        print(f"Vagas com requisitos: {sum(1 for v in vagas if v['Requisitos'])}")
        print(f"Vagas com atividades: {sum(1 for v in vagas if v['Atividades'])}")
        print(f"Vagas com benefícios: {sum(1 for v in vagas if v['Benefícios'])}")
        print(f"Vagas com observações: {sum(1 for v in vagas if v['Observações'])}")
    else:
        print("Nenhuma vaga foi extraída. Verifique a estrutura do HTML.")

except FileNotFoundError:
    print("Arquivo 'pagina_vagas.html' não encontrado. Execute primeiro o código de download.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")