# Generated by Django 5.0.4 on 2024-05-09 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_otherlink_display_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallink',
            name='text',
            field=models.CharField(default='whatsapp account', max_length=35),
            preserve_default=False,
        ),
    ]