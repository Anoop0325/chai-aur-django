# Generated by Django 5.0.6 on 2024-06-24 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0003_certificate_chaireview_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaireview',
            name='rating',
            field=models.IntegerField(max_length=5),
        ),
    ]
