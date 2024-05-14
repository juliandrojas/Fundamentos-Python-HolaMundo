texto = "Hola Mundo"
print(texto.upper())
print(texto.lower())
#En que indice está la M
print(texto.find("M"))
#En que indice está la cadena Mun
print(texto.find("Mun"))
#No se encuentra la cadena mun (case sensitive, retorna -1)
print(texto.find("mun"))
#Cambia la cadena (si la encuentra) por la que le especifiquemos (en el segundo parámetro)
#NOTA: No cambia la cadena original
nuevoTexto = texto.replace("Mundo", "chanchito feliz")
print(texto, nuevoTexto)
#Buscar una palabra en una cadena
print("Mundo" in texto)

