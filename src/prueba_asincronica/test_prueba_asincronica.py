import asyncio
import pytest
import httpx
from prueba_asincronica import fetch_all

@pytest.mark.asyncio
async def test_fetch_all():
    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3"
    ]
    
    results = await fetch_all(urls)
    
    assert len(results) == 3
    assert "title" in results[0]  # Verifica que la respuesta contenga un campo esperado

if __name__ == "__main__":
    pytest.main()