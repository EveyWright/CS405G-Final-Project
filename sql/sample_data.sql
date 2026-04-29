

-- --------------------
-- Clubs
-- --------------------
INSERT IGNORE INTO Club (name) VALUES
('MathCounts'),
('Choir'),
('Robotics'),
('Drama Club'),
('Art Club'),
('Band'),
('Chess Club'),
('Debate Team'),
('Science Club'),
('Photography Club'),
('Orchestra');


-- --------------------
-- Faculty
-- --------------------
INSERT IGNORE INTO Faculty (faculty_ID, name, title, dept, phone_number, email) VALUES
(1, 'Dr. Alan Smith', 'Teacher', 'Math', '859-555-1000', 'asmith@school.edu'),
(2, 'Ms. Laura Johnson', 'Teacher', 'Music', '859-555-2000', 'ljohnson@school.edu'),
(3, 'Mr. David Lee', 'Teacher', 'Science', '859-555-2500', 'dlee@school.edu'),
(4, 'Dr. Alan Smith', 'Teacher', 'Art', '859-555-3000', 'asmith2@school.edu'),
(5, 'Ms. Laura Johnson', 'Teacher', 'Music', '859-555-2000', 'ljohnson2@school.edu'),
(6, 'Mr. David Lee', 'Teacher', 'Science', '859-555-2500', 'dlee2@school.edu'),
(7, 'Dr. Alan Smith', 'Teacher', 'Math', '859-555-1000', 'asmith3@school.edu'),
(8, 'Dr. Alan Smith', 'Teacher', 'Art', '859-555-3000', 'asmith4@school.edu');
-- --------------------
-- Students
-- --------------------
INSERT IGNORE INTO Student (student_ID, name, grade, parent_number) VALUES
(101, 'Emily Brown', 7, '859-555-3000'),
(102, 'James Wilson', 8, '859-555-4000'),
(103, 'Sophia Miller', 6, '859-555-5000'),
(104, 'Michael Davis', 7, '859-555-6000'),
(105, 'Olivia Garcia', 8, '859-555-7000'),
(106, 'William Martinez', 6, '859-555-8000'),
(107, 'Ava Rodriguez', 7, '859-555-9000'),
(108, 'Ethan Hernandez', 8, '859-555-10000'),
(109, 'Isabella Lopez', 6, '859-555-11000'),
(110, 'Mason Gonzalez', 7, '859-555-12000'),
(111, 'Mia Perez', 8, '859-555-13000'),
(112, 'Logan Wilson', 6, '859-555-14000'),
(113, 'Charlotte Anderson', 7, '859-555-15000'),
(114, 'Lucas Thomas', 8, '859-555-16000'),
(115, 'Amelia Taylor', 6, '859-555-17000'),
(116, 'Benjamin Moore', 7, '859-555-18000'),
(117, 'Evelyn Jackson', 8, '859-555-19000'),
(118, 'Alexander White', 6, '859-555-20000'),
(119, 'Harper Harris', 7, '859-555-21000'),
(120, 'Daniel Martin', 8, '859-555-22000'),
(121, 'Ella Thompson', 6, '859-555-23000'),
(122, 'Matthew Garcia', 7, '859-555-24000'),
(123, 'Sofia Martinez', 8, '859-555-25000'),
(124, 'Joseph Robinson', 6, '859-555-26000'),
(125, 'Avery Clark', 7, '859-555-27000'),
(126, 'David Rodriguez', 8, '859-555-28000'),
(127, 'Madison Lewis', 6, '859-555-29000'),
(128, 'Samuel Lee', 7, '859-555-30000'),
(129, 'Abigail Walker', 8, '859-555-31000'),
(130, 'Christopher Hall', 6, '859-555-32000');

-- --------------------
-- Advisors per year
-- --------------------
INSERT IGNORE INTO Advises (club_name, faculty_ID, year) VALUES
('MathCounts', 1, 2025),
('Choir', 2, 2025),
('Chess Club', 3, 2025),
('Art Club', 4, 2025),
('Band', 5, 2025),
('Debate Team', 6, 2025),
('Science Club', 7, 2025),
('Photography Club', 8, 2025),
('Robotics', 1, 2025);

