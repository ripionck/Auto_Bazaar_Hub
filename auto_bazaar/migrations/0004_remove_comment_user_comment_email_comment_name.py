# Generated by Django 5.0 on 2023-12-17 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_bazaar', '0003_alter_comment_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='abul', max_length=100),
        ),
    ]
