# Generated by Django 2.2.3 on 2019-08-26 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sapp', '0004_emp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='e_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sapp.tb_registration'),
        ),
    ]