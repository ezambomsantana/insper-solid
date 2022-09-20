

class Telefone:

    def tocar(self) -> bool:
        raise NotImplementedError

    def discar(self) -> bool:
        raise NotImplementedError

class Foto:

    def tirar_foto(self) -> bool:
        raise NotImplementedError

class Nfc:

    def conecta_nfc(self) -> bool:
        raise NotImplementedError


class TelefoneFixo(Telefone):

    def tocar(self) -> bool:
        return True

    def discar(self) -> bool:
        return True

class TelefoneCelularBarato(Telefone, Foto):

    def tocar(self) -> bool:
        return True

    def discar(self) -> bool:
        return True

    def tirar_foto(self) -> bool:
        return True

class TelefoneCelularCaro(Telefone, Nfc):

    def tocar(self) -> bool:
        return True

    def discar(self) -> bool:
        return True

    def tirar_foto(self) -> bool:
        return True

    def conecta_nfc(self) -> bool:
        return True

telefone = TelefoneCelularCaro()
print(telefone.tirar_foto())