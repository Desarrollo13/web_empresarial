# Generated by Django 3.2.3 on 2021-05-20 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Blog', verbose_name='Imagen'),
        ),
    ]