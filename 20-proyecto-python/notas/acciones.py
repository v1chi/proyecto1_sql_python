import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        titulo = input("Introduce el titulo de la nota: ")
        descripcion = input("Introduce la descripcion de la nota: ")
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"Nota guardada, con el titulo {nota.titulo}")
        else:
            print("La nota no se pudo guardar, intente de nuevo")
    
    def mostrar(self, usuario):
        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.listar()

        for n in notas:
            print("\n-----------------------------------------------")
            print(n[2])
            print(n[3])
    
    def borrar(self, usuario):
        titulo = input("Introduce el titulo de la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo, "")
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print("Nota borrada correctamente")
        else:
            print("No se pudo borrar la nota")