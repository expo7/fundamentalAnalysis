# Generated by Django 5.1 on 2024-08-11 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='sector',
            name='articles',
            field=models.ManyToManyField(to='stocks.article'),
        ),
    ]
