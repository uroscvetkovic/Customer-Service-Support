# Generated by Django 3.1.13 on 2021-08-15 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service_supports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerservicesupport',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='customerservicesupport',
            name='date_time_callback',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
