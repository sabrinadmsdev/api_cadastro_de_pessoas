from pydantic import BaseModel, Field, field_validator
from typing import Optional
from validate_docbr import CPF



class Pessoa(BaseModel):
    id: int
    nome: str = Field(max_lenght=100)
    cpf: str = Field(min_length=11, max_length=11)
    celular: str = Field(max_length=11)
    endereco: str = Field(max_lenght=100)

    @field_validator('cpf') #validação do campo CPF
    def check_cpf(cls, value): #cls usamos em método da classe
        cpf = CPF()
        if cpf.validate(value):
            return value
        else:
            raise ValueError(f'CPF inválido.')
    

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

