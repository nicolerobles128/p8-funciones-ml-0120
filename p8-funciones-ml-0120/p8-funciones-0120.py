# Nicole Robles NC 0120
print("==================================================")
print("          LISTA DE NOMBRES (1 AL 30)")
print("==================================================")

nombres_1_30 = [
    "Alejandro", "Sofía", "Mateo", "Valentina", "Santiago", "Isabella", "Gabriel", "Camila", "Lucas", "Mariana",
    "Daniel", "Valeria", "Nicolás", "Lucía", "Diego", "Natalia", "Samuel", "Daniela", "Joaquín", "Victoria",
    "Sebastián", "Martina", "Andrés", "Paula", "Leonardo", "Elena", "Carlos", "Andrea", "Fernando", "Claudia"
]
print(nombres_1_30)

print("\n==================================================")
print("          LISTA DE NOMBRES (31 AL 60)")
print("==================================================")

nombres_31_60 = [
    "Javier", "Carmen", "Tomás", "Sara", "Rodrigo", "Marta", "Hugo", "Laura", "Martín", "Irene",
    "Gonzalo", "Alba", "Manuel", "Beatriz", "Pablo", "Alicia", "Esteban", "Rocío", "Adrián", "Clara",
    "Mario", "Cristina", "Raúl", "Silvia", "Iván", "Lorena", "Marcos", "Patricia", "David", "Mónica"
]
print(nombres_31_60)


print("\n==================================================")
print("     BLOQUE 1: EL PYTHONISTA (6 EJEMPLOS)")
print("==================================================")

print("\n--- Ejemplo 1: Función básica ---")
def saludar():
    print("¡Hola, mundo!")

saludar()

print("\n--- Ejemplo 2: Parámetros posicionales ---")
def calcular_area(ancho, alto):
    return ancho * alto

print(calcular_area(5, 10))

print("\n--- Ejemplo 3: Parámetro por defecto ---")
def saludar_persona(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"

print(saludar_persona("Sofía"))

print("\n--- Ejemplo 4: Retorno múltiple ---")
def calcular_estadisticas(numeros):
    return sum(numeros), sum(numeros) / len(numeros), max(numeros)

suma, prom, max_val = calcular_estadisticas([10, 20, 30])
print(f"Suma: {suma}, Promedio: {prom}, Máximo: {max_val}")

print("\n--- Ejemplo 5: *args y **kwargs ---")
def crear_perfil(nombre, *aficiones, **detalles):
    print(f"Nombre: {nombre}")
    print(f"Aficiones: {aficiones}")
    print(f"Detalles: {detalles}")

crear_perfil("Gabriel", "Fútbol", edad=28)

print("\n--- Ejemplo 6: Validación de email ---")
def validar_email(email):
    return "@" in email and "." in email.split("@")[1]

print(validar_email("usuario@ejemplo.com"))


print("\n==================================================")
print("       BLOQUE 2: PYTHONES (5 EJEMPLOS)")
print("==================================================")

print("\n--- Ejemplo 7: Built-in ---")
mensaje = "Hola Python"
print(f"Longitud: {len(mensaje)}, Tipo: {type(mensaje)}")

print("\n--- Ejemplo 8: Suma simple ---")
def suma(a, b):
    return a + b

print(suma(4, 5))

print("\n--- Ejemplo 9: Cálculo con impuesto ---")
def precio_final(precio, impuesto):
    return precio * (1 + impuesto)

print(precio_final(100, 0.21))

print("\n--- Ejemplo 10: Argumentos por nombre ---")
def presentar(nombre, edad, ciudad):
    return f"{nombre}, {edad} años, {ciudad}"

print(presentar(ciudad="Sevilla", nombre="Carmen", edad=32))

print("\n--- Ejemplo 11: Calculadora ---")
def calculadora(a, b, operacion):
    operaciones = {
        "sumar": a + b,
        "restar": a - b,
        "multiplicar": a * b,
        "dividir": a / b if b != 0 else "Error"
    }
    return operaciones.get(operacion, "Inválido")

print(calculadora(10, 2, "multiplicar"))
print("Nicole Robles NC 0120")