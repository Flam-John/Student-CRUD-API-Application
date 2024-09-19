# Student-CRUD-API-Application
This project is a simple CRUD (Create, Read, Update, Delete) application for managing student records using Spring Boot and a REST API

<h1> Backend: </h1>
<h3>Spring Boot Application:</h3> Manages student data through a RESTful API with endpoints to create, retrieve, update, and delete student records.
<h3>Student Entity:</h3> Represents student data with attributes like id, firstName, lastName, email, and grade.
<h3>DAO Layer: </h3> Handles database interactions using JPA/Hibernate with methods for CRUD operations.
<h3>CommandLineRunner:</h3> Demonstrates CRUD operations by creating, updating, deleting, and querying student records.

<h1> Frontend (Python Script): </h1>
A Python script interacts with the REST API to fetch student data and analyze it.
<h3>Features:</h3> Identifies the student with the highest and lowest grades, calculates the average grade of all students, and displays the results.
<h3>Endpoints:</h3> GET /api/students: Retrieve all student records.

<h1>Setup:</h1> 
Run the Spring Boot application to start the server.
Execute the Python script to perform data analysis.
This project is ideal for learning and demonstrating basic CRUD operations with Spring Boot and RESTful services, and for performing data analysis with a Python client.

<h1>StudentRestController.java </h1>
<h3>Description:</h3> This file defines a REST controller for managing student data. It uses Spring Boot's @RestController and @RequestMapping annotations to handle HTTP requests. The /api/students endpoint is mapped to the findAll method, which retrieves a list of all students from the database using the StudentDAO.

<h1>StudentDAO.java </h1>
<h3>Description:</h3> This interface defines the Data Access Object (DAO) methods for managing Student entities. It includes methods for:

save(Student theStudent): Save a new student.
findById(Integer id): Retrieve a student by ID.
findAll(): Retrieve all students.
update(Student theStudent): Update an existing student.
delete(Integer id): Delete a student by ID.
Implementations of this interface handle the actual database operations.

<h1>StudentDAOImpl.java</h1>
<h3>Description:</h3> This class implements the StudentDAO interface using JPA/Hibernate. It provides concrete implementations for CRUD operations:

save(Student theStudent): Persists a new student entity.
findById(Integer id): Finds a student by ID.
findAll(): Retrieves all student records.
update(Student theStudent): Merges changes to an existing student entity.
delete(Integer id): Removes a student entity by ID.
Transactional annotations ensure database operations are managed correctly.

<h1>Student.java</h1>
<h3>Description:</h3> This class represents the Student entity mapped to the student table in the database. It includes fields for id, firstName, lastName, email, and grade, with appropriate JPA annotations for persistence. It also provides getters, setters, and a toString method for displaying student information.

<h1>CruddemoApplication.java</h1>
<h3>Description:</h3> The main entry point for the Spring Boot application. It contains the main method to run the application and a CommandLineRunner bean for executing CRUD operations at startup. It includes methods for:

Creating a new student.
Reading, updating, and deleting students.
Querying and displaying student data.
The file demonstrates how to interact with the StudentDAO in a Spring Boot environment.

<h1>student_analysis.py</h1>
<h3>Description:</h3> A Python script that interacts with the Spring Boot REST API to perform student data analysis. It:

Fetches student data from the /api/students endpoint.
Identifies the student with the highest and lowest grades.
Calculates and prints the average grade of all students.
This script demonstrates how to consume a RESTful API and perform data processing using Python.

<h1>student_tracker.sql</h1> 
<h3>Description:</h3>This SQL script is responsible for setting up the database and table structure for the Student CRUD application. 
<h3>It performs the following operations:</h3>

<h4>Database Creation:</h4>
Creates a database named student_tracker if it doesn't already exist.
Switches the context to the student_tracker database.

<h4>Table Creation:</h4>
Defines the structure for the student table, which stores student records.
<h3>Fields in the table include:</h3>
<h4>id:</h4> An auto-incrementing primary key.
<h4>first_name:</h4> A VARCHAR field for the student's first name.
<h4>last_name:</h4> A VARCHAR field for the student's last name.
<h4>email:</h4> A VARCHAR field for the student's email address.
<strong>grade:</strong> A DECIMAL(3,2) field for the student's grade, constrained to be between 0.00 and 10.00.

<h3>Table Constraints:</h3>
The id field is the primary key.
A CHECK constraint ensures that the grade value must be within the valid range of 0.00 to 10.00.
This script sets up the foundational database schema required for the Spring Boot application to perform CRUD operations on student data.
