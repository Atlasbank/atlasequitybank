# Generated by Django 5.1.1 on 2024-09-10 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rockwellbank', '0016_rename_beneficiary_phone_number_transactions_senders_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='senders_phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]