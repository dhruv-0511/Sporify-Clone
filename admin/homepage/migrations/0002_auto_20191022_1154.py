# Generated by Django 2.2.6 on 2019-10-22 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]