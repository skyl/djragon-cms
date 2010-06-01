from pymongo import Connection, ASCENDING, DESCENDING

c = Connection()
db = c.test
collection = db.posts
collection.create_index([("date", DESCENDING), ("author", ASCENDING)])


