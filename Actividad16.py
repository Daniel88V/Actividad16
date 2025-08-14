class Libro:
    def __init__(self, codigo, titulo, autor, fecha_publicacion):
        self._codigo = codigo
        self._titulo = titulo
        self._autor = autor
        self._fecha_publicacion = fecha_publicacion
    def __str__(self):
        return f"Libro: {self._titulo} | Autor: {self._autor} | Fecha: {self._fecha_publicacion}"
class Usuario:
    def __init__(self, carnet, nombre, carrera):
        self._carnet = carnet
        self._nombre = nombre
        self._carrera = carrera
    def __str__(self):
        return f"Nombre: {self._nombre} | Carrera: {self._carrera}"
class BibliotecaUsuarios:
    def __init__(self):
        self._usuarios = []
    def registrar_usuario(self):
        cont = int(input("Ingrese cuantos usuarios desea ingresar: "))
        for i in range(cont):
            print(f"Usuario#{i + 1}: ")
            while True:
                codigo = input("Ingrese el codigo del usuario: ")
                existe = False
                for usuario in self._usuarios:
                    if usuario._codigo.upper() == codigo.upper():
                        existe = True
                        break
                if existe:
                    print("Error.Usuario ya existente, ingrese un código distinto")
                else:
                    break
            while True:
                nombre = input("Ingrese el nombre del usuario: ")
                if not nombre:
                    print("Error. Campo requerido, por favor ingrese el nombre del usuario.")
                else:
                    break
            while True:
                carrera = input("Ingrese el carrera del usuario: ")
                if not carrera:
                    print("Error. Campo requerido, por favor ingrese la carrera del usuario.")
                else:
                    break
            nuevo_usuario = Usuario(codigo, nombre, carrera)
            self._usuarios.append(nuevo_usuario)
while True:
    biblioteca = BibliotecaUsuarios()
    print("Menu")
    print("1. Registrar Usuario")
    opcion = input("Seleccione: ")
    if opcion == "1":
        biblioteca.registrar_usuario()