-- --------------------
-- Memberships
-- --------------------
INSERT IGNORE INTO Member (club_name, student_ID, year) VALUES
('MathCounts', 101, 2025),
('MathCounts', 102, 2025),
('Choir', 103, 2025),
('Choir', 104, 2025),
('Chess Club', 105, 2025),
('Chess Club', 106, 2025),
('Art Club', 107, 2025),
('Art Club', 108, 2025),
('Band', 109, 2025),
('Band', 110, 2025),
('Debate Team', 111, 2025),
('Debate Team', 112, 2025),
('Science Club', 113, 2025),
('Science Club', 114, 2025),
('Photography Club', 115, 2025),
('Photography Club', 116, 2025),
('Orchestra', 117, 2025),
('Orchestra', 118, 2025),
('Orchestra', 119, 2025),
('Robotics', 119, 2025),
('Robotics', 120, 2025),
('Robotics', 101, 2025);

-- --------------------
-- Budgets
-- --------------------
INSERT IGNORE INTO Budget (club_name, year, total) VALUES
('MathCounts', 2025, 1500.00),
('Choir', 2025, 2000.00),
('Chess Club', 2025, 1200.00),
('Art Club', 2025, 1800.00),
('Band', 2025, 2500.00),
('Debate Team', 2025, 1000.00),
('Science Club', 2025, 2200.00),
('Photography Club', 2025, 1600.00),
('Orchestra', 2025, 2000.00),
('Robotics', 2025, 3000.00);

-- --------------------
-- Expenses
-- --------------------
INSERT IGNORE INTO Expense (expense_ID, club_name, year, amount, memo) VALUES
(1, 'MathCounts', 2025, 200.00, 'Competition registration'),
(2, 'Choir', 2025, 350.00, 'Sheet music'),
(3, 'Chess Club', 2025, 150.00, 'Chess boards'),
(4, 'Art Club', 2025, 400.00, 'Art supplies'),
(5, 'Band', 2025, 500.00, 'Instruments'),
(6, 'Debate Team', 2025, 100.00, 'Research materials'),
(7, 'Science Club', 2025, 300.00, 'Lab equipment'),
(8, 'Photography Club', 2025, 250.00, 'Cameras and accessories'),
(9, 'Orchestra', 2025, 450.00, 'Sheet music and instruments'),
(10, 'Robotics', 2025, 500.00, 'Electronic components');

-- --------------------
-- Events
-- --------------------
INSERT IGNORE INTO Event (event_ID, club_name, date, time, description) VALUES
(1001, 'MathCounts', '2025-04-10', '15:30:00', 'Weekly practice'),
(0001, 'MathCounts', '2025-04-17', '15:30:00', 'Weekly practice'),
(0002, 'MathCounts', '2025-04-24', '15:30:00', 'Weekly practice'),
(0003, 'MathCounts', '2025-05-01', '15:30:00', 'Weekly practice'),
(0004, 'MathCounts', '2025-05-08', '15:30:00', 'Weekly practice'),
(0005, 'MathCounts', '2025-05-15', '15:30:00', 'Weekly practice'),
(0006, 'MathCounts', '2025-05-22', '15:30:00', 'Weekly practice'),
(0007, 'MathCounts', '2025-05-29', '15:30:00', 'Weekly practice'),
(0020, 'Choir', '2025-04-11', '16:00:00', 'Choir rehearsal'),
(0021, 'Choir', '2025-04-18', '16:00:00', 'Choir rehearsal'),
(0022, 'Choir', '2025-04-25', '16:00:00', 'Choir rehearsal'),
(0023, 'Choir', '2025-05-02', '16:00:00', 'Choir rehearsal'),
(0024, 'Choir', '2025-05-09', '16:00:00', 'Choir rehearsal'),
(0025, 'Choir', '2025-05-16', '16:00:00', 'Choir rehearsal'),
(0026, 'Choir', '2025-05-23', '16:00:00', 'Choir rehearsal'),
(0027, 'Choir', '2025-05-30', '16:00:00', 'Choir rehearsal'),
(1002, 'Choir', '2025-04-12', '16:00:00', 'Choir rehearsal'),
(1010, 'Choir', '2025-04-19', '16:00:00', 'Choir rehearsal'),
(1004, 'Choir', '2025-04-26', '16:00:00', 'Choir rehearsal'),
(1005, 'Choir', '2025-05-03', '16:00:00', 'Choir rehearsal'),
(1006, 'Choir', '2025-05-10', '16:00:00', 'Choir rehearsal'),
(1007, 'Choir', '2025-05-17', '16:00:00', 'Choir rehearsal'),
(1008, 'Choir', '2025-05-24', '16:00:00', 'Choir rehearsal'),
(1009, 'Choir', '2025-05-31', '16:00:00', 'Choir rehearsal'),
(1010, 'Choir', '2025-06-07', '16:00:00', 'Choir rehearsal'),
(9001, 'Orchestra', '2025-04-13', '17:00:00', 'Orchestra rehearsal'),
(9002, 'Orchestra', '2025-04-20', '17:00:00', 'Orchestra rehearsal'),
(9003, 'Orchestra', '2025-04-27', '17:00:00', 'Orchestra rehearsal'),
(9004, 'Orchestra', '2025-05-04', '17:00:00', 'Orchestra rehearsal'),
(9005, 'Orchestra', '2025-05-11', '17:00:00', 'Orchestra rehearsal'),
(9006, 'Orchestra', '2025-05-18', '17:00:00', 'Orchestra rehearsal'),
(9007, 'Orchestra', '2025-05-25', '17:00:00', 'Orchestra rehearsal'),
(9008, 'Orchestra', '2025-06-01', '17:00:00', 'Orchestra rehearsal'),
(9009, 'Orchestra', '2025-06-08', '17:00:00', 'Orchestra rehearsal'),
(2001, 'Chess Club', '2025-04-14', '17:00:00', 'Chess tournament'),
(2002, 'Chess Club', '2025-05-12', '17:00:00', 'Chess tournament'),
(2003, 'Chess Club', '2025-06-09', '17:00:00', 'Chess tournament'),
(3001, 'Art Club', '2025-04-16', '14:00:00', 'Painting workshop'),
(3002, 'Art Club', '2025-05-14', '14:00:00', 'Sculpture workshop'),
(3003, 'Art Club', '2025-06-11', '14:00:00', 'Photography workshop'),
(4001, 'Band', '2025-04-18', '18:00:00', 'Band practice'),
(4002, 'Band', '2025-05-16', '18:00:00', 'Band practice'),
(4003, 'Band', '2025-06-13', '18:00:00', 'Band practice'),
(5001, 'Debate Team', '2025-04-20', '19:00:00', 'Debate practice'),
(5002, 'Debate Team', '2025-05-18', '19:00:00', 'Debate practice'),
(5003, 'Debate Team', '2025-06-15', '19:00:00', 'Debate practice'),
(6001, 'Science Club', '2025-04-22', '15:00:00', 'Science experiment'),
(6002, 'Science Club', '2025-05-20', '15:00:00', 'Science experiment'),
(6003, 'Science Club', '2025-06-17', '15:00:00', 'Science experiment'),
(7001, 'Photography Club', '2025-04-24', '16:30:00', 'Photo walk'),
(7002, 'Photography Club', '2025-05-22', '16:30:00', 'Photo walk'),
(7003, 'Photography Club', '2025-06-19', '16:30:00', 'Photo walk'),
(1011, 'Robotics', '2025-04-15', '15:45:00', 'Build session');

