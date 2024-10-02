# HR Management System

## Project Overview

This project is a basic HRMS (Human Resource Management System) implemented using Django. It includes functionalities such as employee management, attendance tracking, and basic reporting.

## Project Structure

The project is organized as follows:

- `hrmsapp`: Django application containing models, views, serializers, and other related components.
- `manage.py`: Django management script.
- `HRmanagement`: Project settings and configuration.
- Other Django-related files and directories.

## Getting Started

Follow the steps below to run the app locally:

1. **Clone the Repository:**

   git clone https://github.com/Nikunj6265/Human-Resource-Management-System

   
2. **Navigate to the Project Directory:**
  cd HRmanagement
  Install Dependencies:
  pip install -r requirements.txt


3. **Apply Migrations:**
  python manage.py migrate


4. **Run the Development Server:**
  python manage.py runserver
  Access the App:
  Open your web browser and go to http://127.0.0.1:8000/ to access the home page.


## Usage
Home Page: Lists all employees.
Add Employee: Access the /newemployee/ endpoint to add a new employee.
Attendance: Access the /attendence/ endpoint to mark attendance for an employee.
Report: Access the /report/ endpoint to view a report on the number of employees in each department.

## Additional Information
The project uses Django REST Framework for building APIs.
Ensure that you have Python and Django installed on your system.
The database is configured to use MySQL. Update the DATABASES settings in settings.py accordingly.
