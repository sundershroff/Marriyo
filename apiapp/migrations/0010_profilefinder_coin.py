# Generated by Django 4.2.5 on 2024-01-22 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0009_profilefinder_ads_highlights_pf_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilefinder',
            name='coin',
            field=models.TextField(null=True),
        ),
    ]
