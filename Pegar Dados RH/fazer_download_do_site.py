import requests

def download_html(url):
    try:
        # Fazer requisição GET para a URL
        response = requests.get(url)
        
        # Verificar se a requisição foi bem-sucedida
        response.raise_for_status()
        
        # Salvar o HTML em um arquivo
        with open('pagina_vagas.html', 'w', encoding='utf-8') as file:
            file.write(response.text)
        
        print("Download concluído! HTML salvo em 'pagina_vagas.html'")
        return response.text
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer download: {e}")
        return None

# URL do site
url = "https://www.advancerh.com.br/vagas.php"

# Fazer download
html_content = download_html(url)

# Se quiser ver o conteúdo no console (primeiras 500 caracteres)
if html_content:
    print("\n--- Primeiras 500 caracteres do HTML ---")
    print(html_content[:500])