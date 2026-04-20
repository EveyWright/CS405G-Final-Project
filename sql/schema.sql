--CREATE DATABASE IF NOT EXISTS club_management;
--USE club_management;

CREATE TABLE IF NOT EXISTS Club (
    name VARCHAR(100),
    PRIMARY KEY (name)
);

CREATE TABLE IF NOT EXISTS Student (
    student_ID INT,
    name VARCHAR(100),
    grade INT,
    parent_number VARCHAR(20),
    PRIMARY KEY (student_ID)
);

CREATE TABLE IF NOT EXISTS Faculty (
    faculty_ID INT,
    name VARCHAR(100),
    title VARCHAR(50),
    dept VARCHAR(50),
    phone_number VARCHAR(20),
    email VARCHAR(100),
    PRIMARY KEY (faculty_ID)
);

CREATE TABLE IF NOT EXISTS Event (
    event_ID INT,
    club_name VARCHAR(100),
    date DATE,
    time TIME,
    description VARCHAR(255),
    PRIMARY KEY (event_ID),
    FOREIGN KEY (club_name) REFERENCES Club(name)
);

CREATE TABLE IF NOT EXISTS Meeting (
    event_ID INT,
    classroom VARCHAR(50),
    PRIMARY KEY (event_ID),
    FOREIGN KEY (event_ID) REFERENCES Event(event_ID)
);

CREATE TABLE IF NOT EXISTS Field_Trip (
    event_ID INT,
    location VARCHAR(100),
    PRIMARY KEY (event_ID),
    FOREIGN KEY (event_ID) REFERENCES Event(event_ID)
);

CREATE TABLE IF NOT EXISTS Budget (
    club_name VARCHAR(100),
    year INT,
    total DECIMAL(10,2),
    PRIMARY KEY (club_name, year),
    FOREIGN KEY (club_name) REFERENCES Club(name)
);

CREATE TABLE IF NOT EXISTS Expense (
    expense_ID INT,
    club_name VARCHAR(100),
    year INT,
    amount DECIMAL(10,2),
    memo VARCHAR(255),
    PRIMARY KEY (expense_ID),
    FOREIGN KEY (club_name, year) REFERENCES Budget(club_name, year)
);

CREATE TABLE IF NOT EXISTS Member (
    club_name VARCHAR(100),
    student_ID INT,
    year INT,
    PRIMARY KEY (club_name, student_ID, year),
    FOREIGN KEY (club_name) REFERENCES Club(name),
    FOREIGN KEY (student_ID) REFERENCES Student(student_ID)
);

CREATE TABLE IF NOT EXISTS Advises (
    club_name VARCHAR(100),
    faculty_ID INT,
    year INT,
    PRIMARY KEY (club_name, faculty_ID, year),
    FOREIGN KEY (club_name) REFERENCES Club(name),
    FOREIGN KEY (faculty_ID) REFERENCES Faculty(faculty_ID)
);
