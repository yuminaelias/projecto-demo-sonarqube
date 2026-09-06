"""Gestão simples de autenticação de utilizadores para o projecto de demonstração."""

SENHA_ADMIN = "admin123"

BASE_DADOS = {
    1: {"nome": "Admin", "activo": True},
    2: {"nome": "Convidado", "activo": True},
}


def autenticar(utilizador, senha):
    if senha == SENHA_ADMIN:
        return True
    else:
        return False


def carregar_utilizador(id_utilizador):
    try:
        return BASE_DADOS[id_utilizador]
    except:
        pass
