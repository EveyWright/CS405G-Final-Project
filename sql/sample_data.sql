

-- --------------------
-- Clubs
-- --------------------
INSERT IGNORE INTO Club (name) VALUES
('MathCounts'),
('Choir'),
('Robotics');

-- --------------------
-- Faculty
-- --------------------
INSERT IGNORE INTO Faculty (faculty_ID, name, title, dept, phone_number, email) VALUES
(1, 'Dr. Alan Smith', 'Teacher', 'Math', '859-555-1000', 'asmith@school.edu'),
(2, 'Ms. Laura Johnson', 'Teacher', 'Music', '859-555-2000', 'ljohnson@school.edu');

-- --------------------
-- Students
-- --------------------
INSERT IGNORE INTO Student (student_ID, name, grade, parent_number) VALUES
(101, 'Emily Brown', 7, '859-555-3000'),
(102, 'James Wilson', 8, '859-555-4000'),
(103, 'Sophia Miller', 6, '859-555-5000');

-- --------------------
-- Advisors per year
-- --------------------
INSERT IGNORE INTO Advises (club_name, faculty_ID, year) VALUES
('MathCounts', 1, 2025),
('Choir', 2, 2025),
('Robotics', 1, 2025);

-- --------------------
-- Memberships
-- --------------------
INSERT IGNORE INTO Member (club_name, student_ID, year) VALUES
('MathCounts', 101, 2025),
('MathCounts', 102, 2025),
('Choir', 103, 2025),
('Robotics', 101, 2025);

-- --------------------
-- Budgets
-- --------------------
INSERT IGNORE INTO Budget (club_name, year, total) VALUES
('MathCounts', 2025, 1500.00),
('Choir', 2025, 2000.00),
('Robotics', 2025, 3000.00);

-- --------------------
-- Expenses
-- --------------------
INSERT IGNORE INTO Expense (expense_ID, club_name, year, amount, memo) VALUES
(1, 'MathCounts', 2025, 200.00, 'Competition registration'),
(2, 'Choir', 2025, 350.00, 'Sheet music'),
(3, 'Robotics', 2025, 500.00, 'Electronic components');

-- --------------------
-- Events
-- --------------------
INSERT IGNORE INTO Event (event_ID, club_name, date, time, description) VALUES
(1001, 'MathCounts', '2025-04-10', '15:30:00', 'Weekly practice'),
(1002, 'Choir', '2025-04-12', '16:00:00', 'Choir rehearsal'),
(1003, 'Robotics', '2025-04-15', '15:45:00', 'Build session');

-- --------------------
-- Meetings
-- --------------------
INSERT IGNORE INTO Meeting (event_ID, classroom) VALUES
(1001, 'Room 201'),
(1002, 'Music Room'),
(1003, 'Lab A');

-- --------------------
-- Field Trips
-- --------------------
INSERT IGNORE INTO Field_Trip (event_ID, location) VALUES
(1002, 'City Auditorium');
