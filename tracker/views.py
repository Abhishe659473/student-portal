from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Subject, Exam, Attendance, Mark


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_no = request.POST.get('roll_no')
        class_name = request.POST.get('class_name')
        section = request.POST.get('section')

        Student.objects.create(
            name=name,
            roll_no=roll_no,
            class_name=class_name,
            section=section
        )
        return redirect('student_list')

    return render(request, 'add_student.html')


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)

    attendance_records = Attendance.objects.filter(student=student).select_related('subject')
    marks = Mark.objects.filter(student=student).select_related('subject', 'exam')

    # simple attendance % per subject
    attendance_summary = {}
    for rec in attendance_records:
        subj = rec.subject.name
        if subj not in attendance_summary:
            attendance_summary[subj] = {'present': 0, 'total': 0}
        attendance_summary[subj]['total'] += 1
        if rec.status == 'P':
            attendance_summary[subj]['present'] += 1

    for subj, data in attendance_summary.items():
        data['percentage'] = round((data['present'] / data['total']) * 100, 2) if data['total'] > 0 else 0

    # average marks per subject
    marks_summary = {}
    for m in marks:
        subj = m.subject.name
        if subj not in marks_summary:
            marks_summary[subj] = {'total_marks': 0, 'count': 0}
        marks_summary[subj]['total_marks'] += float(m.marks_obtained)
        marks_summary[subj]['count'] += 1

    for subj, data in marks_summary.items():
        data['average'] = round(data['total_marks'] / data['count'], 2) if data['count'] > 0 else 0

    context = {
        'student': student,
        'attendance_records': attendance_records,
        'marks': marks,
        'attendance_summary': attendance_summary,
        'marks_summary': marks_summary,
    }
    return render(request, 'student_detail.html', context)


def add_attendance(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    subjects = Subject.objects.all()

    if request.method == 'POST':
        subject_id = request.POST.get('subject')
        date = request.POST.get('date')
        status = request.POST.get('status')

        subject = get_object_or_404(Subject, pk=subject_id)

        Attendance.objects.create(
            student=student,
            subject=subject,
            date=date,
            status=status
        )
        return redirect('student_detail', pk=student.id)

    return render(request, 'add_attendance.html', {
        'student': student,
        'subjects': subjects,
    })


def add_mark(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    subjects = Subject.objects.all()
    exams = Exam.objects.all()

    if request.method == 'POST':
        subject_id = request.POST.get('subject')
        exam_id = request.POST.get('exam')
        marks_obtained = request.POST.get('marks_obtained')

        subject = get_object_or_404(Subject, pk=subject_id)
        exam = get_object_or_404(Exam, pk=exam_id)

        Mark.objects.create(
            student=student,
            subject=subject,
            exam=exam,
            marks_obtained=marks_obtained
        )
        return redirect('student_detail', pk=student.id)

    return render(request, 'add_mark.html', {
        'student': student,
        'subjects': subjects,
        'exams': exams,
    })

