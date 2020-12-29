from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()

    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar('me@gilsondev.in', 'renzo@python.pro.br',
                    'Cursos Python Pro', 'Mensagem')

    assert 'me@gilsondev.in' in resultado