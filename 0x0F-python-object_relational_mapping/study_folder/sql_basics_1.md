To view the list of databases and then specifically view the contents of a particular database in MySQL, you can follow these steps:

### Viewing the List of Databases

1. **Connect to MySQL Server:**
   Open your MySQL command-line client or MySQL workbench and connect to the MySQL server where your databases are hosted. Use the appropriate credentials (username and password).

2. **List Databases:**
   To view the list of all databases on the MySQL server, use the following command:

   ```sql
   SHOW DATABASES;
   ```

   This command will display a list of databases available on the MySQL server.

### Viewing the Contents of a Specific Database

Once you have identified the database you want to view:

1. **Use the Database:**
   To switch to a specific database and begin working within it, use the `USE` statement followed by the name of the database:

   ```sql
   USE database_name;
   ```

   Replace `database_name` with the name of the database you want to view.

2. **List Tables:**
   After switching to the desired database, you can list all the tables within that database using:

   ```sql
   SHOW TABLES;
   ```

   This command will display a list of tables present in the selected database.

3. **View Table Structure:**
   To view the structure (columns and their types) of a specific table within the database, you can use:

   ```sql
   DESCRIBE table_name;
   ```

   Replace `table_name` with the name of the table you want to examine. This command will show you the details about the columns and their data types in the specified table.

4. **Query Data:**
   To retrieve data from a table, you can use a `SELECT` statement:

   ```sql
   SELECT * FROM table_name;
   ```

   Replace `table_name` with the name of the table from which you want to fetch data. This query will return all rows and columns from the specified table.

### Example

Assuming you have a database named `my_bd` and a table named `states` (as created in the previous example):

```sql
USE my_bd;  -- Switch to the 'my_bd' database

SHOW TABLES;  -- Display all tables in the 'my_bd' database

DESCRIBE states;  -- View the structure of the 'states' table

SELECT * FROM states;  -- Retrieve all data from the 'states' table
```

By following these steps, you can view the contents of a specific database and interact with its tables as needed using MySQL commands. Adjust the database and table names according to your own setup.
