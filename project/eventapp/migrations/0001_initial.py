# Generated by Django 3.2.7 on 2021-09-12 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=199)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('location', models.CharField(max_length=199)),
                ('image', models.ImageField(upload_to='images/')),
                ('is_liked', models.CharField(choices=[('True', 'LIKE'), ('False', 'UNLIKE')], default='False', max_length=6)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creater', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
