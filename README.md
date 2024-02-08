# Real Estate Management System

This is a Real Estate Management System built with Python and Django.

## Features

- **Admin User Login:**
  - Login with email and password.

- **Property Listing Module:**
  - Create property profiles with details like name, address, location, and features.
  - Each property can have multiple units with features like rent cost and type (1BHK, 2BHK, 3BHK, 4BHK).
  - Property profile view with units and assigned tenant information.

- **Tenant Management Module:**
  - Create tenant profiles with name, address, and document proofs.
  - Assign tenants to units under properties with details like agreement end date and monthly rent date.
  - Search based on unit and property features.
  - Show tenant profile view with personal and rental information.

## Code Structure

The project follows a standard Django structure:

- `property_management/`: Django app containing models, views, and templates.
- `templates/`: HTML templates for rendering views.
- `real_estate_management_system/`: Project settings and configuration.
