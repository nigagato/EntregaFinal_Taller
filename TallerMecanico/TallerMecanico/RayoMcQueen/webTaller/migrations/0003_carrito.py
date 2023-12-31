# Generated by Django 4.2.2 on 2023-07-03 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webTaller', '0002_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField(default=0)),
                ('total', models.IntegerField()),
            ],
        ),
    ]
