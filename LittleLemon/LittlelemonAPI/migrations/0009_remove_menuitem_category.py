# Generated by Django 5.0.6 on 2024-06-09 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LittlelemonAPI', '0008_alter_menuitem_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='category',
        ),
    ]