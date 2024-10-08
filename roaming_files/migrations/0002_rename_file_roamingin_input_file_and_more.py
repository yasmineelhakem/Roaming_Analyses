# Generated by Django 5.1 on 2024-08-23 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roaming_files', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roamingin',
            old_name='file',
            new_name='input_file',
        ),
        migrations.RemoveField(
            model_name='roamingout',
            name='file',
        ),
        migrations.AddField(
            model_name='roamingout',
            name='input_file',
            field=models.FileField(blank=True, null=True, upload_to='roaming_out_files/inputs'),
        ),
        migrations.AddField(
            model_name='roamingout',
            name='output_file',
            field=models.FileField(blank=True, null=True, upload_to='roaming_out_files/outputs/'),
        ),
    ]
