lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]
#Insertar elementos
lenguajes.insert(3, "Go")
lenguajes.insert(0, "C")
#Eliminar elementos
lenguajes.remove("Ruby")
#Si existe un elemento
print("PHP" in lenguajes)
#Limpiar el listado
#lenguajes.clear()
#Cuenta el número de elementos que tiene el arreglo
print(len(lenguajes))