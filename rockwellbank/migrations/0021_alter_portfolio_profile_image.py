# Generated by Django 5.1.1 on 2024-09-11 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rockwellbank', '0020_alter_portfolio_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio_images/'),
        ),
    ]
