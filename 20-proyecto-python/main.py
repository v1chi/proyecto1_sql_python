"""
-Registrar usuario o Login de usuario
-Login:
    *Crear nota
    *Borra nota
    *Mostrar notas
"""
from usuarios import acciones

print("""
Acciones disponibles:
      - registro
      - login
""")

hazEl = acciones.Acciones()
accion = input("Que deseas hacer?: ")

if accion == "login":
    hazEl.login()
    

elif accion == "registro":
    hazEl.registro()

