# Generated by Django 4.2.16 on 2024-12-16 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_categoria_estoque'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='estoque',
        ),
    ]
