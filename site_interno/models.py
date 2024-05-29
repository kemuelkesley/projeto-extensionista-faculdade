from django.db import models



class Operacional(models.Model):
    title = models.CharField(max_length=60, blank=False, null=False)
    descripiton = models.TextField(max_length=200)
    image = models.ImageField(upload_to='imagens_operacionais/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Operacional'
              

    def __str__(self):
        return self.title 


class Tecnico(models.Model):
    pass


class Condominio(models.Model):
    pass


class Sobre(models.Model):
    pass