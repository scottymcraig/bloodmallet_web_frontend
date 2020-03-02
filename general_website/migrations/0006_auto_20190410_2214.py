# Generated by Django 2.1.8 on 2019-04-10 20:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('general_website', '0005_auto_20190407_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='uuid',
        ),
        migrations.AddField(
            model_name='simulation',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='Uuid used to identify a specific simulation.'),
        ),
    ]