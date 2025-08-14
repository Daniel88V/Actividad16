class Libro:
    def __init__(self, codigo, titulo, autor, fecha_publicacion):
        self._codigo = codigo
        self._titulo = titulo
        self._autor = autor
        self._fecha_publicacion = fecha_publicacion
    def __str__(self):
        return f"Libro: {self._titulo}"