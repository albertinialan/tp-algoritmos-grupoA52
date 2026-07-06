espacios_disponibles = 10
autos_atendidos = 0

while True:
    print("\n--- SISTEMA DE ESTACIONAMIENTO ---")
    print("1. Ingresar vehículo")
    print("2. Retirar vehículo")
    print("3. Salir")
    
    opcion = input("Elegí una opción (1-3): ")
    
    if opcion == "1":
        if espacios_disponibles > 0:
            espacios_disponibles = espacios_disponibles - 1
            autos_atendidos = autos_atendidos + 1
            print("Vehículo ingresado. Quedan", espacios_disponibles, "espacios disponibles")
        else:
            print("ESTACIONAMIENTO LLENO! NO QUEDAN LUGARES DISPONIBLES")
    elif opcion == "2":
        print("voy a programar la saluda y el cobro")                 
    elif opcion == "3":
        print("PROGRAMA FINALIZADO")
        break   
    else:
        print("ERROR!, opción inválida")    