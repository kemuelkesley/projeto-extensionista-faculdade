from django.db import models


class Operacional(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False)
    descripiton = models.TextField(max_length=200)
    image = models.ImageField(upload_to='imagens_operacionais/')
    activate = models.BooleanField(verbose_name='Ativar', default=True)
    created_at = models.DateTimeField(verbose_name='Data de publicação',auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Operacional'
              

    def __str__(self):
        return self.title 



class Categoria(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False)      
    activate = models.BooleanField(verbose_name='Ativar', default=True)
    created_at = models.DateTimeField(verbose_name='Data de publicação',auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Categoria'
              

    def __str__(self):
        return self.title


class Tecnico(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False)
    description = models.TextField(max_length=300)
    image_technical = models.ImageField(upload_to='imagens_tecnicos/')
    category = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'Tecnico'

    def __str__(self):
        return self.title
            

class Condominio(models.Model):
    condominium_number = models.CharField(verbose_name='Número do Condominio',max_length=100)
    condominium_name = models.CharField(verbose_name='Nome',max_length=100)
    title = models.CharField(verbose_name='Titulo',max_length=60)
    description = models.TextField(verbose_name='Descrição',max_length=250)
    image_condominium = models.ImageField(verbose_name='Inserir magem',upload_to='imagens_condominio/')
    activate = models.BooleanField(verbose_name='Ativar', default=True)
    created_at = models.DateTimeField(verbose_name='Data de publicação',auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Condominio'

    def __str__(self):
        return self.condominium_name   


class Sobre(models.Model):
    description = models.TextField(max_length=1000, null=True)
    image_company = models.ImageField(upload_to='imagens_sobre/')
    activate = models.BooleanField(verbose_name='Ativar',default=True)
    created_at = models.DateTimeField(verbose_name='Data de publicação',auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Sobre'

    def __str__(self):
        return f"Descrição da Página Sobre - {self.description[:35]}"    
    