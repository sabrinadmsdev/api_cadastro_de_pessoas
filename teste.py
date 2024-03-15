

from typing import Optional

from model import Pessoa




def valida_pessoa(pessoa: Optional[Pessoa]):
    
    pessoa_antiga = Pessoa(id = 21, 
                           nome = "Joana", 
                           cpf = "12345678923", 
                           celular = "21123456782", 
                           endereco = "Rua dos bobos" )

    return pessoa.model_dump() if pessoa else pessoa_antiga


nova_pessoa_passada = Pessoa(id=21, nome="Sabrina", cpf="1823719287391", celular="1231812379812", endereco="Av amaral")
print(valida_pessoa(nova_pessoa_passada))
