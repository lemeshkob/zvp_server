# Generated by Django 2.0.2 on 2018-02-27 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control_panel', '0005_auto_20180227_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_head',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='control_panel.Teacher', verbose_name='Голова'),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_head_rank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='control_panel.TeacherRank', verbose_name='Звання голови'),
        ),
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(default=None, max_length=100, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='discipline_department_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='control_panel.Department', verbose_name='Кафедра'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='discipline_name',
            field=models.CharField(max_length=100, verbose_name='Назва'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_faculty',
            field=models.CharField(default=None, max_length=15, verbose_name='Факультет або ВНЗ'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_full_name',
            field=models.CharField(default=None, max_length=200, verbose_name='ПІБ'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_grade',
            field=models.IntegerField(default=None, verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_notes',
            field=models.TextField(blank=True, default=None, verbose_name='Примітки'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_state',
            field=models.CharField(blank=True, default=None, max_length=100, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_university_group',
            field=models.CharField(default=None, max_length=10, verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_check_tests',
            field=models.BooleanField(default=False, verbose_name='Приймає контрольні'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='control_panel.Department', verbose_name='Кафедра'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_full_name',
            field=models.CharField(default=None, max_length=200, verbose_name='ПІБ'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher_rank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='control_panel.TeacherRank', verbose_name='Звання'),
        ),
        migrations.AlterField(
            model_name='teacherrank',
            name='teacher_rank',
            field=models.CharField(max_length=100, verbose_name='Звання'),
        ),
    ]
