# Generated by Django 4.1.7 on 2023-05-25 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0009_lease'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lease',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='lease',
            name='address_of_residence',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='lease',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='lease',
            name='explanation',
            field=models.TextField(),
        ),
    ]
