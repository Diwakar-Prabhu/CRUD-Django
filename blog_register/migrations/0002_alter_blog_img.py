# Generated by Django 3.2 on 2021-05-01 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
