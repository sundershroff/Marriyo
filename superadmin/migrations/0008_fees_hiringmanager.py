# Generated by Django 5.0 on 2024-08-28 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0007_dummy_matching_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='fees_hiringmanager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees', models.TextField(null=True)),
            ],
        ),
    ]
