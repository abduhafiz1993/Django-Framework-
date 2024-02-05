# Wiki
### video <url https://www.youtube.com/watch?v=7oGnTbWOvrI>
# Django Encyclopedia Application Readme

This Django project implements an encyclopedia application where users can create, edit, and search for entries. Entries are written in markdown and displayed using the markdown2 library.

## Table of Contents
- [Introduction](#introduction)
- [Endpoints](#endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The encyclopedia application allows users to create new entries, edit existing entries, and search for entries. Entries are written in markdown format and rendered using the markdown2 library.

## Endpoints
1. **Index**: `/`
   - Displays a list of all available encyclopedia entries.

2. **Entry Details**: `/wiki/{entry}`
   - Displays the details of a specific entry, including the title and content rendered in markdown format.

3. **Search**: `/search`
   - Allows users to search for entries based on a query string.

4. **New Entry**: `/new`
   - Allows users to create a new entry by providing a title and content (markdown).

5. **Edit Entry**: `/edit/{entry}`
   - Allows users to edit an existing entry. Renders a form with the current title and content, which can be updated and saved.

6. **Random Entry**: `/random`
   - Redirects the user to a randomly selected entry.

## Usage
1. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```
2. **Access the Application** in your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

3. **View All Entries**:
    - Visit the index page at `/` to view a list of all available entries.

4. **View Entry Details**:
    - Click on the title of an entry on the index page to view its details at `/wiki/{entry}`.

5. **Search for Entries**:
    - Use the search bar or visit `/search?q={query}` to search for entries.

6. **Create a New Entry**:
    - Visit `/new` to create a new entry by providing a title and content (markdown).

7. **Edit an Entry**:
    - Click on the "Edit" button on an entry's detail page or visit `/edit/{entry}` to edit the title and content.

8. **View a Random Entry**:
    - Visit `/random` to be redirected to a randomly selected entry.

## Contributing
Feel free to contribute to this project. Fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
