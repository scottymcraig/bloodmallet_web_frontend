# Generated by Django 2.1.8 on 2019-04-20 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general_website', '0008_auto_20190420_1549'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='simulation',
            options={'ordering': ['-created_at']},
        ),
    ]