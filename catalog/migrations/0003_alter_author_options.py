# Generated by Django 4.0 on 2021-12-08 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language_alter_author_options_alter_book_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['first_name', 'last_name']},
        ),
    ]