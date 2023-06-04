# Generated by Django 4.2.1 on 2023-05-24 23:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "category_id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="Serial Number"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("post_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=250)),
                ("excerpt", models.TextField(null=True)),
                ("content", models.TextField()),
                ("slug", models.SlugField(max_length=250, unique_for_date="published")),
                ("published", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "status",
                    models.CharField(
                        choices=[("draft", "Draft"), ("published", "Published")],
                        default="published",
                        max_length=10,
                    ),
                ),
            ],
            options={"ordering": ("-published",),},
        ),
    ]
