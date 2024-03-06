from fastapi import APIRouter, status
from fastapi.responses import JSONResponse #retorno padronizado para o HTTP
from servico import atualizar_cadastro, buscar_cadastro, adicionar_cadastro, atualizar_parcial_cadastro, deletar_cadastro
from model import Pessoa, PessoaAtualizada

route = APIRouter()

#endpoint GET
@route.get("/pessoas")
def buscar_pessoas():
    dados_brutos= buscar_cadastro()
    resultado = Pessoa.validacao_banco(dados_brutos)
    return JSONResponse(status_code= status.HTTP_200_OK, content=resultado)

    
#endpoint POST
@route.post("/pessoas")
def adicionar_pessoas(pessoa: Pessoa):
    adicionar_cadastro(pessoa)
    return JSONResponse(status_code= status.HTTP_201_CREATED, content="Cadastro feito com sucesso")


#endpoint PUT
@route.put("/pessoas")
def atualizar_pessoas(pessoa: PessoaAtualizada, id: int):
    atualizar_cadastro(pessoa, id)
    return JSONResponse(status_code= status.HTTP_200_OK, content="Atualizado com sucesso")


#endpoint PATCH
@route.patch("/pessoas")
def atualizar_parcial_pessoas(pessoa: PessoaAtualizada, id: int):
    atualizar_parcial_cadastro(pessoa, id)
    return JSONResponse(status_code= status.HTTP_200_OK, content="Atualizado parcialmente com sucesso")


#endpoint DELETE
@route.delete("/pessoas")
def deletar_pessoas(id: int):
    deletar_cadastro(id)
    return JSONResponse(status_code= status.HTTP_200_OK, content="Deletado com sucesso")