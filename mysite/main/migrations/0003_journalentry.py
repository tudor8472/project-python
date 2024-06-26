# Generated by Django 5.0.1 on 2024-01-18 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_todolist_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_title', models.CharField(max_length=200)),
                ('entry_date', models.DateField()),
                ('entry_content', models.TextField()),
            ],
        ),
    ]
