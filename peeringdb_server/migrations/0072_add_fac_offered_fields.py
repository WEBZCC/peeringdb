# Generated by Django 2.2.19 on 2021-05-03 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0071_populate_obj_counts"),
    ]

    operations = [
        migrations.AddField(
            model_name="facility",
            name="offered_power",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="The amount of power offered by the facility",
                null=True,
                verbose_name="Offered Power (kilowatts)",
                default=None,
            ),
        ),
        migrations.AddField(
            model_name="facility",
            name="offered_resilience",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Not Disclosed"),
                    ("Not Disclosed", "Not Disclosed"),
                    ("None (Best Effort)", "None (Best Effort)"),
                    ("N+1", "N+1"),
                    ("2N", "2N"),
                ],
                default="",
                max_length=64,
                verbose_name="Offered Resilience",
            ),
        ),
        migrations.AddField(
            model_name="facility",
            name="offered_space",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="The amount of space offered by the facility, in square meters",
                null=True,
                verbose_name="Offered Space (sq meters)",
                default=None,
            ),
        ),
    ]
