# Generated by Django 3.2.8 on 2021-10-12 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('email_id', models.CharField(max_length=70)),
                ('password', models.CharField(max_length=70)),
                ('user_name', models.CharField(max_length=70)),
            ],
        ),
    ]
