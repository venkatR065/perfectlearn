# Generated by Django 3.2.5 on 2021-08-06 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
