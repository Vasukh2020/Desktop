# Generated by Django 4.0.5 on 2022-06-29 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('side', '0003_alter_post_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='owner',
            field=models.TextField(),
        ),
    ]
