from tabnanny import verbose
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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

class Funcionario(models.Model):
  nome_completo = models.CharField(max_length=50, verbose_name="Qual seu nome?", help_text="Digite seu nome completo")
  nascimento = models.DateField(verbose_name='Data de nascimento')
  email = models.EmailField(max_length=100)  # ja ira validar o EMAIL
  contato=models.IntegerField(verbose_name='Numero de celular:', help_text="Exemplo: 44997253416", validators=[MaxValueValidator(15)])
  cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

# class Funcionario():
#     usuario = models.CharField(max_length=20, verbose_name="Qual usuario para logar no sistema ?", help_text="Exemplo: Fulano123")
#     senha = models.CharField(max_length=30, verbose_name="Qual a senha para logar ?", help_text="Exemplo: SenhaFulano123")

class Cliente():
    codigo = models.CharField(max_length=10)
    

class Veiculo(models.Model):
  nome = models.CharField(max_length=50, verbose_name="Qual é o veiculo ?", help_text="Exemplo: Mazda RX7")
  data = models.DateField(verbose_name='Data do veiculo', help_text="Exemplo: 06/02/2014")
  cor = models.CharField(max_length=20, verbose_name= "Qual a cor do veiculo ?", help_text="Exemplo: Vermelho, Prata, Preto...")
  diaria = models.IntegerField(verbose_name="Qual o valor da diaria do veiculo ?", help_text="Exemplo: 150, 200, 500 ...")
  qtn_bancos = models.IntegerField(
    verbose_name="Qual a quantidade de bancos do veiculo ?", help_text="Exemplo: 3, 4, 5 ...", validators=[MaxValueValidator(8)])
  gasto_gasolina_km = models.IntegerField(verbose_name="Quanto que o veiculo gasta de gasolina por KM ?", help_text="Exemplo: 3, 4, 5 ...", validators=[MaxValueValidator(10), MinValueValidator(1)])
  modelo_motor = models.CharField(max_length=20, verbose_name="Qual o modelo do motor ?")
  velocidade_max = models.CharField(max_length=50, verbose_name="Qual a velocidade maxima do veiculo ?")

class Reserva(models.Model):
    codigo = models.CharField(max_length=10)
    inicio = models.DateField(verbose_name="Data da reserva do veiculo")
    fim = models.DateField(verbose_name="Data da entrega do veiculo")

class Usuario():
  name = models.CharField(max_length=50, verbose_name="Qual é o nome do veiculo ?", help_text="Exemplo: Fulado de tal")
