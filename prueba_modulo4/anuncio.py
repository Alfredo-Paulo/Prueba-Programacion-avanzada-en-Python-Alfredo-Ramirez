from abc import ABC, abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self, alto: int, ancho: int, url_archivo: str, url_clic: str, sub_tipo: str):
        self.__sub_tipo = sub_tipo
        self.__alto = alto
        self.__ancho = ancho
        self.__url_clic = url_clic
        self.__url_archivo = url_archivo

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, alto):
        self.__alto = alto if alto > 0 else 1

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho if ancho > 0 else 1

    @property
    def url_archivo(self):
        return self.__url_archivo

    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo

    @property
    def url_clic(self):
        return self.__url_clic

    @url_clic.setter
    def url_clic(self, url_cli):
        self.__url_clic = url_cli

    @property
    def sub_tipo(self):
        return self.__sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        if sub_tipo not in self.SUB_TIPOS:
            raise SubTipoInvalidoError(f"El subtipo '{sub_tipo}' no es válido para este tipo de anuncio.")
        self.__sub_tipo = sub_tipo

    @staticmethod
    def mostrar_formatos(FORMATOS, SUB_TIPOS):
        print(f"{FORMATOS}:")
        print("===========")
        for subtipo in SUB_TIPOS:
            print(f"- {subtipo}")
            
    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass

class Video(Anuncio):
    FORMATOS = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.__duracion = duracion
        self.__alto = 1
        self.__ancho = 1
    
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto):
        pass
    
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        pass

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, value):
        self.__duracion = value if value > 0 else 5

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    FORMATOS = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    FORMATOS = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
        
if __name__ == "__main__":
    
    # Prueba de Anuncio
    print("Anuncio:\n")
    # Prueba de Video
    Video.mostrar_formatos(Video.FORMATOS, Video.SUB_TIPOS)
    print()
    
    test=Video("","","",3)
    test.alto=720
    print(test.alto)