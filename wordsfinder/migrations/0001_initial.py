# Generated by Django 3.1.6 on 2021-02-05 13:24

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='url',
            fields=[
                ('url_nm', models.URLField(primary_key=True, serialize=False)),
                ('res', jsonfield.fields.JSONField()),
            ],
        ),
    ]
