The "Access denied" error when trying to log into MySQL with the root user usually indicates that the password is incorrect or that the root user does not have the necessary privileges. Here are the steps to reset the root password and resolve this issue:

### Steps to Reset the MySQL Root Password

#### 1. Stop the MySQL Service

First, you need to stop the MySQL service:

```sh
sudo systemctl stop mysql
```

#### 2. Start MySQL in Safe Mode

Start MySQL in safe mode to bypass the authentication system. This will allow you to connect to the MySQL server without a password:

```sh
sudo mysqld_safe --skip-grant-tables &
```

This command will run MySQL in the background without loading the privilege information, which effectively bypasses the normal password checks.

#### 3. Connect to MySQL

Now, you should be able to connect to the MySQL server without a password:

```sh
mysql -u root
```

#### 4. Reset the Root Password

Once connected, you can reset the root password using the following SQL commands. Replace `new_password` with the password you want to set:

```sql
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
```

If the `ALTER USER` command does not work, try the following:

```sql
UPDATE mysql.user SET authentication_string=PASSWORD('new_password') WHERE User='root';
FLUSH PRIVILEGES;
```

#### 5. Exit MySQL

Exit the MySQL shell:

```sql
EXIT;
```

#### 6. Stop MySQL Safe Mode

You need to stop the MySQL server running in safe mode:

```sh
sudo kill $(pgrep mysqld)
```

#### 7. Restart the MySQL Service

Finally, restart the MySQL service to apply the changes:

```sh
sudo systemctl start mysql
```

### Verifying the Password Reset

After following these steps, you should be able to log in to MySQL with the root user and the new password:

```sh
mysql -u root -p
```

Enter the new password when prompted.

### Troubleshooting

If you still encounter issues, consider the following additional steps:

- **Check MySQL Version:**
  Ensure you are using the correct commands for your version of MySQL.

- **Check MySQL Configuration:**
  Verify the MySQL configuration file (`/etc/mysql/my.cnf` or `/etc/mysql/mysql.conf.d/mysqld.cnf`) for any settings that might affect authentication.

- **MySQL Logs:**
  Check the MySQL error log for any specific errors that might provide more details on the issue. The log is typically located at `/var/log/mysql/error.log`.

By following these steps, you should be able to reset the MySQL root password and resolve the "Access denied" error.
