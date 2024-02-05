# Django Mail Application Readme

### Video Demo <https://www.youtube.com/watch?v=xjvVpunw3Ig>

This Django project implements a simple mail application where users can send and receive emails.


## Table of Contents
- [Introduction](#introduction)
- [Endpoints](#endpoints)
- [Authentication](#authentication)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Introduction
The mail application provides functionality for users to compose, send, and view emails. Users can log in, check their inbox, send emails to other registered users, and manage their mailbox.


## Endpoints
1. **Inbox**: `/inbox`
   - Endpoint to view the user's inbox.

2. **Compose Email**: `/compose` (POST)
   - Compose and send a new email. Requires a POST request with the recipients, subject, and body.

3. **Mailbox**: `/mailbox/{mailbox}`
   - View emails based on the specified mailbox (`inbox`, `sent`, or `archive`).

4. **Email Detail**: `/email/{email_id}`
   - View details of a specific email. Supports GET and PUT requests for reading and archiving emails.

5. **Login**: `/login` (POST)
   - Log in to the application. Requires a POST request with the user's email and password.

6. **Logout**: `/logout`
   - Log out from the application.

7. **Register**: `/register` (POST)
   - Register a new user. Requires a POST request with a unique email address and matching password confirmation.


## Authentication
- Authentication is required for composing emails, viewing mailboxes, and email details.
- Use the `/login` endpoint to authenticate. After successful login, you can access other authenticated endpoints.
- Logout using the `/logout` endpoint.


## Usage
1. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```
2. **Access the Application** in your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

3. **Log In** using the provided login form.

4. **Compose Email**:
    - Use the `/compose` endpoint to send emails.

5. **View Inbox and Mailboxes**:
    - Access the `/inbox` and `/mailbox/{mailbox}` endpoints to view emails.

6. **View Email Details**:
    - Use the `/email/{email_id}` endpoint to view details of a specific email.


## Contributing
Feel free to contribute to this project. Fork the repository, make changes, and submit a pull request.


## License
This project is licensed under the [MIT License](LICENSE).

