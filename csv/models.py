from django.db import models

class Csv(models.Model): 
    identificadorURL = models.TextField()
    nome = models.TextField()
    categorias = models.TextField()
    preco = models.TextField()
    precoPromocional = models.TextField()
    peso = models.TextField()
    altura = models.TextField()
    largura = models.TextField()
    comprimento = models.TextField()
    estoque = models.TextField()
    SKU = models.TextField()
    codigoDeBarras = models.TextField()
    exibirNaLoja = models.TextField()
    freteGratis = models.TextField()
    descricao = models.TextField()
    tags = models.TextField()
    tituloParaSEO = models.TextField()
    descricaoParaSEO = models.TextField()
    marca = models.TextField()
    produtoFisico = models.TextField()
    MPN = models.TextField()
    sexo = models.TextField()
    faixaEtaria = models.TextField()
