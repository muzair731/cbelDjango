# Generated by Django 3.1.4 on 2021-01-06 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='file_upload',
            fields=[
                ('ids', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=255)),
                ('my_file', models.FileField(upload_to='')),
            ],
        ),
    ]
