# Generated by Django 4.2.2 on 2023-06-15 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='svaz',
            old_name='foto',
            new_name='image',
        ),
    ]