# Generated by Django 4.0.3 on 2022-04-30 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='estados',
        ),
        migrations.AddField(
            model_name='cidade',
            name='estados',
            field=models.CharField(choices=[('PR', 'Paraná'), ('MT', 'Mato Grosso'), ('AP', 'Amapá')], default=('MT', 'Mato Grosso'), max_length=2),
        ),
    ]
