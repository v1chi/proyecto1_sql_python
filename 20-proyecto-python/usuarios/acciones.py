import usuarios.usuario as modelo
import notas.acciones

class Acciones:

    def registro(self):
        print("Registro")
        nombre = input("Ingrese su nombre: ")
        apellidos = input("Ingrese sus apellidos: ")
        email = input("Ingrese su email: ")
        passwd = input("Ingrese la contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, passwd)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(f"Registro correcto, bienvenidx {registro[1].nombre}")
        else:
            print("Error al registrarse")
    

    def login(self):
        print("Login")
        email = input("Ingrese su email: ")
        passwd = input("Ingrese la contraseña: ")

        try: 
            usuario = modelo.Usuario('', '', email, passwd)
            login = usuario.identificar()
            if email == login[3]:
                print(f"Bienvenidx {login[1]}")
                self.proximasAcciones(login)

        except:
            print("Error al iniciar sesión, intente de nuevo")
            self.login()
    
    def proximasAcciones(self, usuario):
        print(""" 
        Que desea hacer:
        1. Crear una nueva nota
        2. Mostrar todas las notas
        3. Eliminar una nota
        4. Salir
        """)    

        accion = input("Ingrese la accion que desea realizar: ")
        hazEl = notas.acciones.Acciones()

        if accion == "1":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "2":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "3":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "4":
            print("Hata luego")
