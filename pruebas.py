ruta_prueba = "niveles//demo.txt" 
ruta_fichero_nivel = ruta_prueba


with open(ruta_fichero_nivel, encoding="utf-8") as f:
       # 1. Lee todo el contenido del archivo como una sola cadena y luego la divide
       texto_entero = f.read()
       print(texto_entero)
       lineas = [linea.strip() for linea in texto_entero.splitlines() if linea.strip()]    #Obtiene las lineas sin espacios y separados por l
       print(len(lineas))
       i = 0
       j = 0
       while i < len(lineas):
        while j < len(lineas[0]):
            zxz 
            j += 1   
        i += 1
       longitudes = [len(linea) for linea in lineas]    # Comprueba el ancho de las lineas
       if len(set(longitudes)) > 1:   
           raise ValueError("Las filas del nivel no tienen el mismo ancho")  
 


def crear_bloques(self) -> None:    #YOOOOOYOOOOO
    """Genera los rectángulos de los bloques en base a la cuadrícula."""
    # - Limpia `self.blocks`, `self.block_colors` y `self.block_symbols`.
    self.blocks.clear(), self.block_colors.clear(), self.block_symbols.clear()
    # - Recorre `self.layout` para detectar símbolos de bloque.
    lista_filas = []
    lista_columnas = []
    for fila, conjunto_caracter in enumerate(self.layout, start=1):
        for columna, caracter in enumerate(conjunto_caracter, start=1): 
            if caracter not in self.BLOQUE_SIMBOLOS:
                raise ValueError("Hay caracteres no definidos en el archivo") 
            lista_filas.append(fila)  # añade la fila correspondiente hasta que termina de añadir las columnas
            lista_columnas.append(columna)