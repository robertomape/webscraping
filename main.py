from fastapi import FastAPI, HTTPException
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/scrape/")
async def web_scraping(url: str):
    # Definir el User-Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # Realizar la solicitud a la URL
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lanza un error si la respuesta es un error

        # Analizar el contenido de la página
        soup = BeautifulSoup(response.content, 'html.parser')

        # Obtener todo el texto de la página
        page_content = soup.get_text()

        return {"content": page_content}

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error scraping the URL: {e}")
