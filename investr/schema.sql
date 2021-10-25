DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS stocks_owned;


CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
);

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    stock_sympol TEXT NOT NULL,
    stock_name TEXT NOT NULL,
    shares INTEGER NOT NULL,
    price NUMERIC NOT NULL,
    timestamp TEXT NOT NULL,
);

CREATE TABLE stocks_owned (
    index INTEGER PRIMARY KEY,
    user_id INTEGER,
    stock_symbol TEXT NOT NULL,
    stock_name TEXT NOT NULL,
    total_shares INTEGER NOT NULL,
);