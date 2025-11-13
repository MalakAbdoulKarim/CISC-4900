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
//2
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

//Stores custom questions that users ask when they don’t find an answer in the FAQ
CREATE TABLE user_questions (
    question_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    question_text TEXT NOT NULL,
    asked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

//Stores the assistant’s or technician’s response to user questions.
CREATE TABLE responses (
    response_id INT AUTO_INCREMENT PRIMARY KEY,
    question_id INT NOT NULL,
    responder_type ENUM('assistant', 'technician') DEFAULT 'assistant',
    response_text TEXT NOT NULL,
    responded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (question_id) REFERENCES user_questions(question_id)
);


// Tracks each user's login session in the web app.
CREATE TABLE user_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    logout_time TIMESTAMP NULL,
    session_status ENUM('active', 'ended') DEFAULT 'active',
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

//Records actions within a session (like searched FAQ and viewed response).
CREATE TABLE activity_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    session_id INT NOT NULL,
    action_type VARCHAR(100), 
    details TEXT,
    action_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES user_sessions(session_id)
);

_____________________________________________________________________________________________________________________________
//Example Queries
1. Add a new user
INSERT INTO users (full_name, email, role, password_hash)
VALUES ('Adam Smith', 'Adam.Smith@brooklyn.cuny.edu', 'student', 'hashed_password_here');

//2. Log a question
INSERT INTO user_questions (user_id, question_text)
VALUES (1, 'I can’t connect to eduroam on my Mac/Windows');

//3. Add a chatbot response
INSERT INTO responses (question_id, responder_type, response_text)
VALUES (1, 'assistant', 'Try forgetting the Wi-Fi network and reconnecting using your CUNY Login credentials.');

//4. Record session activity 
INSERT INTO activity_logs (session_id, action_type, details)
VALUES (1, 'ask_question', 'User asked about Wi-Fi connection issues');



