# Generated by Django 4.2 on 2024-08-05 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_expense_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='subcategory',
        ),
    ]
