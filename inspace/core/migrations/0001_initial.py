from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Planet',
                'verbose_name_plural': 'Planets',
                'db_table': 'planets',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='core.Planet', verbose_name='Planet')),
            ],
            options={
                'verbose_name': 'Resource',
                'verbose_name_plural': 'Resources',
                'db_table': 'resources',
                'ordering': ('title',),
            },
        ),
    ]
