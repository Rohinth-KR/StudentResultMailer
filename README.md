# 🧾 StudentReportPortal

A Django-based web application that allows staff to upload student mark data via Excel, automatically process results, generate downloadable reports, and email personalized mark sheets to parents with secure one-time links.

---

## 🚀 Features

- Upload Excel sheet with student marks (Sub1, Sub2, Sub3)
- Automatically calculate Total, Average, and Pass/Fail
- Generate:
  - ✅ Excel files for Passed and Failed students
  - ✅ Individual PDF mark sheets (like a report card)
- Emails parents with secure **one-time-use download links**
- Beautiful frontend with DataTables for student records
- Admin can track all processed student results

---

## 🧩 Tech Stack

- **Backend**: Django 5+
- **Frontend**: HTML, CSS, jQuery, DataTables
- **PDF Generation**: `xhtml2pdf`
- **Excel Processing**: `pandas`
- **Database**: SQLite (default)

---

## 📂 Folder Structure


StudentReportPortal/
├── marks/
│ ├── templates/marks/
│ │ ├── upload.html
│ │ └── marksheet.html
│ ├── models.py
│ ├── views.py
│ └── urls.py
├── media/
│ ├── exports/
│ └── onetime/
├── static/
│ └── marks/
│ └── style.css
├── student_portal/
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── db.sqlite3
├── manage.py
└── README.md

Create a virtual environment:

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux
Install requirements:

pip install -r requirements.txt
(You may need to manually install pandas, xhtml2pdf, openpyxl.)

Run migrations:

python manage.py makemigrations
python manage.py migrate
Start the server:

python manage.py runserver
Visit: http://127.0.0.1:8000/upload/
