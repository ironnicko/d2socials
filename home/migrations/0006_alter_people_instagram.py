# Generated by Django 3.2.8 on 2021-12-11 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_people_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='instagram',
            field=models.CharField(blank=True, default="only the id without '@' or link", max_length=256, null=True),
        ),
    ]
