from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=150)
    dt_nacimento = models.DateField()
    vivo = models.BooleanField(default=True)
    pais_origem = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class livro(models.Model):

    genero_opcoes =[


        ('tr','Terro'),
        ('rn', 'Romance'),
        ('aj','Autoajuda'),
        ('av', 'Aventura'),
        ('mg', 'Manga'),
        ('hg','Historia em quadrinhos'),
        ('bg', 'Biografia'),
    ]

    titulo = models.CharField(max_length=100)
    editora = models.CharField(max_length=50)
    data_lacamento = models.DateField
    preco = models.DecimalField(decimal_places=2, max_digits=10, default=30)
    paginas = models.IntegerField()
    idioma= models.CharField(max_length=30)
    resumo = models.TextField(default='')
    genero = models.CharField(max_length=2, choices=genero_opcoes)
    nome = models.ForeignKey(Autor,on_delete=models.SET_DEFAULT, default='')


    def __str__(self):
       return self.titulo
