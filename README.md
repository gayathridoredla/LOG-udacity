# Project 3: Log-Analysis Project
# By Doredla Gayathri

Log-Analysis Project

a). What it is and does??

A Reporting page that prints out reports in a plain text format based on the data in the database.This reporting tool is a python program using the `psycopg2` module to connect to the database.

b). Project content

This project consists for the following files are:

1) LAnysis_Ud.py - main file to run this Log Analysis Reporting tool
2) README.md - Instructions to install this reporting tool
3) newsdata.sql - database file
4) OutPut.JPG

c). Required Tools

1. Python
2. Vagrant
3. VirtualBox

d). Installation

There are some dependancies and a few instructions on how to run the application.

e). Dependencies

1. [Vagrant](https://www.vagrantup.com/)
2. [Udacity Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm)
3. [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

f). How to Install
1. Install Vagrant & VirtualBox
2. Clone the Udacity Vagrantfile
3. Go to Vagrant directory and either clone this repo or download and place zip here
3. Launch the Vagrant VM (`vagrant up`)
4. Log into Vagrant VM (`vagrant ssh`)
5. Navigate to `cd /vagrant` as instructed in terminal

g). How to Run Project

Download the project zip file to you computer and unzip the file then place inside `vagrant/log-analysis`.

  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:
  
  ---
    $ vagrant up
  ---
  2. Then Log into this using command:
  
  ---
    $ vagrant ssh
  ---
  3. download database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

  4. Unzip this file after downloading it. The file inside is called newsdata.sql.

  5. Copy the newsdata.sql file and place inside `vagrant/LAnysis_Ud.py`


  6. In terminal Change directory to `vagrant/LAnysis_Ud.py` and look around with ls.

  7. Load the data in local database using the command:

  ---
    $psql -d news -f views.sql
    $ psql -d news -f newsdata.sql
  ---
   8. Run newsdata.py using:
  ---
    $ python newsdata.py
  ---
    $python LAnysis_Ud.py
  Note: queries will take sometime to execute 


h). Miscellaneous

This README document is based on a template suggested by PhilipCoach. 