from pymongo import MongoClient
from datetime import datetime, date
from helper import cor_terminal


client = MongoClient("mongodb://localhost:27017")
db = client.insta_bot


def consult_all():
    res_consult = db.insta_bot.find({})
    for doc in res_consult:
        print(doc)


def insert_data(user, posts=0, likes=None,):
    print(
        f"{cor_terminal['yellow']}end - inserindo dados no banco{cor_terminal['clean']}")
    dir = date.today()
    log = open(f'logs/{dir}/logDB - {date.today()}', 'a')
    if likes is None:
        likes = posts
    objdic = {
        'usuario': user,
        'posts': posts,
        'likes': likes,
        'inserido em': datetime.now()
    }
    db.insta_bot.insert_one(objdic)

    print('=' * 30)
    print(f'''{cor_terminal['violet']}inserido com sucesso!
    usuario:{user}
    posts: {posts}
    likes: {likes}
    {cor_terminal['clean']}''')
    log.write(f'''inserido com sucesso!
    usuario:{user}
    posts: {posts}
    likes: {likes}
    ''')


# db.insta_bot.delete_one({'usuario': 'ms_sites'})
