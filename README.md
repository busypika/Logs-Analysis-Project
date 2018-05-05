# Logs Analysis Project

This is a project for Udacity's Full Stack Web Developer Nanodegree.

This project is about analyzing the database behind a newspaper site.
It's an internal reporting tool which use information from the database to analyze which article and which author is the most popular on the site.
And it even checks for connection error, too.

## Main Function

    1. What are the most popular three articles of all time? Which articles have been accessed the most?
    2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views?
    3. On which days did more than 1% of requests lead to errors?

### Expected Output

    Analyzing...

    The most popular 3 articles are:

    "Candidate is jerk, alleges rival" - 338647 views
    "Bears love berries, alleges bear" - 253801 views
    "Bad things gone, say good people" - 170098 views

    The most popular article authors are:

    "Ursula La Multa" - 507594 views
    "Rudolf von Treppenwitz" - 423457 views
    "Anonymous Contributor" - 170098 views
    "Markoff Chaney" - 84557 views

    Days did more than 1% of requests lead to errors are:

    2016-07-17:  2.26 %  errors

## Design
	I tried not to use "view" on this project to get more challenges.
	The whole design is simply "set a query to database, get results, print it out". To reach that, I've created a function to handle the method that set querys to database, since we don't need too complicated codes to do that and all questions above can be done by a simple, similar pattern.
	The only problem is to find out what query needs to be send, most important is every question should only have one query. And it turns out that subqueries can fix the problem, and I also use "join" on every question though they might not be so explicit.
	Since the hardest part has been solved, the only thing remained is simply to print those results out and that's it!

## Requirements

    The program is based on python 3, and PostgreSQL for the database. To ensure nothing goes wrong, a Virtual Machine might be needed. Python 3 and PostgreSQL will be both installed on the VM automatically.

    1. VM: Install Vagrant and VirtualBox.
        VirtualBox: https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
        Vagrant: https://www.vagrantup.com/downloads.html
    2. Terminal: If you're using windows, Git Bash is recommended.
        Git: https://git-scm.com/downloads
    3. Download the VM configuration.
        https://github.com/udacity/fullstack-nanodegree-vm
    4. Download the database.
        https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
    5. Download this project.
        https://github.com/busypika/Logs-Analysis-Project

### Start the Virtual Machine

    1. Inside the configuration, there is a directory names "vagrant".
    2. Open up your terminal and change directory into the folder.
    3. Run vagrant up.
    4. After all set, run vagrant ssh to log in.
	
	Notice: Everything inside /vagrant in VM will be shared with your local computer.

### Load database

    1. Put the database file into the "vagrant" folder.
    2. You'll find a newsdata.sql inside that database file, change directory to here.
    3. Run psql -d news -f newsdata.sql through your terminal.

## Run the Project

    1. To run this project, please put logs-analysis.py into the "vagrant" folder, too.
    2. You'll need two terminal at the same time, one for database and another for Python.
    3. First, make sure that database is running on one of your VM.
    4. Then, use another terminal, run python logs-analysis.py.
    5. That's it! Hope you've got the results!
