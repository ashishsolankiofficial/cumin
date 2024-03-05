# Generated by Django 5.0.3 on 2024-03-05 16:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ext_id', models.CharField(max_length=10)),
                ('active', models.BooleanField(default=True)),
                ('disable_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayableCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MultiChoice',
            fields=[
                ('playable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='playable.playable')),
                ('description', models.TextField()),
            ],
            bases=('playable.playable',),
        ),
        migrations.CreateModel(
            name='PlayableGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ext_id', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='playable_groups', to='playable.playablecategories')),
            ],
        ),
        migrations.AddField(
            model_name='playable',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='playables', to='playable.playablegroup'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='playable.multichoice')),
            ],
        ),
    ]
