CREATE DATABASE computer_lab_assistant;
USE computer_lab_assistant;

//1- Users Table
//Stores info about every user (students, staff, faculty).


CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    role ENUM('student', 'faculty', 'staff') NOT NULL,
    password_hash VARCHAR(255) NOT NULL,  -- for login (store hashed passwords)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
//2. FAQs Table
//Stores common troubleshooting questions and answers(the assistant can search or display these).
CREATE TABLE faqs (
    faq_id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(100) NOT NULL,  -- e.g. "Wi-Fi", "CUNYfirst", "outlook", "MFA",
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
//Example entries:
INSERT INTO faqs (category, question, answer) VALUES
('Wi-Fi', 
 'How do I connect to BC Wi-Fi?', 
 'Select “BC WiFi” network, then sign in using your CUNY Login credentials.'),

('Outlook', 
 'How do I reset my Outlook email password?', 
 'Visit outlook.office.com, click “Forgot password,” and follow the password reset steps using your CUNY Login.'),

('CUNYfirst', 
 'Why can’t I log into CUNYfirst?', 
 'Make sure you are using your correct CUNY Login credentials and that your MFA (Multi-Factor Authentication) is properly configured.'),

('MFA', 
 'How do I set up Multi-Factor Authentication (MFA) for my CUNY account?', 
 'Go to the CUNY MFA setup page, log in with your CUNY credentials, and follow the instructions to register your authentication method (phone or app).'),

('MFA', 
 'I changed my phone. How do I update my MFA settings?', 
 'Visit the CUNY MFA management page, remove your old device, and re-register your new phone for authentication.');

