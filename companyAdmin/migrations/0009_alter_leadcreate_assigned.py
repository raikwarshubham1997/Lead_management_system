# Generated by Django 4.1.3 on 2022-11-21 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companyAdmin', '0008_alter_leadcreate_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadcreate',
            name='assigned',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
