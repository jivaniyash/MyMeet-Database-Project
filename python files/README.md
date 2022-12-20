[raw_file.txt](https://github.com/jivaniyash/MyMeet-Database-Project/blob/main/python%20files/raw_file.txt) is a sample file containing list of first_name & last_name of users (source: [http://random-name-generator.info/](http://random-name-generator.info/))



[data_generate.py](https://github.com/jivaniyash/MyMeet-Database-Project/blob/main/python%20files/data_generate.py) is a python file to generate data for [mymeet.db](https://github.com/jivaniyash/MyMeet-Database-Project/blob/main/database%20file/mymeet.db) using random module. It has SQLTableValues class which has methods for building data in particular format in the form of dictonary object (key-value pairs). 

[admin.py](https://github.com/jivaniyash/MyMeet-Database-Project/blob/main/python%20files/admin.py) inherits SQLTableValues from [data_generate.py](https://github.com/jivaniyash/MyMeet-Database-Project/blob/main/python%20files/data_generate.py) into SQL class. Also SQL class uses sqlite3 module for creating connection and cursor object for linking of python with [mymeet database](https://github.com/jivaniyash/MyMeet-Database-Project/blob/main/database%20file/mymeet.db).


main() function in [admin.py](https://github.com/jivaniyash/MyMeet-Database-Project/blob/main/python%20files/admin.py) calls different methods to create tables and insert values in [database file](https://github.com/jivaniyash/MyMeet-Database-Project/blob/main/database%20file/mymeet.db)


