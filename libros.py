# Definir el tamaño máximo de la matriz
MAX_LIBROS = 5

# Crear una matriz vacía para almacenar los libros
libros = [[None, None] for _ in range(MAX_LIBROS)]  # Cada fila tiene dos elementos: título y autor

# Solicitar al usuario la información de los libros
for i in range(MAX_LIBROS):
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    libros[i] = [titulo, autor]

# Mostrar los libros almacenados
print("Libros almacenados:")
for i in range(MAX_LIBROS):
    titulo, autor = libros[i]
    print(f"Libro {i + 1}: Título: {titulo}, Autor: {autor}")
