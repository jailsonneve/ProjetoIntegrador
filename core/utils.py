from .models import Perfil

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

