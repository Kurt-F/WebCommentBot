# Generated by Django 2.0.6 on 2018-06-30 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('botinterface', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='site',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
    ]
