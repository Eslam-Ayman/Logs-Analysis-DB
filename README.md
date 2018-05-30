# Documentation of Logs Analysis (DB)
## About
this project has made for testing skills of `structured query language (SQL)` .
this project analyses DB called `news`

## To Run
### You will need:
- Python3
- PostgreSQL DB
- psycopg2 Module

## Setup
 1. Install python
    - https://www.python.org/downloads/
 2. Download flask Module
    - `pip install flask```
 3. Download PostgreSQL DB
    - https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
 4. Download psycopg2 Module (DB-API)
    - ```pip install  psycopg2```
 5. Download data from here
    - [News Database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

### To Run
to be able using `psql` command through your terminal on linux or git bash on windows
you need to add those two paths to `$PATH` environment variable
`%APPDATA%/PostgreSQL/bin` & `%APPDATA%/PostgreSQL/lib` <br>
`%APPDATA%` it is mean your installition path

download database and change your directory to the same file path 
and import it in your DBMS by using this command
`psql -d news -f newsdata.sql`

to run the project code use this command
`python newsSourceCode.py`

## Program's Output
![N|Solid](https://preview.ibb.co/mXQrv7/image.png)

# License 
this project is free to every one who is starting to learn python
> Author : Eslam Ayman 
