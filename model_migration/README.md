# SQL

## Databases
Before we get into how to use the SQL language, we should discuss how our data is stored. When using SQL, we’ll work with a relational database where we can find all of our data stored in a number of tables. Each of these tables is made up of a set number of columns and a flexible number of rows.

There are several different relational database management systems that are commonly used to store information, and that can easily interact with SQL commands:

- MySQL
- PostgreSQL
- SQLite
…
The first two, MySQL and PostgreSQL, are heavier-duty database management systems that are typically run on servers separate from those running a website. SQLite, on the other hand, is a lighter-weight system that can store all of its data in a single file. We’ll be using SQLite throughout this course, as it is the default system used by Django


## Column Types

Just as we worked with several different variable types in Python, SQLite has types that represent different forms of information. Other management systems may have different data types, but all are fairly similar to those of SQLite:

- TEXT: For strings of text (Ex. a person’s name)
- NUMERIC: A more general form of numeric data (Ex. A date or boolean value)
- INTEGER: Any non-decimal number (Ex. a person’s age)
- REAL: Any real number (Ex. a person’s weight)
-BLOB (Binary Large Object): Any other binary data that we may want to store in our database (Ex. an image)

## Tables
Now, to actually get started with using SQL to interact with a database, let’s begin by creating a new table. The command to create a new table looks something like this:


    ```bash
    CREATE TABLE flights(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        origin TEXT NOT NULL,
        destination TEXT NOT NULL,
        duration INTEGER NOT NULL
    );

In the above command, we’re creating a new table that we’ve decided to call flights, and we’ve added four columns to this table:

id: It is often helpful to have an number that allows us to uniquely identify each row in a table. Here we have specified that id is an integer, and also that it is our primary key, meaning it is our unique identifier. We have additionally specified that it will AUTOINCREMENT, which means we will not have to provide an id every time we add to the table because it will be done automatically.
origin: Here we’ve specified that this will be a text field, and by writing NOT NULL we have required that it have a value.
destination: Again we’ve specified that this will be a text field and prevented it from being null.
duration: Again this value cannot be null, but this time it is represented by an integer rather than as text.
We just saw the NOT NULL and PRIMARY KEY constraint when making a column, but there are several other constraints available to us:

- CHECK: Makes sure certain constraints are met before allowing a row to be added/modified
- DEFAULT: Provides a default value if no value is given
- NOT NULL: Makes sure a value is provided
- PRIMARY KEY: Indicates this is the primary way of searching for a row in the database
- UNIQUE: Ensures that no two rows have the same value in that column.
…

example:

    ```bash
    CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT,
    gender VARCHAR(10),
    grade INT CHECK (grade BETWEEN 1 AND 12),
    email VARCHAR(100) UNIQUE,
    registration_date DATE DEFAULT CURRENT_DATE
    );
    ```

## Functions

There are also a number of SQL functions we can apply to the results of a query. These can be useful if we don’t need all of the data returned by a query, but just some summary statistics of the data.

AVERAGE
COUNT
MAX
MIN
SUM
…

example 

    ```bash
    SELECT AVG(salary) AS average_salary,
       COUNT(*) AS total_employees,
       MAX(age) AS max_age,
       MIN(age) AS min_age,
       SUM(sales) AS total_sales
    FROM employees;
    ```
## UPDATE

We’ve now seen how to add to and search tables, but we may also want to be able update rows of a table that already exist. We do this using the UPDATE command as shown below. As you may have guessed by reading this out loud, the command finds any flights that go from New York to London, and then sets their durations to 430
