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
