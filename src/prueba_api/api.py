from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, conint
from typing import List

app = FastAPI()

class Usuario(BaseModel):
    nombre: str
    email: EmailStr
    edad: conint(gt=0)  # Edad debe ser un número positivo

usuarios_db = []

@app.get("/usuarios", response_model=List[Usuario])
def obtener_usuarios():
    return usuarios_db

@app.post("/usuarios", response_model=Usuario)
def crear_usuario(usuario: Usuario):
    nuevo_usuario = usuario.dict()
    nuevo_usuario["id"] = len(usuarios_db) + 1
    usuarios_db.append(nuevo_usuario)
    return nuevo_usuario

@app.get("/usuarios/{id}", response_model=Usuario)
def obtener_usuario(id: int):
    for usuario in usuarios_db:
        if usuario["id"] == id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.put("/usuarios/{id}", response_model=Usuario)
def actualizar_usuario(id: int, usuario_actualizado: Usuario):
    for i, usuario in enumerate(usuarios_db):
        if usuario["id"] == id:
            usuarios_db[i] = usuario_actualizado.dict()
            usuarios_db[i]["id"] = id
            return usuarios_db[i]
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.delete("/usuarios/{id}")
def eliminar_usuario(id: int):
    for i, usuario in enumerate(usuarios_db):
        if usuario["id"] == id:
            usuarios_db.pop(i)
            return {"mensaje": "Usuario eliminado"}
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
