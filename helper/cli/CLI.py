cor_terminal = {
    "red": "\033[31m",
    "violet": "\033[35m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "purple": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "clean": "\033[0m",
}


def PROCESSANDO_USUARIO(user):
    print(
        f'{cor_terminal["cyan"]}PROCESSANDO USUARIO {user}{cor_terminal["clean"]}'
    )


def TOKEN_EXPIRADO():
    print(f'{cor_terminal["red"]}TOKEN EXPIRADO{cor_terminal["clean"]}')


def USUARIO_N_TEM_POSTAGEM():
    print(
        f'{cor_terminal["yellow"]}Usuario não tem postagem{cor_terminal["clean"]}'
    )


def POST_N_TEM_LIKE(i):
    print(
        f'{cor_terminal["green"]} post {i} - não tinha like{cor_terminal["clean"]}'
    )


def USUARIOS_VARRIDOS(user_list):
    print(
        f'{cor_terminal["green"]} {len(user_list)} Usuarios varridos{cor_terminal["clean"]}'
    )


def TOTAL_LIKES(tot_like):
    print(
        f'{cor_terminal["green"]} Total de likes: {tot_like}{cor_terminal["clean"]}'
    )


def EXCESSO_DE_REQUISICOES(timeError, timeRegret):
    print(
        f'{cor_terminal["red"]}Excesso de requisições {timeError.strftime("%H:%M")} volta em {timeRegret.strftime("%H:%M")}{cor_terminal["clean"]}'
    )


def FIM_DO_SCRIPT():
    print(f'{cor_terminal["green"]}FIM DO SCRIPT{cor_terminal["clean"]}')
