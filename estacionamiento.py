import os

def apretar_enter():
    input("\nAPRETE ENTER PARA CONTINUAR...")

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_cobro(horas):
    if horas < 1:
        return 2000
    else:
        return horas * 2500

espacios_disponibles = 10
autos_atendidos = 0
recaudacion_total = 0

while True:
    limpiar_pantalla()
    print("\n--- SISTEMA DE ESTACIONAMIENTO ---")
    print("\n1. Ingresar vehículo")
    print("2. Retirar vehículo")
    print("3. Salir")
    
    opcion = input("\nElegí una opción (1-3): ")
    
    if opcion == "1":
        limpiar_pantalla()
        if espacios_disponibles > 0:
            espacios_disponibles = espacios_disponibles - 1
            autos_atendidos = autos_atendidos + 1
            print("VEHÍCULO INGRESADO. QUEDAN", espacios_disponibles, "ESPACIOS DISPONIBLES")
        else:
            print("ESTACIONAMIENTO LLENO! NO QUEDAN LUGARES DISPONIBLES")
        apretar_enter()  

    elif opcion == "2":
        limpiar_pantalla()
        print("\nSE VA A RETIRAR UN VEHÍCULO")
        if espacios_disponibles == 10:
            print("\nERROR! No hay autos ingresados, el estacionamiento está vacío!")
            apretar_enter()
        else:
            try:
                espacios_disponibles = espacios_disponibles + 1
                hora_estacionado = float(input("\nCUANTAS HORAS ESTUVO ESTACIONADO?: ")) 
                costo_estacionado = calcular_cobro(hora_estacionado)     
                recaudacion_total = recaudacion_total + costo_estacionado  
            except ValueError:
                print("\nERROR! ingrese un número válido...")
                apretar_enter()    

    elif opcion == "3":
        limpiar_pantalla()
        print("\nPROGRAMA FINALIZADO")
        print("\nAUTOS ATENDIDOS: ", autos_atendidos)
        print("RECAUDACION TOTAL: $", recaudacion_total)
        apretar_enter()
        break   
    else:
        print("\nERROR!, opción inválida")    
        apretar_enter