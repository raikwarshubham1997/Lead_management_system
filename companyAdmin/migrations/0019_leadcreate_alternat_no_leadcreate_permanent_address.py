# Generated by Django 4.1.3 on 2022-11-23 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyAdmin', '0018_calllogs_lead_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadcreate',
            name='alternat_no',
            field=models.CharField(default='12:05', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leadcreate',
            name='permanent_address',
            field=models.CharField(default='1', max_length=500),
            preserve_default=False,
        ),
    ]
