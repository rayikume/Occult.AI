-- Create Users Table
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(255) PRIMARY KEY,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL
);

-- Create Authors Table
CREATE TABLE IF NOT EXISTS authors (
    author_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);

-- Create Books Table
CREATE TABLE IF NOT EXISTS books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    genre VARCHAR(100),
    description TEXT,
    thumbnail TEXT
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

-- Create User Preferences Table
CREATE TABLE IF NOT EXISTS user_preferences (
    preference_id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    genre VARCHAR(100) NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
);

-- Create User Activities Table
CREATE TABLE IF NOT EXISTS user_activities (
    activity_id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    activity VARCHAR(255) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (username) REFERENCES users(username)
);