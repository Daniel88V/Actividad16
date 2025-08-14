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
                carnet = input("Ingrese el codigo del usuario: ")
                existe = False
                for usuario in self._usuarios:
                    if usuario._carnet.upper() == carnet.upper():
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
                carrera = input("Ingrese la carrera del usuario: ")
                if not carrera:
                    print("Error. Campo requerido, por favor ingrese la carrera del usuario.")
                else:
                    break
            nuevo_usuario = Usuario(carnet, nombre, carrera)
            self._usuarios.append(nuevo_usuario)
    def buscar_usuario(self):
        def busqueda_secuencual(lista, objetivo):
            for i in range(len(lista)):
                if lista[i].upper() == objetivo.upper():
                    return i
            return None
        buscar = input("Ingrese el carnet del usuario: ")
        users = [usuario._carnet for usuario in self._usuarios]
        lupa = busqueda_secuencual(users, buscar)
        if lupa is not None:
            encontrado = self._usuarios[lupa]
            print(f"Carnet: {encontrado._carnet} | Usuario: {encontrado._nombre} | Carrera: {encontrado._carrera}")
        else:
            print("Usuario no encontrado. Intente con otro carnet")
    def quick_sort(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x._nombre < pivote._nombre]
        iguales = [x for x in lista if x._nombre == pivote._nombre]
        mayores = [x for x in lista[1:] if x._nombre > pivote._nombre]
        return self.quick_sort(menores) + iguales + self.quick_sort(mayores)
    def listado_usuarios(self):
        print("-------Listado de usuarios--------")
        """
        for usuario in self._usuarios:
            print(usuario)
        """
        alfabetico = self.quick_sort(self._usuarios)
        for usuario in alfabetico:
            print(usuario)
        print("------------------------------------")
class BibliorecaLibros:
    def __init__(self):
        self._libros = []
    def ingreso_libro(self):
        cont = int(input("Ingrese cuantos libros ingresar: "))
        for i in range(cont):
            print(f"Libro#{i + 1}: ")
            while True:
                codigo = input("Ingrese el codigo del libro: ")
                existe = False
                for libro in self._libros:
                    if libro._codigo.upper() == codigo.upper():
                        existe = True
                        break
                    if existe:
                        print("Error. Este código ya fue ingresado, pruebe con otro código")
                    else:
                        break
                while True:
                    titulo = input("Ingrese el titulo del libro: ")
                    if not titulo:
                        print("Error. Campo requerido, ingrese el nombre del libro")
                    else:
                        break
                while True:
                    autor = input("Ingrese el nombre del autor del libro: ")
                    if not autor:
                        print("Error. Campo requerido, ingrese el nombre del autor.")
                    else:
                        break
while True:
    biblioteca = BibliotecaUsuarios()
    print("Menu")
    print("1. Registrar Usuario")
    opcion = input("Seleccione: ")
    if opcion == "1":
        biblioteca.registrar_usuario()
