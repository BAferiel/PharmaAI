# Generated by Django 5.0.2 on 2024-03-28 07:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0014_alter_obesitydisorder_activitylevel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="obesitydisorder",
            name="activityLevel",
            field=models.CharField(
                choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")], max_length=10
            ),
        ),
    ]