# Generated by Django 5.0.4 on 2024-05-08 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_nin_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='image',
            field=models.ImageField(default='null', storage='/users', upload_to=''),
            preserve_default=False,
        ),
    ]