from django.contrib import admin
from .models import Student, Subject, Exam, Attendance, Mark


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name', 'class_name', 'section')
    search_fields = ('roll_no', 'name')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    list_filter = ('date',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'date', 'status')
    list_filter = ('subject', 'date', 'status')
    search_fields = ('student__name', 'student__roll_no')


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'exam', 'marks_obtained')
    list_filter = ('subject', 'exam')
    search_fields = ('student__name', 'student__roll_no')
