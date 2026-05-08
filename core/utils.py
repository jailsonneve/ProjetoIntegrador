from .models import Perfil
from clientes.models import Cliente
from motoristas.models import Motorista
from fornecedores.models import Fornecedor
import re

def get_perfil(user):
    from .models import Perfil, Filial

    perfil = Perfil.objects.filter(user=user).first()

    if perfil:
        return perfil

    # pega uma filial padrão (ou cria uma)
    filial = Filial.objects.first()

    if not filial:
        raise Exception("Nenhuma filial cadastrada. Crie uma primeiro.")

    return Perfil.objects.create(user=user, filial=filial)


def validar_telefone(telefone):
    # somente numeros, sem "-" ou (xx)
    pattern = r'^\d{10,11}$'

    # validar formato
    if not re.fullmatch(pattern, telefone):
        return 'invalido'
    
    # verificar se ja esta cadastrado no banco
    classes = [Perfil, Cliente, Motorista, Fornecedor]
    for classe in classes:
        if classe.objects.filter(telefone=telefone).exists():
            return 'cadastrado'
    
    return 'valido'
