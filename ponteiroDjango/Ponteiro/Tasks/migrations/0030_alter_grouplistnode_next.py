# Generated by Django 4.2.7 on 2023-11-10 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0029_alter_linkedlist_head_alter_linkedlist_nodetype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouplistnode',
            name='next',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tasks.grouplistnode'),
        ),
    ]
