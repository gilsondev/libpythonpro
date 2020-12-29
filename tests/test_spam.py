import pytest

from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()

    assert enviador is not None


@pytest.mark.parametrize('destinatario',
                         ['renzo@python.pro.br', 'foo.bar@mail.com'])
def test_remetente(destinatario):
    enviador = Enviador()
    remetente = 'me@gilsondev.in'
    resultado = enviador.enviar(remetente, destinatario,
                                'Cursos Python Pro', 'Mensagem')

    assert destinatario in resultado
