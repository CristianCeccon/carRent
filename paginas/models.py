from django.db import models

# Create your models here.

#________________________ EXEMPLO 1 _______________________________

ESTADOS = [

    ("PR", "Paraná"),
    ("MT", "Mato Grosso"),
    ("AP", "Amapá"),

]


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)

    estados = models.CharField(
        max_length=2,
        choices=ESTADOS,
        default=ESTADOS[1],
    )

    def __str__(self):
        return '{} ({})'.format(self.nome, self.estado)


class Pessoa(models.Model):
  nome_completo = models.CharField(
      max_length=50, verbose_name="Qual seu nome?", help_text="Digite seu nome completo")
  nascimento = models.DateField(verbose_name='Data de nascimento')
  email = models.EmailField(max_length=100)  # ja ira validar o EMAIL
  cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

  def __str__(self):
      return '{} ({})'.format(self.nome, self.nascimento)
