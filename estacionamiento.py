espacios_disponibles = 10
autos_atendidos = 0
recaudacion_total = 0

while True:
    print("\n--- SISTEMA DE ESTACIONAMIENTO ---")
    print("\n1. Ingresar vehículo")
    print("2. Retirar vehículo")
    print("3. Salir")
    
    opcion = input("\nElegí una opción (1-3): ")
    
    if opcion == "1":
        if espacios_disponibles > 0:
            espacios_disponibles = espacios_disponibles - 1
            autos_atendidos = autos_atendidos + 1
            print("VEHÍCULO INGRESADO. QUEDAN", espacios_disponibles, "ESPACIOS DISPONIBLES")
        else:
            print("ESTACIONAMIENTO LLENO! NO QUEDAN LUGARES DISPONIBLES")
    elif opcion == "2":
        print("\nSE VA A RETIRAR UN VEHÍCULO")
        espacios_disponibles = espacios_disponibles + 1
        hora_estacionado = float(input("\nCUANTAS HORAS ESTUVO ESTACIONADO? ")) 
        if hora_estacionado < 1:
            costo_estacionado = 2000
        else:  
            costo_estacionado = hora_estacionado * 2500        
        recaudacion_total = recaudacion_total + costo_estacionado   
    elif opcion == "3":
        print("\nPROGRAMA FINALIZADO")
        print("AUTOS ATENDIDOS: ", autos_atendidos)
        print("RECAUDACION TOTAL: ", recaudacion_total)
        break   
    else:
        print("\nERROR!, opción inválida")    