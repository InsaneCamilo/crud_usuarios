import requests

BASE_URL = "http://127.0.0.1:8000/api/usuarios/"

def listar_usuarios():
    r = requests.get(BASE_URL)
    return r.json()

def crear_usuario(codigo, nombre):
    payload = {"codigo": codigo, "nombre": nombre}
    r = requests.post(BASE_URL, json=payload)
    return r.status_code == 201

def actualizar_usuario(codigo, nombre):
    url = f"{BASE_URL}{codigo}/"
    payload = {"codigo": codigo, "nombre": nombre}
    r = requests.put(url, json=payload)
    return r.status_code == 200

def eliminar_usuario(codigo):
    url = f"{BASE_URL}{codigo}/"
    r = requests.delete(url)
    return r.status_code == 204
