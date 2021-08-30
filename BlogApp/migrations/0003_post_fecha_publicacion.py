# Generated by Django 3.2.6 on 2021-08-30 15:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_post_tag_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha_publicacion',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
