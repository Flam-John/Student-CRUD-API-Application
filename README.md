# Student-CRUD-API-Application
This project is a simple CRUD (Create, Read, Update, Delete) application for managing student records using Spring Boot and a REST API

Backend:

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
