To add entries into a table in MySQL, you use the `INSERT INTO` statement. This statement allows you to insert new rows into a table. Here's how to do it, including examples for different scenarios.

### Basic Syntax

```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```

### Examples

1. **Inserting a Single Row:**

   Suppose you have a table `employees` with columns `id`, `name`, and `position`. To insert a single row:

   ```sql
   INSERT INTO employees (id, name, position)
   VALUES (1, 'John Doe', 'Software Engineer');
   ```

2. **Inserting Multiple Rows:**

   You can insert multiple rows in a single `INSERT INTO` statement:

   ```sql
   INSERT INTO employees (id, name, position)
   VALUES 
     (2, 'Jane Smith', 'Project Manager'),
     (3, 'Emily Davis', 'Data Analyst');
   ```

3. **Inserting Data Without Specifying Columns:**

   If you are inserting values for all columns in the order they are defined in the table, you can omit the column names:

   ```sql
   INSERT INTO employees
   VALUES (4, 'Michael Brown', 'UX Designer');
   ```

   Note: The number and order of values must match the columns defined in the table.

4. **Inserting Data Using a Subquery:**

   You can also insert data into a table based on the results of a `SELECT` query:

   ```sql
   INSERT INTO new_employees (id, name, position)
   SELECT id, name, position
   FROM employees
   WHERE position = 'Software Engineer';
   ```

### Example with a Table Creation

Here’s an end-to-end example, including table creation and insertion:

1. **Create the Table:**

   ```sql
   CREATE TABLE employees (
     id INT PRIMARY KEY,
     name VARCHAR(100),
     position VARCHAR(50)
   );
   ```

2. **Insert Single Row:**

   ```sql
   INSERT INTO employees (id, name, position)
   VALUES (1, 'John Doe', 'Software Engineer');
   ```

3. **Insert Multiple Rows:**

   ```sql
   INSERT INTO employees (id, name, position)
   VALUES 
     (2, 'Jane Smith', 'Project Manager'),
     (3, 'Emily Davis', 'Data Analyst');
   ```

4. **Insert Data Using a Subquery:**

   ```sql
   INSERT INTO employees_archive (id, name, position)
   SELECT id, name, position
   FROM employees
   WHERE position = 'Software Engineer';
   ```

### Special Considerations

- **Auto-Increment Columns:**
  If your table has an `AUTO_INCREMENT` column (often used for primary keys), you can omit it in the `INSERT` statement:

  ```sql
  INSERT INTO employees (name, position)
  VALUES ('Sarah Johnson', 'Marketing Manager');
  ```

- **Default Values:**
  If columns have default values and you don’t provide values for them in your `INSERT` statement, MySQL will use the default values.

- **Handling NULL Values:**
  To insert `NULL` values explicitly, you can use `NULL` in place of a value:

  ```sql
  INSERT INTO employees (id, name, position)
  VALUES (5, 'Unknown', NULL);
  ```

These examples should cover most common use cases for inserting data into MySQL tables.
