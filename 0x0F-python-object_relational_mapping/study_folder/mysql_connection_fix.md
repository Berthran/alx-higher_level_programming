The error message "Directory '/var/run/mysqld' for UNIX socket file doesn't exist" indicates that the directory where MySQL expects to place its socket file does not exist. This can happen if the directory was accidentally deleted or not created during installation.

Here are the steps to resolve this issue:

### 1. Create the Directory

Create the `/var/run/mysqld` directory and set the appropriate permissions:

```sh
sudo mkdir -p /var/run/mysqld
sudo chown mysql:mysql /var/run/mysqld
```

### 2. Start MySQL in Safe Mode

After creating the directory, you can start MySQL in safe mode:

```sh
sudo mysqld_safe --skip-grant-tables &
```

### 3. Connect to MySQL and Reset the Password

Now, you should be able to connect to the MySQL server without a password and reset the root password:

```sh
mysql -u root
```

Once connected, reset the password:

```sql
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
```

If `ALTER USER` doesn't work, try:

```sql
UPDATE mysql.user SET authentication_string=PASSWORD('new_password') WHERE User='root';
FLUSH PRIVILEGES;
```

### 4. Stop MySQL Safe Mode and Restart the MySQL Service

Exit the MySQL shell:

```sql
EXIT;
```

Stop the MySQL server running in safe mode:

```sh
sudo kill $(pgrep mysqld)
```

Restart the MySQL service:

```sh
sudo systemctl start mysql
```

### Verifying the Password Reset

After following these steps, log in to MySQL with the root user and the new password:

```sh
mysql -u root -p
```

Enter the new password when prompted.

### Additional Troubleshooting Steps

If you still encounter issues, consider these additional steps:

#### 1. Check MySQL Configuration

Ensure your MySQL configuration file (usually located at `/etc/mysql/my.cnf` or `/etc/mysql/mysql.conf.d/mysqld.cnf`) does not contain any incorrect settings related to the socket file.

#### 2. Check MySQL Logs

Check the MySQL error log for any specific errors that might provide more details on the issue. The log is typically located at `/var/log/mysql/error.log`.

#### 3. Reinstall MySQL

If the issue persists, you might need to reinstall MySQL:

```sh
sudo apt-get remove --purge mysql-server mysql-client mysql-common
sudo apt-get autoremove
sudo apt-get autoclean
sudo apt-get install mysql-server
```

This will remove MySQL and reinstall it, which can help resolve configuration issues.

By following these steps, you should be able to fix the issue and reset the MySQL root password successfully.
