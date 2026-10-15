# 1. Las listas van arriba de todo para que no se borren
libros = []
autores = []

# 2. Usamos un bucle para que el menú se repita y puedas registrar y luego consultar
while True:
    seleccion = int(input('''\nSeleccione qué quiere hacer a continuación:
                  1. Registrar libro
                  2. Registrar autor
                  3. Consultar (libro o autor)
                  4. Salir
                  Ingrese su opción: '''))

    if seleccion == 1:
        cuantos = int(input("¿Cuántos libros va a registrar?: "))
        
        for i in range(cuantos):
            print(f"\n--- Libro {i + 1} ---")
            codigo = input("Ingrese el código del libro: ")
            titulo = input("Ingrese el título del libro: ")
            autor_nombre = input("Ingrese el autor del libro: ")
            
            nuevo_libro = {
                "codigo": codigo,
                "titulo": titulo,
                "autor": autor_nombre
            }
            libros.append(nuevo_libro)

        print("\nLista de libros registrados:")
        print(libros)

    elif seleccion == 2:
        cuantos = int(input("¿Cuántos autores va a registrar?: "))
        
        for i in range(cuantos):
            print(f"\n--- Autor {i + 1} ---")
            nombre = input("Ingrese el nombre del autor: ")
            id_autor = input("Ingrese el ID del autor: ")
            libros_tiene = int(input("Ingrese cuántos libros tiene: "))
            
            nuevo_autor = {
                "nombre": nombre,
                "id": id_autor,
                "libros_tiene": libros_tiene
            }
            autores.append(nuevo_autor)

        print("\nLista de autores registrados:")
        print(autores)

    elif seleccion == 3:
        tipo = input("¿Qué desea buscar? (escriba 'libro' o 'autor'): ").strip().lower()
        
        if tipo == "libro":
            criterio = input("¿Desea buscar por 'id' (código) o por 'nombre' (título)?: ").strip().lower()
            busqueda = input("Ingrese el valor que desea buscar: ").strip()
            
            encontrados = []
            for l in libros:
                if criterio == "id" and l["codigo"] == busqueda:
                    encontrados.append(l)
                elif criterio == "nombre" and busqueda.lower() in l["titulo"].lower():
                    encontrados.append(l)
                    
            print("\nResultado de la búsqueda de libros:")
            print(encontrados if encontrados else "No se encontraron coincidencias.")
            
        elif tipo == "autor":
            criterio = input("¿Desea buscar por 'id' o por 'nombre'?: ").strip().lower()
            busqueda = input("Ingrese el valor que desea buscar: ").strip()
            
            encontrados = []
            for a in autores:
                if criterio == "id" and a["id"] == busqueda:
                    encontrados.append(a)
                elif criterio == "nombre" and busqueda.lower() in a["nombre"].lower():
                    encontrados.append(a)
                    
            print("\nResultado de la búsqueda de autores:")
            print(encontrados if encontrados else "No se encontraron coincidencias.")
        else:
            print("Opción no válida. Debe escribir 'libro' o 'autor'.")
            
    elif seleccion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida en el menú principal.")