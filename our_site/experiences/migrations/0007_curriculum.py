# Generated by Django 4.2.16 on 2025-02-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0006_pathways_badges'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Curricula',
            },
        ),
    ]
