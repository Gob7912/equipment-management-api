Equipment Management API
 About Project
This is a simple REST API built with Django and Django REST Framework.
The system helps manage equipment in a company.
You can:
add equipment
see equipment list
update it
delete it
assign equipment to a person
 What Problem It Solves
In companies it is hard to track:
who uses equipment
which equipment is free
which one is already assigned
This API solves this problem by storing everything in database and controlling assignment logic.
 Models
Equipment
name
serial_number (unique)
is_assigned (True/False)
created_at
Assignment
equipment (ForeignKey)
assigned_to
assigned_at
When equipment is assigned:
new Assignment is created
is_assigned becomes True
