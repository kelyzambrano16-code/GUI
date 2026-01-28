import valor


class Persona:
    '''
    Clase que permite crear objetos de persona
    '''
    def __init__(self, cedula:str, nombre:str, apellido:str, sexo:str
                 , email:str):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._sexo = sexo
        self._email = email

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, valor):
        if not valor.isdigit():
            raise ValueError("La cédula debe contener solo números.")
        if len(valor) != 10:
            raise ValueError("La cédula debe tener exactamente 10 dígitos.")
        self._cedula= valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        self._apellido = valor

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, valor):
        self._sexo = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        self._email = valor

    def __str__(self):
        return (f"Persona [Cédula: {self._cedula}, Nombre: {self._nombre},"
                f" Apellido: {self._apellido}, Sexo: {self._sexo}, Email: {self._email}]")
