from anuncio import Video, Display, Social
from error import LargoExcedidoError

class Campania:
    
    def __init__(self, nombre: str, anuncios, fecha_inicio, fecha_termino):
        self._nombre = nombre
        # Transformar la lista de anuncios en un diccionario
        self.__anuncios = {i: self.crear_anuncio(anuncio) for i, anuncio in enumerate(anuncios)}
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino

    def crear_anuncio(self, anuncio):
        tipo = anuncio['tipo']
        sub_tipo = anuncio['sub_tipo']
        if tipo == 'Video':
            duracion = anuncio['duracion']
            return Video("", "", sub_tipo, duracion)  # Los primeros dos argumentos son URL de archivo y URL de clic
        elif tipo == 'Display':
            return Display(1, 1, "", "", sub_tipo)  # Se agregan valores predeterminados para url_archivo y url_clic
        elif tipo == 'Social':
            return Social(sub_tipo)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if len(nombre) <= 250:
            self._nombre = nombre
        else:
            raise LargoExcedidoError("El nombre de la campaña excede el límite de 250 caracteres.")

    @property
    def anuncios(self):
        return self.__anuncios

    def __str__(self):
        tipo_contador = {'Video': 0, 'Display': 0, 'Social': 0}
        for anuncio in self.anuncios.values():  # Iterar sobre los valores del diccionario de anuncios
            if isinstance(anuncio, Video):
                tipo_contador['Video'] += 1
            elif isinstance(anuncio, Display):
                tipo_contador['Display'] += 1
            elif isinstance(anuncio, Social):
                tipo_contador['Social'] += 1

        return f"Nombre de la campaña: {self.nombre}\n" \
                f"Anuncios: {tipo_contador['Video']} Video, {tipo_contador['Display']} Display, {tipo_contador['Social']} Social"