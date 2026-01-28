import re

from PySide6.QtGui import QValidator, QIntValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

#from Datos.persona_DAO import PersonaDAO
from Dominio.persona import Persona
from UI.vtnPrincipal import Ui_vtnPrincipal


class PersonaServicio(QMainWindow):
    '''
    Clase que genera la logica de los objetos  persona
    '''
    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.txtCedula.setValidator(QIntValidator())

    def guardar (self):
        nombre = self.ui.txtNombre.text()
        apellido = self.ui.txtApellido.text()
        cedula = self.ui.txtCedula.text()
        sexo = self.ui.cbSexo.currentText()
        email = self.ui.txtemail.text().strip()


        # validacion en uno por uno
        if nombre == '':
            QMessageBox.warning(self,"Advertencia", "Debe ingresar un nombre")
        elif apellido == '':
            QMessageBox.warning(self,"Advertencia", "Debe ingresar un apellido")
        elif len(cedula) < 10:
            QMessageBox.warning(self,"Advertencia", "Debe ingresar un cedula")
        elif sexo == 'Seleccionar':
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar Sexo")
        elif not self.validar_email(email):
            QMessageBox.warning(self, "Advertencia", "Inserte un correo valido")
        else:
            persona = Persona(nombre= nombre, apellido=apellido, cedula=cedula, sexo=sexo, email=email)
            #PersonaDAO.insertar_persona(persona)
            print(persona)
            #print(nombre)
            #print(apellido)
            #print(cedula)
            #print(sexo)

        #validacion en uno solo
          # if nombre == '' or apellido == '': or cedula == '':
          #    QMessageBox.warning(self,"Advertencia", "Debe ingresar los datos completos")

        #mostrar confirmacion de que se guardaron los datos

        self.ui.statusbar.showMessage("Se Guardo con Exito", 3000)

        #borrar campos del formulario
        self.ui.txtNombre.setText('')
        self.ui.txtApellido.setText('')
        self.ui.txtCedula.setText('')
        self.ui.cbSexo.setCurrentText('Seleccionar')
        self.ui.txtemail.clear()

    def limpiar(self):
        self.ui.txtNombre.clear()
        self.ui.txtApellido.clear()
        self.ui.txtCedula.clear()
        self.ui.cbSexo.setCurrentText('Seleccionar')
        self.ui.txtemail.clear()

    def validar_email(self, email: str) -> bool:
        secuencia = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.fullmatch(secuencia, email) is not None

       # def validar_email(self, email: str) -> bool:
        #    secuencia = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        #return re.fullmatch(secuencia, email) is not None