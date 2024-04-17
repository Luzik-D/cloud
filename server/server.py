from flask import Flask, render_template, request, jsonify
import mysql.connector
import os
import time

app = Flask(__name__)

time.sleep(5)

cnx = mysql.connector.connect(user='root', password='admin',
                              host='mysqldb',
                              database='db')

cursor = cnx.cursor(buffered=True)
def init_db():
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INT, title VARCHAR(255), author VARCHAR(255))")

@app.route("/")
def hello_world():
    return "Welcome to bookStorage"

@app.route("/books")
def getBooks():
    books = []
    cursor.execute("SELECT title, author FROM books")
    for res in cursor.fetchall():
        print(res)
        books.append(f"title: {res[0]}, author: {res[1]}\n")
    
    return "".join(books)

@app.route("/books/add", methods=["POST"])
def addBook():
    content = request.json
    title = content.get("title")
    author = content.get("author")
    print(title, author)
    cursor.execute(f"INSERT INTO books (title, author) VALUES ('{title}', '{author}')")
    cnx.commit()
    return content


if __name__ == "__main__":
    init_db()
    app.run("0.0.0.0", port="5000")
