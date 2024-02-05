# Django Auction Project Readme

This Django project implements an online auction system. Users can register, log in, create auction listings, place bids, add items to their watchlist, and view auction details.

## Table of Contents
- [Getting Started](#getting-started)
- [Features](#features)
- [File Structure](#file-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started
1. **Install Python**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Django**: Use the following command to install Django.
    ```bash
    pip install django
    ```

3. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/django-auction-project.git
    ```

4. **Navigate to the Project Directory**:
    ```bash
    cd django-auction-project
    ```

5. **Apply Database Migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a Superuser** (Admin) for the Django Admin Panel:
    ```bash
    python manage.py createsuperuser
    ```

7. **Start the Development Server**:
    ```bash
    python manage.py runserver
    ```

8. **Open your Browser** and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the application.

## Features
1. **User Authentication**: Users can register, log in, and log out.

2. **Create Auction Listings**: Authenticated users can create auction listings, providing details such as item name, description, starting price, and category.

3. **Place Bids**: Users can place bids on active auction listings. The highest bid is displayed, and the auction winner is determined when the auction ends.

4. **Watchlist**: Users can add and remove listings from their watchlist, making it easy to track favorite items.

5. **View Listings by Category**: Listings can be filtered based on categories, allowing users to explore items in specific categories.

6. **Comments**: Users can add comments to auction listings to share thoughts or ask questions.

7. **User Profile**: Each user has a profile that includes a watchlist and additional information.

8. **Responsive Design**: The application is designed to work well on different screen sizes.

## File Structure
- `auctions/`: Django app containing models, views, and templates.
- `static/`: Contains static files like CSS stylesheets and images.
- `templates/`: HTML templates for rendering views.
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django management script.
- `README.md`: Project documentation.

## Usage
- **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```
- **Access the Application** in your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
- **Log in** with the superuser account created during setup to access the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Contributing
Feel free to contribute to this project. Fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
