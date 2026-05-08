from django.contrib import admin
from .models import Perfil, Filial, FilialCliente, FilialVeiculos, FilialMotoristas, FilialFornecedores, FilialDiario, FilialRotas


admin.site.register(Perfil)
admin.site.register(Filial)
admin.site.register(FilialCliente)
admin.site.register(FilialVeiculos)
admin.site.register(FilialMotoristas)
admin.site.register(FilialFornecedores)
admin.site.register(FilialDiario)
admin.site.register(FilialRotas)