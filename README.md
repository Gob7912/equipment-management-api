 Equipment Management API
 Project Description

This project is a REST API built with Django and Django REST Framework.

The system is used to manage equipment in a company or organization.

It allows:

Creating equipment

Viewing equipment list

Updating equipment

Deleting equipment

Assigning equipment to a person

What Problem Does This Project Solve?

In many companies it is difficult to track:

Which equipment exists

Who is using equipment

Which equipment is available

Which equipment is already assigned

This API solves this problem by storing all equipment in a database and controlling assignment logic.

 Models
1 Equipment

Fields:

name

serial_number (unique)

is_assigned (True / False)

created_at

2 Assignment

Fields:

equipment (ForeignKey to Equipment)

assigned_to

assigned_at

When equipment is assigned:

A new Assignment is created

is_assigned becomes True

Equipment cannot be assigned twice
