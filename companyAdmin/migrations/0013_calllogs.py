# Generated by Django 4.1.3 on 2022-11-22 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyAdmin', '0012_leadcreate_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_typ', models.CharField(max_length=50)),
                ('remark', models.CharField(max_length=250)),
            ],
        ),
    ]
