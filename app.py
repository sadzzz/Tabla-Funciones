import streamlit as st

def saludar(nombre):
    return f"Hola, {nombre}"

def sumar(a, b):
    return a + b

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_precio_final(precio, descuento=10, impuesto=16):
    precio_descuento = precio - (precio * descuento / 100)
    precio_final = precio_descuento + (precio_descuento * impuesto / 100)
    return precio_final

def sumar_lista(numeros):
    return sum(numeros)

def producto(nombre, cantidad=1, precio_por_unidad=10):
    return cantidad * precio_por_unidad

def numeros_pares_e_impares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]
    return pares, impares

def multiplicar_todos(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

def informacion_personal(**kwargs):
    return kwargs

def calculadora_flexible(a, b, operacion="suma"):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicacion":
        return a * b
    elif operacion == "division":
        return a / b

st.title("Aplicación Interactiva de Funciones en Python")

st.header("Ejercicio 1: Función de saludo simple")
nombre = st.text_input("Ingresa tu nombre:")
if nombre:
    st.write(saludar(nombre))

st.header("Ejercicio 2: Suma de dos números")
num1 = st.number_input("Ingresa el primer número:", value=0)
num2 = st.number_input("Ingresa el segundo número:", value=0)
st.write("La suma es:", sumar(num1, num2))

st.header("Ejercicio 3: Área de un triángulo")
base = st.number_input("Ingresa la base del triángulo:", value=0)
altura = st.number_input("Ingresa la altura del triángulo:", value=0)
st.write("El área del triángulo es:", calcular_area_triangulo(base, altura))

st.header("Ejercicio 4: Calculadora de descuento")
precio = st.number_input("Ingresa el precio original:", value=0)
descuento = st.number_input("Ingresa el porcentaje de descuento:", value=10)
impuesto = st.number_input("Ingresa el porcentaje de impuesto:", value=16)
st.write("El precio final es:", calcular_precio_final(precio, descuento, impuesto))

st.header("Ejercicio 5: Suma de una lista de números")
numeros = st.text_input("Ingresa una lista de números separados por comas:")
if numeros:
    lista_numeros = list(map(int, numeros.split(',')))
    st.write("La suma de la lista es:", sumar_lista(lista_numeros))

st.header("Ejercicio 6: Funciones con valores predeterminados")
nombre_producto = st.text_input("Ingresa el nombre del producto:")
cantidad = st.number_input("Ingresa la cantidad:", value=1)
precio_por_unidad = st.number_input("Ingresa el precio por unidad:", value=10)
st.write("El precio total es:", producto(nombre_producto, cantidad, precio_por_unidad))

st.header("Ejercicio 7: Números pares e impares")
numeros = st.text_input("Ingresa una lista de números separados por comas:")
if numeros:
    lista_numeros = list(map(int, numeros.split(',')))
    pares, impares = numeros_pares_e_impares(lista_numeros)
    st.write("Números pares:", pares)
    st.write("Números impares:", impares)

st.header("Ejercicio 8: Multiplicación con *args")
numeros = st.text_input("Ingresa una lista de números separados por comas:")
if numeros:
    lista_numeros = list(map(int, numeros.split(',')))
    st.write("El resultado de la multiplicación es:", multiplicar_todos(*lista_numeros))

st.header("Ejercicio 9: Información de una persona con **kwargs")
nombre = st.text_input("Nombre:")
edad = st.number_input("Edad:", value=0)
direccion = st.text_input("Dirección:")
if nombre and edad and direccion:
    info = informacion_personal(nombre=nombre, edad=edad, direccion=direccion)
    st.write(info)

st.header("Ejercicio 10: Calculadora flexible")
num1 = st.number_input("Ingresa el primer número:", value=0)
num2 = st.number_input("Ingresa el segundo número:", value=0)
operacion = st.selectbox("Selecciona la operación:", ["suma", "resta", "multiplicacion", "division"])
st.write("El resultado es:", calculadora_flexible(num1, num2, operacion))
