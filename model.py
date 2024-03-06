from pydantic import BaseModel
from typing import Optional

class Pessoa(BaseModel):
    id: int
    nome: str
    cpf: str
    celular: str
    endereco: str

    @staticmethod #tratamento do retorno que está em lista
    def validacao_banco(dados):
        lista_validada = []
        for dado in dados: #para retira o dado da lista
            pessoa = {
                'id': dado[0],
                'nome': dado[1],
                'cpf': dado[2],
                'celular': dado[3],
                'endereco': dado[4]
            }

            lista_validada.append(pessoa)
        return lista_validada


class PessoaAtualizada(BaseModel):
    nome: Optional[str] = None
    cpf: Optional[str] = None
    celular: Optional[str] = None
    endereco: Optional[str] = None

