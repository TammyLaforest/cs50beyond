import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


books=[]
def main():
    f = open("books.csv")
    reader = csv.reader(f)
    next(reader)
    # db.execute("DELETE FROM books")
    for isbn, title, author, year in reader:
        if isbn not in books:
            books.append(isbn)
            db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
                        {"isbn": isbn, "title":title, "author": author, "year":year})
    db.commit()

if __name__ == "__main__":
    main()



# author

# isbn		bigint
# title		character varying(50)
# author	character varying(50)
# year		smallint
