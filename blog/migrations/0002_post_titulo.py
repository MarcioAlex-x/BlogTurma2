# Generated by Django 4.2.6 on 2023-10-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='titulo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
