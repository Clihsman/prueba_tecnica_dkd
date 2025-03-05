import asyncio
import httpx

urls = [
    "https://api.ejemplo.com/datos/1",
    "https://api.ejemplo.com/datos/2",
    "https://api.ejemplo.com/datos/3"
]

async def fetch(client, url):
    try:
        response = await client.get(url)
        response.raise_for_status() 
        return response.json()
    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP Error {e.response.status_code} en {url}"}
    except httpx.RequestError as e:
        return {"error": f"Error de conexión: {str(e)}"}

async def fetch_all(urls):
    transport = httpx.AsyncHTTPTransport(verify=False)
    async with httpx.AsyncClient(transport=transport) as client:
        tasks = [fetch(client, url) for url in urls]
        return await asyncio.gather(*tasks)

if __name__ == "__main__":
    import sys
    if sys.platform.startswith("win"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    results = asyncio.run(fetch_all(urls))
    for i, result in enumerate(results):
        print(f"Respuesta {i+1}: {result}")