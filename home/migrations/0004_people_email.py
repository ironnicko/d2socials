# Generated by Django 3.2.8 on 2021-12-11 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_product_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='email',
            field=models.EmailField(default='none', max_length=256),
        ),
    ]
