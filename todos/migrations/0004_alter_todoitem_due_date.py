# Generated by Django 4.1.1 on 2022-09-08 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0003_alter_todoitem_is_completed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todoitem",
            name="due_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
