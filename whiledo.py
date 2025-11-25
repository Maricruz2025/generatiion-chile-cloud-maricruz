frutas = []
 
while True:
    nombre = input("Ingresa el nombre de la fruta que deseas agregar: ")
 
    if nombre == "salir": # salir cuando el usuario ingrese 'salir'
        break
    precio = float(input(f"Ingresa el precio de {nombre}: "))
 
    fruta = {
        "nombre" :nombre,
        "precio" : precio
    }
    frutas.append(fruta)
    print(f"Ingresando la fruta: {nombre} con el precio de {precio}")
 
print("Frutas ingresadas:", frutas)
#for para imprimir un ticket de compra a la terminal

print("\n--- Ticket de Compra ---")
total = 0
for fruta in frutas:
    print(f"{fruta['nombre']} - ${fruta['precio']:.2f}")
    total += fruta['precio']

print("------------------------")
print(f"TOTAL: ${total:.2f}")