import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
authors=[]
def main():
    f = open("books.csv")
    reader = csv.reader(f)
    # db.execute("DELETE FROM authors")
    for isbn,title, author, year in reader:
        if author not in authors:
            authors.append(author)
            db.execute("INSERT INTO authors (author) VALUES (:author)",
                        {"author": author})
    db.commit()

if __name__ == "__main__":
    main()



# author

# isbn		bigint
# title		character varying(50)
# author	character varying(50)
# year		smallint


	# COPY persons(first_name,last_name,dob,email)
	# FROM 'C:\tmp\persons.csv' DELIMITER ',' CSV HEADER;
