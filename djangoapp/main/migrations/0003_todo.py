# Generated by Django 4.1.7 on 2023-08-03 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_discount_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="ToDo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=500, verbose_name="TODOs")),
                ("creation_date", models.DateTimeField(verbose_name="Creation date")),
            ],
        ),
    ]