from django.db import models


class Genero(models.Model):
    nome = models.CharField(blank=True, max_length=50)


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'


class Cargo(models.Model):
    nome = models.CharField(max_length=500)
    salario = models.DecimalField(blank=True, max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'






class Colaborador(models.Model):
    nome = models.CharField(max_length=500)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    ativo = models.BooleanField(default=True, blank=False)
    curriculo = models.FileField(blank=True)
    foto = models.ImageField(upload_to='Colaboradores', blank=True,
                             null=True, verbose_name='Foto do Colaborador')
    # telefone = PhoneNumberField(null=False)
    telefone = models.CharField(
        max_length=11, null=True, verbose_name='Nº de telefone', blank=True)
    peso = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank=True)
    altura = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank=True)
    # Blank=False --> O campo será obrigatório
    Cargo = models.ForeignKey('colaborador.Cargo', on_delete=models.CASCADE)
    Genero = models.ForeignKey('colaborador.Genero', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} ({self.pk})'

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'
