# Generated by Django 3.2 on 2021-05-06 19:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapi', '0004_alter_message_conversation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
