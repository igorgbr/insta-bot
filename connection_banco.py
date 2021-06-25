from pymongo import MongoClient
from datetime import datetime, date
from helper import cor_terminal


client = MongoClient("mongodb://localhost:27017")
db = client.insta_bot


def consult_all():
    res_consult = db.insta_bot.find({})
    for doc in res_consult:
        print(doc)


def consult_all_0():
    res_consult = db.insta_bot.find({'likes': 0})

    lista_0_likes = [f"{data['usuario']}\n" for data in res_consult]
    return set(lista_0_likes)


def write_0_like():
    list_0 = open('data/followers_files/zero_likes.txt', 'a')

    for user in consult_all_0():
        list_0.write(user)


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

    hourInsert = datetime.now()
    print('=' * 30)
    print(f'''{cor_terminal['violet']}inserido com sucesso!
    usuario:{user}
    posts: {posts}
    likes: {likes}
    hora da inserção: {hourInsert.strftime("%H:%M")}
    {cor_terminal['clean']}''')
    log.write(f'''inserido com sucesso!
    usuario:{user}
    posts: {posts}
    likes: {likes}
    hora da inserção: {hourInsert.strftime("%H:%M")}
    ''')


# db.insta_bot.delete_one({'usuario': 'ms_sites'})
