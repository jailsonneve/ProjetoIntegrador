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

def validar_cpf(cpf, ignorar_id=None):

    cpf = re.sub(r'\D', '', cpf)

    if len(cpf) != 11:
        return 'invalido'

    if cpf == cpf[0] * 11:
        return 'invalido'

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)

    digito1 = (soma * 10 % 11) % 10

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)

    digito2 = (soma * 10 % 11) % 10

    if digito1 != int(cpf[9]) or digito2 != int(cpf[10]):
        return 'invalido'

    # PERFIL REMOVIDO
    classes = [Cliente, Motorista, Fornecedor]

    for classe in classes:

        query = classe.objects.filter(cpf=cpf)

        if ignorar_id:
            query = query.exclude(id=ignorar_id)

        if query.exists():
            return 'cadastrado'

    return 'valido'

def validar_cnh(cnh, ignorar_id=None):

    if len(cnh) != 11 or not cnh.isdigit():
        return 'invalido'

    # PERFIL REMOVIDO
    classes = [Cliente, Motorista]

    for classe in classes:

        query = classe.objects.filter(cnh=cnh)

        if ignorar_id:
            query = query.exclude(id=ignorar_id)

        if query.exists():
            return 'cadastrado'

    return 'valido'

def validar_telefone(telefone, objeto_id=None):
    
    # somente numeros
    pattern = r'^\d{10,11}$'

    # validar formato
    if not re.fullmatch(pattern, telefone):
        return 'invalido'

    classes = [Perfil, Cliente, Motorista, Fornecedor]

    for classe in classes:

        query = classe.objects.filter(telefone=telefone)

        # ignorar o próprio registro em edição
        if objeto_id:
            query = query.exclude(id=objeto_id)

        if query.exists():
            return 'cadastrado'

    return 'valido'
