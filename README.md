# Project Title

Projeto Extensionista: Intranet and Communication System

# Project Name

Projeto Extensionista

## Description

Projeto Extensionista is an intranet solution designed for companies looking to keep their employees informed about the latest updates, regulations, courses, and internal events. The system allows administrators to post news and announcements in a dedicated administrative area, accessible only by authorized users. This ensures that employees can easily access these updates and stay informed about what’s happening within the company. The project also includes an authentication system, ensuring secure and controlled access.

## Objective

The goal of this project is to provide a centralized platform for company-wide communication. Through this intranet, employees can stay informed about new regulations, events, courses, and company updates in an organized and secure environment.

## History

This project arose from the need of a company that lacked an intranet system to communicate efficiently with employees. The objective was to provide a simple and effective solution to bridge this gap, keeping the workforce well-informed and engaged with internal happenings.

## Technologies Used

This project was built using the following technologies:

- **[Python 12](https://www.python.org/)**: Programming language used for the backend.
- **[Django 5.0](https://www.djangoproject.com/)**: Python web framework that facilitates rapid and secure web application development.
- **[HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML/HTML5)**: Structure of the user interface.
- **[CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)**: Styling of the user interface.
- **[Bootstrap 5.0](https://getbootstrap.com/)**: CSS framework for responsive design and UI components.
- **[SQL Server](https://www.microsoft.com/en-us/sql-server)**: Primary database for storing company information.
- **[SQLite](https://www.sqlite.org/)**: Database used for testing.
- **[Git](https://git-scm.com/)**: Version control for source code management.


## Screens

| Project                                                                                      | 
|----------------------------------------------------------------------------------------------------
| ![projeto-extensionista](https://github.com/user-attachments/assets/da27ce3c-e826-43d6-95ef-45e2147cea92) |
 

&nbsp;


##  Click here for project run.

<a href="https://youtu.be/ciQP65GGL8s">Youtube</a>

## How to Run the Project

1. Clone the repository:
    ```bash
    https://github.com/kemuelkesley/projeto-extensionista-faculdade.git
    ```

2. Navigate to the project directory:
    ```bash
    cd projeto-extensionista-faculdade
    ```

3. Create and activate a virtual environment:
    ```bash
    Create a virtual environment:

    python -m venv venv

    Activate the virtual environment
    
    # On Linux use `source venv/bin/activate`  # On Windows use `venv\Scripts\activate`
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Apply the database migrations:
    ```bash
    1 - python manage.py migrate  
    ```

7. Create a user to access the admin area:
    ```bash
    1 - python manage.py createsuperuser
    2 - Create the username
    3 - Optionally create an email
    4 - Create your password
    5 - Confirm at the end
    6 - To access the admin area, go to http://127.0.0.1:8000/admin/
    7 - Enter the created username and password.
    ```

8. Start the development server:
    ```bash
    python manage.py runserver

    Address:

    http://127.0.0.1:8000/
    ```

## Contribution

Contributions are welcome! If you have suggestions, issues, or pull requests, feel free to collaborate.

## License

This project is licensed under [kemSoftware].
