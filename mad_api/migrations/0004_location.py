# Generated by Django 4.1.5 on 2023-01-15 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mad_api', '0003_comment_edited'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('city', models.CharField(max_length=75)),
                ('state', models.CharField(max_length=75)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mad_api.event')),
            ],
        ),
    ]
