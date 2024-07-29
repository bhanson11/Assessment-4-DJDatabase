### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  - PostgreSQL is an open-source relational database management system (RDBMS). See differences from SQL below 
  - Relational database is a tyep of database that stores and gives access to data points that are related to one another. Quicker and more efficient than DBMS which is just set up in files. More efficient because of the relationships data points have with one another.

- What is the difference between SQL and PostgreSQL?
  - PostgreSQL is open-source and free 
  - SQL is only for Windows (owned by Microsoft) and psql is on Linux, macOS, and Windows
  - SQL supports JS, PHP and C# / PSQL supports Pthon, Tcl, Net, C, C++, Delphi, Java, JS (Node.js), and Perl

- In `psql`, how do you connect to a database?
  - Connecting to a database you use: "\c DATABASE_NAME if it is local - which is the only way I've done it

- What is the difference between `HAVING` and `WHERE`?
  - WHERE decides which rows to use 
  - HAVING determines which grouped results to keep 

- What is the difference between an `INNER` and `OUTER` join?
  - INNER joins only the rows that match the condition in both tables
  - OUTER includes left, right, and full joins and are helpful when trying to find rows in one table with no match in another table
  - FULL join is just joining both tables completely side by side or all the rows from both tables (left and right)

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  - LEFT joins all of the rows from the first table (left), combined with matching rows from the second table (right) 
  - RIGHT - the matching rows from the first table (left), combined with all the rows from the second table (right)

- What is an ORM? What do they do?
  - ORM = Object-relational mapping. ORM is a programming technique that acts as a bridge between OOP languages and RDBMS like PSQL
  - SQLAlchemy and Django are two examples of such systems that help with this

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

- What is CSRF? What is the purpose of the CSRF token?
  - CSRF or "Cross-Site Request Forgery" is an attack that forces an end user to make actions in a web app where they are currently authenticated. The attackers will trick the user by having certain actions on the website link to other websites that the attackers control and then can get information from the that they want such as money, email address, other sensitive info. 
  - The CSRF token is a safety net against such attacks. It is a unique security measure designed to protect web apss from these malicious requests 

- What is the purpose of `form.hidden_tag()`?
  - This is used by Flask-WTF to implement CSRF protection 