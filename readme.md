Creating backend for math practice problem application for elementary school students

Currently database has randomly generated data of 200 students, with 5 months of testing over 3 subjects

Python dependencies: sqlite3, names, numpy, pandas


To do:
    -Decide DB hosting logistics (DBMS, location, etc)
    -SQL queries or functions to return records of specific student, etc.
    -SQL queries or functions to produce data for different reports
        -Decide on what sort of reports we want
    -

General notes:
    -This is my first time building a back end or database from scratch. Nothing is set in stone and if there are better ways to do it, or norms I'm violating feel free to override anything I've done. (Tim) 
    -Using SqLite was the easiest way to get a DB up and running on a local machine. Usually production applications use something more heavy-duty. Thinking it'd be helpful (where possible) to try to make code agnostic about which framework is used so it's easy to move everything over when the time comes. (Tim)

Things to talk to Kevin about:

Database management
    -Storing class data...keep track of teacher, year, and students. What else?
    -Scoring/grading, what this will look like and/or what needs to be stored

UI
    -Dashboards - functionality and visualizations of interest


------ students.db -------

TABLE students 
    studentid integer
    email text
    first text
    last text
    dob text

TABLE classes 
    teacherid integer
    year integer
    studentid integer

TABLE scores 
    studentid integer
    metricid integer
    date integer
    score integer





