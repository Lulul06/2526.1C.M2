ruta_prueba = "niveles//demo.txt" 
ruta_fichero_nivel = ruta_prueba


with open(ruta_fichero_nivel, encoding="utf-8") as f:
       # 1. Lee todo el contenido del archivo como una sola cadena y luego la divide
       texto_entero = f.read()
       print(texto_entero)
       lineas = [linea.strip() for linea in texto_entero.splitlines() if linea.strip()]    #Obtiene las lineas sin espacios y separados por l
       print(lineas)
       longitudes = [len(linea) for linea in lineas]    # Comprueba el ancho de las lineas
       if len(set(longitudes)) > 1:   
           raise ValueError("Las filas del nivel no tienen el mismo ancho")  
 
   
