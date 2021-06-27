### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

An object-relational database system.


- What is the difference between SQL and PostgreSQL?

SQL is a language used for communicating with a database.

- In `psql`, how do you connect to a database?

\l to list databases
\c "database" to connect

- What is the difference between `HAVING` and `WHERE`?

A where clause filters records from a result.  A having clause filters records from a group.


- What is the difference between an `INNER` and `OUTER` join?

An inner join finds and returns matching data from tables, an outer join finds matching data along with the data
that doesn't having any matching elements.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

A left outer join will return all the data from the left table and only the data from the right table that has a matching element.  A right outer join will return all the data from the right table and the data from the left table with matching elements.

- What is an ORM? What do they do?

Object relational mapping.  They transfer data from a database to an object, to be used in an application using an object-oriented programming language.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

  Ajax sends requests from the client side and the python module "requests" sends from the server side.  Ajax handles response code in the client's backround through javascript, so the page doesn't have to be re-rendered, "requests" uses the response to load a new page in the browser.

- What is CSRF? What is the purpose of the CSRF token?

Cross-site register forgery.  It is included in the http request from the server to the client, so when the client makes later requests, the token is used for validating those requests to the server, and rejecting the request if the token is missing or invalid.

- What is the purpose of `form.hidden_tag()`?

To generate a hidden field that includes a CSRF token.