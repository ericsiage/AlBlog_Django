# Generated by Django 3.2.6 on 2021-08-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag_titulo',
            field=models.CharField(default='Blog', max_length=255),
        ),
    ]