# Generated by Django 5.0.6 on 2024-06-09 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_interno', '0010_alter_tecnico_image_technical'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condominio',
            name='image_condominium',
            field=models.ImageField(blank=True, null=True, upload_to='imagens_condominio/', verbose_name='Inserir magem'),
        ),
    ]
