# Generated by Django 3.1.2 on 2020-10-20 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfaudio',
            name='audio_rate',
            field=models.IntegerField(blank=True, default=125, null=True),
        ),
        migrations.AlterField(
            model_name='pdfaudio',
            name='audio_voice',
            field=models.CharField(choices=[('0', 'Male'), ('1', 'Female')], default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='pdfaudio',
            name='volume_level',
            field=models.DecimalField(blank=True, decimal_places=1, default=1.0, max_digits=2, null=True),
        ),
    ]
