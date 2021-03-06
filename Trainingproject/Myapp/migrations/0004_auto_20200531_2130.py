# Generated by Django 3.0.3 on 2020-05-31 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0003_auto_20200529_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('verify_email', models.EmailField(max_length=30)),
                ('comment', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Myapp.Session'),
        ),
    ]
