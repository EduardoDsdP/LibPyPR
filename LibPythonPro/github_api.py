def buscar_avatar (Usuario):
    """
    Busca o avatar de um usuario no github
    :param Usuario: str com o nome de usuario no github
    :return: str com o link do avatar
    """
    url= f'https://api.github.com/users/{Usuario}'



