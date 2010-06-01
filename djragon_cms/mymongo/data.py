import datetime

post1 = {
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
}

post2 = {
        "_id": "5",
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
}

new_posts = [
        {
            "author": "Mike",
            "text": "Another post!",
            "tags": ["bulk", "insert"],
            "date": datetime.datetime(2009, 11, 12, 11, 14)
        },
        {
            "author": "Eliot",
            "title": "MongoDB is fun",
            "text": "and pretty easy too!",
            "date": datetime.datetime(2009, 11, 10, 10, 45)
        }
]

new_post = {
        'text': "post post post post",
        'title': "post post",
        'author': "Post Postus",
        "date": datetime.datetime.utcnow(),
        "tags": ['my', 'first', 'mapreduce'],
}
