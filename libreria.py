class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True


class Biblioteca:
    def __init__(self):
        self.libros = []

    def registrar_libro(self, titulo, autor, isbn):
        if any(libro.isbn == isbn for libro in self.libros):
            print(f"\n Error: Ya existe un libro registrado con el ISBN '{isbn}'.")
            return
        
        nuevo_libro = Libro(titulo, autor, isbn)
        self.libros.append(nuevo_libro)
        print(f"\n Libro '{titulo}' registrado exitosamente.")

    def listar_libros(self):
        if not self.libros:
            print("\n No hay libros registrados en la biblioteca.")
            return

        print("\n" + "="*50)
        print("          CATÁLOGO EN MEMORIA")
        print("="*50)
        for i, libro in enumerate(self.libros, 1):
            estado = "Disponible" if libro.disponible else "Prestado"
            print(f"{i}. Título: {libro.titulo}")
            print(f"   Autor:  {libro.autor}")
            print(f"   ISBN:   {libro.isbn}")
            print(f"   Estado: [{estado}]")
            print("-" * 50)

    def buscar_libro(self, termino):
        termino = termino.lower()
        coincidencias = [
            l for l in self.libros
            if termino in l.titulo.lower() or termino in l.autor.lower() or termino == l.isbn.lower()
        ]

        if not coincidencias:
            print(f"\n No se encontraron resultados para '{termino}'.")
            return

        print(f"\n--- Resultados para '{termino}' ---")
        for libro in coincidencias:
            estado = "Disponible" if libro.disponible else "Prestado"
            print(f"• '{libro.titulo}' - {libro.autor} (ISBN: {libro.isbn}) [{estado}]")

    def prestar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                if libro.disponible:
                    libro.disponible = False
                    print(f"\n Éxito: Has prestado el libro '{libro.titulo}'.")
                else:
                    print(f"\n Aviso: El libro '{libro.titulo}' ya se encuentra prestado.")
                return
        print(f"\n Error: No existe ningún libro con el ISBN '{isbn}'.")

    def devolver_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                if not libro.disponible:
                    libro.disponible = True
                    print(f"\n Éxito: Se ha devuelto el libro '{libro.titulo}'.")
                else:
                    print(f"\n Aviso: El libro '{libro.titulo}' ya figuraba como disponible.")
                return
        print(f"\n Error: No existe ningún libro con el ISBN '{isbn}'.")


def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n" + "="*35)
        print("    REGISTRADOR DE LIBROS (MEMORIA)")
        print("="*35)
        print("1. Registrar nuevo libro")
        print("2. Mostrar todos los libros")
        print("3. Buscar libro")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Salir")

        opcion = input("\nSeleccione una opción (1-6): ").strip()

        if opcion == "1":
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            isbn = input("ISBN/Código: ").strip()

            if titulo and autor and isbn:
                biblioteca.registrar_libro(titulo, autor, isbn)
            else:
                print("\n Error: Todos los campos son obligatorios.")

        elif opcion == "2":
            biblioteca.listar_libros()

        elif opcion == "3":
            termino = input("Ingrese título, autor o ISBN: ").strip()
            if termino:
                biblioteca.buscar_libro(termino)

        elif opcion == "4":
            isbn = input("ISBN del libro a prestar: ").strip()
            biblioteca.prestar_libro(isbn)

        elif opcion == "5":
            isbn = input("ISBN del libro a devolver: ").strip()
            biblioteca.devolver_libro(isbn)

        elif opcion == "6":
            print("\n Programa finalizado.")
            break
        else:
            print("\n Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()