# Generated by Django 3.0.5 on 2020-05-24 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hms.Person')),
            ],
        ),
    ]
