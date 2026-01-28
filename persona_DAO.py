'''
from Datos.conexion import Conexion
from Dominio.persona import Persona


class PersonaDAO:
    _INSERT = ("INSERT INTO Personas ( nombres, apellidos, cedula, sexo, email)"
               "VALUES (?,?,?,? , null)")

    @classmethod
    def insertar_persona(cls, persona):
        with Conexion.obtenerCursor() as cursor:
            datos = (persona.nombre, persona.apellido, persona.cedula, persona.sexo, persona.email)
            cursor.execute(cls._INSERT, datos)

if __name__ == '__main__':
    p1 = Persona(cedula ='0948578425',nombre="Tatiana", apellido="Alvarado", sexo="Femenino", email="kely.zambranoa@ug.edu.ec")
    PersonaDAO.insertar_persona(p1)
'''