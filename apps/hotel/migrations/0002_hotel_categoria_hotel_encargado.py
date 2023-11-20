# Generated by Django 4.2.7 on 2023-11-20 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.categoria'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='encargado',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.encargado'),
        ),
    ]
