# Generated by Django 5.0.4 on 2024-05-07 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='book',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]