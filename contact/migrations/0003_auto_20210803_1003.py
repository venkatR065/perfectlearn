# Generated by Django 3.2.5 on 2021-08-03 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='email',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
