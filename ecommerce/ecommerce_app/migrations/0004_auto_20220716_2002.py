# Generated by Django 3.1.7 on 2022-07-16 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0003_auto_20220716_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='visitor', to='ecommerce_app.product'),
        ),
    ]
