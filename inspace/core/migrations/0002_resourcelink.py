from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.URLField(unique=True, verbose_name='Url')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources_links', to='core.Planet', verbose_name='Planet')),
            ],
            options={
                'verbose_name': 'Resource Link',
                'verbose_name_plural': 'Resources Links',
                'db_table': 'resources_links',
                'ordering': ('title',),
            },
        ),
    ]
