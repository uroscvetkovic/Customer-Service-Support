# Generated by Django 2.2.6 on 2021-08-16 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service_supports', '0003_customerservicesupport_submited_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerservicesupport',
            old_name='arhived',
            new_name='archived',
        ),
    ]
