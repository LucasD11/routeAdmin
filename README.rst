Environment Setup
=================

1. Create database and database user

.. code:: SQL

   create USER router WITH PASSWORD '******';
   CREATE DATABASE router;
   ALTER ROLE router SET client_encoding TO 'utf8';
   ALTER ROLE router SET default_transaction_isolation TO 'read committed';
   ALTER ROLE router SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE router to router;

2. Create virtual environment and install requirements.
