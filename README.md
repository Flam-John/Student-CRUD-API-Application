# Student-CRUD-API-Application
This project is a simple CRUD (Create, Read, Update, Delete) application for managing student records using Spring Boot and a REST API

<h1> Backend: </h1>
Spring Boot Application: Manages student data through a RESTful API with endpoints to create, retrieve, update, and delete student records.
Student Entity: Represents student data with attributes like id, firstName, lastName, email, and grade.
DAO Layer: Handles database interactions using JPA/Hibernate with methods for CRUD operations.
CommandLineRunner: Demonstrates CRUD operations by creating, updating, deleting, and querying student records.

Frontend (Python Script):
A Python script interacts with the REST API to fetch student data and analyze it.
Features: Identifies the student with the highest and lowest grades, calculates the average grade of all students, and displays the results.
Endpoints:

GET /api/students: Retrieve all student records.

Setup:
Run the Spring Boot application to start the server.
Execute the Python script to perform data analysis.
This project is ideal for learning and demonstrating basic CRUD operations with Spring Boot and RESTful services, and for performing data analysis with a Python client.

StudentRestController.java
Description: This file defines a REST controller for managing student data. It uses Spring Boot's @RestController and @RequestMapping annotations to handle HTTP requests. The /api/students endpoint is mapped to the findAll method, which retrieves a list of all students from the database using the StudentDAO.

StudentDAO.java
Description: This interface defines the Data Access Object (DAO) methods for managing Student entities. It includes methods for:

save(Student theStudent): Save a new student.
findById(Integer id): Retrieve a student by ID.
findAll(): Retrieve all students.
update(Student theStudent): Update an existing student.
delete(Integer id): Delete a student by ID.
Implementations of this interface handle the actual database operations.

StudentDAOImpl.java
Description: This class implements the StudentDAO interface using JPA/Hibernate. It provides concrete implementations for CRUD operations:

save(Student theStudent): Persists a new student entity.
findById(Integer id): Finds a student by ID.
findAll(): Retrieves all student records.
update(Student theStudent): Merges changes to an existing student entity.
delete(Integer id): Removes a student entity by ID.
Transactional annotations ensure database operations are managed correctly.

Student.java
Description: This class represents the Student entity mapped to the student table in the database. It includes fields for id, firstName, lastName, email, and grade, with appropriate JPA annotations for persistence. It also provides getters, setters, and a toString method for displaying student information.

CruddemoApplication.java
Description: The main entry point for the Spring Boot application. It contains the main method to run the application and a CommandLineRunner bean for executing CRUD operations at startup. It includes methods for:

Creating a new student.
Reading, updating, and deleting students.
Querying and displaying student data.
The file demonstrates how to interact with the StudentDAO in a Spring Boot environment.

student_analysis.py
Description: A Python script that interacts with the Spring Boot REST API to perform student data analysis. It:

Fetches student data from the /api/students endpoint.
Identifies the student with the highest and lowest grades.
Calculates and prints the average grade of all students.
This script demonstrates how to consume a RESTful API and perform data processing using Python.
