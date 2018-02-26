from django.db import models
from django.db.models import *


class Student(models.Model):

    class Meta:
        db_table = 'Students'

    student_full_name = models.CharField(max_length=200)
    student_university_group = models.CharField(max_length=10)
    student_faculty = models.CharField(max_length=15)
    student_grade = models.IntegerField(default=None)
    student_state = models.CharField(max_length=100)
    student_notes = models.TextField()


class Teacher(models.Model):

    class Meta:
        db_table = 'Teachers'

    teacher_full_name = models.CharField(max_length=200)
    teacher_rank = models.CharField(max_length=100)
    teacher_department = models.ForeignKey('control_panel.Department.department_name')
    teacher_check_tests = models.BooleanField(default=False)


class Department(models.Model):

    class Meta:
        db_table = 'Departments'

    department_name = models.CharField(max_length=100)
    department_head = models.ForeignKey(Teacher.teacher_full_name)
    department_head_rank = models.ForeignKey(Teacher.teacher_rank)


class Discipline(models.Model):

    class Meta:
        db_table = 'Disciplines'

    discipline_name = models.CharField(max_length=100)
    discipline_department_name = models.ForeignKey(Department.department_name)


class Troop(models.Model):

    class Meta:
        db_table = 'Troops'

    troop_id = models.IntegerField(default=None)
    troop_head = models.ForeignKey(Teacher.teacher_full_name)
    troop_head_rank = models.ForeignKey(Teacher.teacher_rank)
    troop_department = models.ForeignKey(Department.department_name)

