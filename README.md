# HCPSMSHS Alumni Database Management System (DBMS)

## Overview
The HCPSMSHS Alumni Database Management System (DBMS) is a comprehensive solution developed for Honorato C. Perez, Sr. Memorial Science High School (HCPSMSHS) to effectively manage and organize alumni records. This project addresses challenges in accessing, maintaining, and utilizing alumni data, providing a user-friendly and efficient platform for data collection, storage, retrieval, and analysis.

## Features
The system offers several key features to ensure efficient management of alumni records:

1. **User Authentication**: 
    - Implements user authentication using Django's built-in authentication framework.
    - Users can register, log in, and log out of the system.
    - Specific actions require authentication, such as adding, updating, or deleting records.

2. **Record Management**:
    - Allows users to manage alumni records with details such as name, sex, strand, graduation year, college/university, college course, and HEI (public or private).

3. **Record Filtering**:
    - Provides filtering functionality using Django's Django-filter library.
    - Users can filter records based on sex, strand, graduation year, college/university, and college course.

4. **Record CRUD Operations**:
    - Users can perform Create, Read, Update, Delete (CRUD) operations on alumni records.
    - Features include adding new records, viewing individual records, updating existing records, and deleting records from the database.

5. **File Export**:
    - Includes a feature to export alumni records as a CSV (Comma-Separated Values) file.
    - Users can download a CSV file containing selected fields from the alumni records for data analysis or other purposes.

6. **User Interface**:
    - Various HTML templates provide a user-friendly interface for interacting with the database.
    - Templates include pages for displaying, adding, updating, and viewing individual record details, as well as a homepage, team page, and login/logout feature.

7. **Security**:
    - Incorporates security measures such as user authentication, password validation, and protection against clickjacking attacks.
    - Uses the Django Defender library to add additional security features, such as protection against brute-force login attempts.

8. **Database Integration**:
    - Integrated with a MySQL database, with configuration options including database name, username, password, host, and port.

9. **Admin Interface Customization**:
    - Utilizes the Jazzmin package to enhance the default Django admin interface.
    - Customization options include setting the site header, site title, welcome text, and copyright information.

## Final Design
The HCPSMSHS Alumni DBMS features a clean and intuitive user interface, ensuring ease of navigation and efficient interaction with the system. The design incorporates a responsive layout, allowing seamless access from various devices, including desktop computers, laptops, tablets, and mobile phones.

## Manuscript Link
For a detailed explanation of the project, please refer to the [manuscript](https://drive.google.com/file/d/1bWef4MLA3wHgzF-3KGB-W-nacqRxFJww/view).

---
