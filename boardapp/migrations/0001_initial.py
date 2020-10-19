from django.db import migrations, models
import hitcount.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(blank=True, max_length=50)),
                ('item', models.CharField(max_length=10)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('year', models.DateField()),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DataroomBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(blank=True, max_length=50)),
                ('item', models.CharField(max_length=10)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('year', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DjangoBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('nick_name', models.CharField(blank=True, max_length=50)),
                ('created_date', models.DateField(blank=True, null=True)),
                ('memo', models.CharField(blank=True, max_length=200)),
                ('hits', models.IntegerField(default=0)),
            ],
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
        migrations.CreateModel(
            name='SubBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subname', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
