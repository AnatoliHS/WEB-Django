# Generated by Django 4.2.16 on 2025-03-03 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiences', '0007_group_is_public_group_last_modified_person_is_public_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelVisibilitySettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(choices=[('person', 'People'), ('group', 'Activity Groups'), ('participation', 'Participations'), ('role', 'Roles'), ('pathways', 'Pathways'), ('badges', 'Badges')], help_text="Select which model's visibility to control", max_length=50, unique=True)),
                ('access_level', models.CharField(choices=[('public', 'Public - Anyone can view'), ('authenticated', 'Authenticated - Any logged in user'), ('staff', 'Staff Only'), ('disabled', 'Disabled - No access (404)')], default='staff', help_text="Who can access this model's views", max_length=20)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Model Visibility Setting',
                'verbose_name_plural': 'Model Visibility Settings',
                'ordering': ['model_name'],
            },
        ),
    ]
