Outline of mymeet database(mymeet.db): 
[mymmet.db](https://github.com/jivaniyash/MyMeet-Database-Project/blob/main/database%20file/mymeet.db) is SQLite database file generated using [admin.py](https://github.com/jivaniyash/MyMeet-Database-Project/blob/main/python%20files/admin.py) 

Following are the details of database tables and its fields with data type.

user table
•	id INT
•	first_name VARCHAR
•	last_name VARCHAR
•	username VARCHAR
•	password VARCHAR

friend table
•	user_id INT
•	friend_id INT

note table
•	id INT
•	user_id INT
•	timestamp TIMESTAMP
•	title VARCHAR
•	text VARCHAR
•	visible_to VARCHAR

event table
•	id INT
•	note_id INT
•	timestamp TIMESTAMP
•	x-cordinate REAL
•	y-cordinate REAL
•	notification_range INT

comment table
•	id INT
•	note_id INT
•	commenter_id INT
•	timestamp TIMESTAMP
•	text VARCHAR


[results.sql](https://github.com/jivaniyash/MyMeet-Database-Project/blob/main/database%20file/results.sql) shows some sample queries and its description which can help analyst to run through the database for receiving important data for analysis.
