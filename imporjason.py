import json
 
 
# Ejemplo 1: Convertir un string JSON simple a un diccionario de Python
json_string = '{"nombre": "Gabriel", "edad": 30, "ciudad": "Santiago"}'
datos = json.loads(json_string)
 
print("Ejemplo 1 - Diccionario simple:")
print(datos)
print(f"Nombre: {datos['nombre']}")
print(f"Edad: {datos['edad']}")
print()
 
# Ejemplo 2: JSON con lista
json_array = '[{"producto": "Laptop", "precio": 999}, {"producto": "Mouse", "precio": 25}]'
productos = json.loads(json_array)
 
print("Ejemplo 2 - Lista de productos:")
for producto in productos:
    print(f"{producto['producto']}: ${producto['precio']}")
print()
 
# Ejemplo 3: JSON anidado
json_complejo = '''
{
    "empresa": "TechCorp",
    "empleados": [
        {
            "nombre": "Ana",
            "rol": "Desarrolladora",
            "habilidades": ["Python", "JavaScript", "SQL"]
        },
        {
            "nombre": "Carlos",
            "rol": "Diseñador",
            "habilidades": ["Photoshop", "Figma"]
        }
    ],
    "activa": true,
    "fundacion": 2020
}
'''
 
empresa = json.loads(json_complejo)
 
print("Ejemplo 3 - JSON anidado:")
print(f"Empresa: {empresa['empresa']}")
print(f"Fundada en: {empresa['fundacion']}")
print("\nEmpleados:")
for empleado in empresa['empleados']:
    print(f"- {empleado['nombre']} ({empleado['rol']})")
    print(f"  Habilidades: {', '.join(empleado['habilidades'])}")