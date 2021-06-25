arquivo = open('users.txt', 'r')

conteudo_total = arquivo.readlines()

user_list = [data.replace('\n', '') for data in conteudo_total]

arquivo.close()
