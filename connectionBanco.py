from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017")
db = client.insta_bot


def consult_all():
    res_consult = db.insta_bot.find({})
    for doc in res_consult:
        print(doc)


def insert_data(user, posts=0, likes=None,):
    if likes is None:
        likes = posts
    objdic = {
        'usuario': user,
        'posts': posts,
        'likes': likes,
        'inserido em': datetime.now()
    }
    db.insta_bot.insert_one(objdic)
    print(f'''inserido com sucesso!
    usuario:{user}
    posts: {posts}
    likes: {likes}''')


# db.insta_bot.delete_one({'usuario': 'ms_sites'})
