from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    class_name = models.CharField(max_length=20)   # e.g. "B.Tech 4-1"
    section = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return f"{self.roll_no} - {self.name}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Exam(models.Model):
    name = models.CharField(max_length=50)  # e.g. "Mid-1", "Mid-2", "Final"
    date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.date})"


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('student', 'subject', 'date')

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.date} - {self.get_status_display()}"


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('student', 'subject', 'exam')

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.exam} - {self.marks_obtained}"
