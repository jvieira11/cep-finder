from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests as http

from database import salvar_cep, listar_ceps

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.post("/buscar")
async def buscar(request: Request, cep: str = Form(...)):
    cep_limpo = cep.replace("-", "").strip()
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    resposta = http.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" not in dados:
            salvar_cep(dados)
            return templates.TemplateResponse(request, "index.html", {
                "resultado": dados,
                "sucesso": True
            })

    return templates.TemplateResponse(request, "index.html", {
        "erro": "CEP não encontrado. Verifique e tente novamente."
    })


@app.get("/historico", response_class=HTMLResponse)
async def historico(request: Request):
    registros = listar_ceps()
    return templates.TemplateResponse(request, "historico.html", {
        "registros": registros
    })