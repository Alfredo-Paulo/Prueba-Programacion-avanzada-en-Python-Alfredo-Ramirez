from campania import Campania
from error import LargoExcedidoError, SubTipoInvalidoError
import datetime

try:
    # Crear una instancia de Campaña con un anuncio de tipo Video
    anuncios = [{'tipo': 'Video', 'sub_tipo': 'outstream', 'duracion': 4},
                {'tipo': 'Display', 'sub_tipo': 'nativo'},
                {'tipo': 'Display', 'sub_tipo': 'tradicional'}]
    # Crear la instancia de Campania
    fecha_inicio = datetime.date(2023, 4, 1)
    fecha_termino = datetime.date(2023, 6, 30)
    campania = Campania("Campaña de prueba", anuncios, fecha_inicio, fecha_termino)
    # Imprimir la representación de la campaña
    print(campania)
    # Solicitar al usuario que ingrese un nuevo nombre para la campaña
    nuevo_nombre = input("\nIngrese el nuevo nombre para la campaña: ")
    campania.nombre = nuevo_nombre

    # Solicitar al usuario que ingrese un nuevo subtipo para el anuncio
    nuevo_subtipo = input("Ingrese el nuevo subtipo para el anuncio: ")

    # Obtener el primer anuncio de la campaña
    primer_anuncio = campania.anuncios[0]

    # Modificar el subtipo del primer anuncio
    primer_anuncio.sub_tipo = nuevo_subtipo

except (LargoExcedidoError, SubTipoInvalidoError) as e:
    # Manejar las excepciones y escribir los mensajes en archivos de registro diferentes
    if isinstance(e, LargoExcedidoError):
        # Manejar la excepción de LargoExcedidoError y escribir el mensaje en un archivo de registro
        with open('dia13/prueba_modulo4/logs/largo.log', 'a+') as errorlargo:
            errorlargo.write(str(e) + '\n')
    elif isinstance(e, SubTipoInvalidoError):
        # Manejar la excepción de SubTipoInvalidoError y escribir el mensaje en un archivo de registro
        with open('dia13/prueba_modulo4/logs/subtipo.log', 'a+') as errorsubtipo:
            print("\nEl subtipo no es válido:\n")
            errorsubtipo.write(str(e) + '\n')

print(campania)