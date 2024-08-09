# Generated by Django 4.1 on 2024-03-20 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualExpert', '0012_rename_arn_no_hiringmanager_aadhaar_card_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('not_id', models.TextField(null=True)),
                ('noter_id', models.TextField(null=True)),
                ('not_message', models.TextField(null=True)),
                ('notify_id', models.TextField(null=True)),
                ('is_read', models.BooleanField(default=False, null=True)),
                ('notify_date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
