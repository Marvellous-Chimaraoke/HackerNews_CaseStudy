# Generated by Django 3.2.8 on 2021-10-11 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('published_news', '0002_alter_comment_parent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent_id',
            field=models.IntegerField(),
        ),
    ]