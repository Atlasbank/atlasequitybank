# Generated by Django 5.1.1 on 2024-09-10 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rockwellbank', '0011_transactions_account_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='account_number',
            new_name='beneficiary_phone_number',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='sender_phone_number',
        ),
        migrations.AlterField(
            model_name='transactions',
            name='account_name',
            field=models.CharField(max_length=200),
        ),
    ]
