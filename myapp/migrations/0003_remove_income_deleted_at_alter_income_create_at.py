# Generated by Django 4.2 on 2024-08-03 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_expense_create_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='income',
            name='deleted_at',
        ),
        migrations.AlterField(
            model_name='income',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]