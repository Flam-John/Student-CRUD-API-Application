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

<strong>save(Student theStudent):</strong> Save a new student.<br/> 
<strong>findById(Integer id):</strong> Retrieve a student by ID.<br/> 
<strong>findAll():</strong> Retrieve all students.<br/> 
<strong>update(Student theStudent):</strong> Update an existing student.<br/> 
<strong>delete(Integer id):</strong> Delete a student by ID.<br/> 
Implementations of this interface handle the actual database operations.<br/> 

<h1>StudentDAOImpl.java</h1>
<h3>Description:</h3> This class implements the StudentDAO interface using JPA/Hibernate. It provides concrete implementations for CRUD operations:

<strong>save(Student theStudent):</strong> Persists a new student entity.<br/> 
<strong>findById(Integer id):</strong> Finds a student by ID.<br/> 
<strong>findAll():</strong> Retrieves all student records.<br/> 
<strong>update(Student theStudent):</strong> Merges changes to an existing student entity.<br/> 
<strong>delete(Integer id):</strong> Removes a student entity by ID.<br/> 
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
<strong>It performs the following operations:</strong>

<h4>Table Creation:</h4>
Defines the structure for the student table, which stores student records.
<h3>Fields in the table include:</h3>
<strong>id:</strong> An auto-incrementing primary key.<br/> 
<strong>first_name:</strong> A VARCHAR field for the student's first name.<br/> 
<strong>last_name:</strong> A VARCHAR field for the student's last name.<br/> 
<strong>email:</strong> A VARCHAR field for the student's email address.<br/> 
<strong>grade:</strong> A DECIMAL(3,2) field for the student's grade, constrained to be between 0.00 and 10.00.<br/> 

<h3>Table Constraints:</h3>
The id field is the primary key.
A CHECK constraint ensures that the grade value must be within the valid range of 0.00 to 10.00.
This script sets up the foundational database schema required for the Spring Boot application to perform CRUD operations on student data.
