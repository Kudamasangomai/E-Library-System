# Generated by Django 3.2.9 on 2022-01-02 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0014_alter_books_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
