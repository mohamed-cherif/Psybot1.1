# Generated by Django 4.1.4 on 2023-06-04 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0002_person_graph_cyb_person_graph_dep_person_graph_home_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='graph_cyb',
        ),
        migrations.RemoveField(
            model_name='person',
            name='graph_dep',
        ),
        migrations.RemoveField(
            model_name='person',
            name='graph_home',
        ),
        migrations.RemoveField(
            model_name='person',
            name='graph_sui',
        ),
    ]
