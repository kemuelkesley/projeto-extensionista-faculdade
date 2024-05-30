from django.db import models


class Operacional(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False)
    descripiton = models.TextField(max_length=200)
    image = models.ImageField(upload_to='imagens_operacionais/')
    activate = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Operacional'
              

    def __str__(self):
        return self.title 


# class Tecnico(models.Model):
#     pass


# class Condominio(models.Model):
#     pass


class Sobre(models.Model):
    description = models.TextField(max_length=1000, null=True)
    image_company = models.ImageField(upload_to='imagens_sobre/')
    activate = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Sobre'

    def __str__(self):
        return f"Descrição da Página Sobre - {self.description[:25]}"    
    