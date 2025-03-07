# Generated by Django 5.1.6 on 2025-02-08 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kanji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.CharField(max_length=1)),
                ('english_translation', models.CharField(max_length=100)),
                ('onyomi', models.CharField(max_length=100)),
                ('kunyomi', models.CharField(max_length=100)),
                ('stroke_count', models.IntegerField()),
                ('jlpt_level', models.IntegerField()),
                ('example_sentence', models.TextField()),
            ],
        ),
    ]
