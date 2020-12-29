class Enviador:
    def enviar(self, remetente, destinatario, assunto, mensagem):
        if '@' not in destinatario:
            raise EmailInvalidoError(
                f'Email de destinatario invalido: {destinatario}')

        return destinatario


class EmailInvalidoError(Exception):
    pass