-- --------------------
-- Meetings
-- --------------------
INSERT IGNORE INTO Meeting (event_ID, classroom) VALUES
(1001, 'Room 201'),
(1002, 'Music Room'),
(1003, 'Room 101'),
(0001, 'Room 201'),
(0002, 'Room 201'),
(0003, 'Room 201'),
(0004, 'Room 201'),
(0005, 'Room 201'),
(0006, 'Room 201'),
(0007, 'Room 201'),
(0020, 'Music Room'),
(0021, 'Music Room'),
(0022, 'Music Room'),
(0023, 'Music Room'),
(0024, 'Music Room'),
(0025, 'Music Room'),
(0026, 'Music Room'),
(0027, 'Music Room'),
(1002, 'Music Room'),
(1010, 'Music Room'),
(1004, 'Music Room'),
(1005, 'Music Room'),
(1006, 'Music Room'),
(1007, 'Music Room'),
(1008, 'Music Room'),
(1009, 'Music Room'),
(1010, 'Music Room'),
(3001, 'Room 102'),
(3002, 'Room 102'),
(3003, 'Room 102'),
(4001, 'Band Room'),
(4002, 'Band Room'),
(4003, 'Band Room'),
(5001, 'Room 103'),
(5002, 'Room 103'),
(6001, 'Science Lab'),
(6002, 'Science Lab'),
(7001, 'Photography Studio'),
(7002, 'Photography Studio'),
(7003, 'Photography Studio'),
(1011, 'Lab B'),
(9001, 'Music Room'),
(9002, 'Music Room'),
(9003, 'Music Room'),
(9004, 'Music Room'),
(9005, 'Music Room'),
(9006, 'Music Room'),
(9007, 'Music Room'),
(9008, 'Music Room'),
(9009, 'Music Room');

-- --------------------
-- Field Trips
-- --------------------
INSERT IGNORE INTO Field_Trip (event_ID, location) VALUES
(2001, 'City Library'),
(2002, 'Science Museum'),
(6003, 'Nature Reserve'),
(5003, 'State Capitol'),
(2003, 'Art Gallery'),
(9010, 'Symphony Hall');
