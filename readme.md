run:
    docker compose build 
    docker compose up

usage:
    http://172.22.0.3:5000/ -- main page
    http://172.22.0.3:5000/books -- read books from database
    http://172.22.0.3:5000/books/add -- insert book to database with json request

test:
    run curl commands from test_curls.txt file