Student Portal – Attendance & Marks Tracker

A Django-based web application that helps institutions manage students, track attendance, and record subject-wise marks with automated performance summaries.

📌 Features

✔ Add, list, and manage students
✔ Record daily attendance per subject (Present/Absent)
✔ Store marks for multiple exams per subject
✔ Performance dashboard for every student
✔ Attendance % and average marks calculated automatically
✔ Simple and clean Bootstrap UI
✔ Admin panel to manage Subjects & Exams

🛠 Tech Stack
Layer	Technology
Backend	Python, Django
Database	SQLite
Frontend	Django Templates (HTML + Bootstrap)
Hosting (planned)	Render / PythonAnywhere
🎯 Data Model Overview
Model	Purpose
Student	Basic student details
Subject	Academic subjects
Exam	Exam names + dates
Attendance	Student + Subject + Date + Status
Mark	Student + Subject + Exam + Marks

Relational design enables subject-wise summaries for each student.

🚀 How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/Abhishe659473/student-portal.git
cd student-portal

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Apply migrations
python manage.py migrate

4️⃣ Run the server
python manage.py runserver


Open in browser:

http://127.0.0.1:8000/

🔐 Admin Panel Setup

Create a superuser:

python manage.py createsuperuser


Login:

http://127.0.0.1:8000/admin/

Add base subjects and exams before adding attendance/marks.

📸 Screenshots
Page	Preview
Student List	(screenshot here)
Student Detail	(screenshot here)
Add Attendance	(screenshot here)
Add Marks	(screenshot here)

Screenshots will be added soon.

📈 Future Enhancements

Authentication & role-based access

Export reports as PDF/Excel

Dashboard with charts for marks trends

Pagination & search filters

Deployment with CI/CD

👨‍💻 Developer

Bagatha Abhishek
Python & Backend Development Enthusiast
Hyderabad, India

📎 Repository Link

🔗 https://github.com/Abhishe659473/student-portal
