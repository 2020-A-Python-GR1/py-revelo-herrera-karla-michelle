from scrapy.loader.processors import TakeFirst

def transformar_url_imagen (texto):
    url_fybeca = 'https://www.fybeca.com'
    cadena_texto = '../..'
    return texto.replace(cadena_texto, url_fybeca)

class ProductoFybeca (scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field(
        input_processor = MapCompose( #Permite trabajar con una lista de funciones
            transformar_url_imagen
        ),
        output_processor = TakeFirst() #Se obtiene una lista y se usa para sacar el primero de la lista
    )








