capacidad = 50
asientos_disp = 50
entradas_vendidas = 0
recaudacion = 0.0

while True:
    print("\n--- SISTEMA DEL CINE ---")
    print("1. Comprar entradas")
    print("2. Consultar asientos disponibles")
    print("3. Consultar entradas vendidas")
    print("4. Consultar recaudacion total")
    print("5. Salir")
    
    opcion = input("Elige una opcion: ")
    
    if opcion == "1":
        if asientos_disp == 0:
            print("Ya no quedan asientos para esta funcion.")
            continue
            
        cant = int(input("Cuantas entradas deseas comprar?: "))
        
        if cant <= 0:
            print("La cantidad debe ser mayor a cero.")
        elif cant > asientos_disp:
            print("No hay suficientes asientos. Solo quedan:", asientos_disp)
        else:
            total_compra = 0.0
            
            for i in range(cant):
                print("\nEntrada", i + 1)
                print("1. Adulto ($5.00)")
                print("2. Nino ($3.00)")
                print("3. Tercera edad ($2.50)")
                
                tipo = input("Tipo de espectador: ")
                
                # Validar que elija una opcion correcta
                while tipo != "1" and tipo != "2" and tipo != "3":
                    tipo = input("Opcion no valida. Ingresa 1, 2 o 3: ")
                
                if tipo == "1":
                    total_compra += 5.0
                elif tipo == "2":
                    total_compra += 3.0
                elif tipo == "3":
                    total_compra += 2.5
            
            print("\nTotal a pagar: $", total_compra)
            
            # Actualizar los contadores generales
            asientos_disp -= cant
            entradas_vendidas += cant
            recaudacion += total_compra
            print("Compra realizada con exito.")

    elif opcion == "2":
        ocupados = capacidad - asientos_disp
        print("\n--- ASIENTOS ---")
        print("Capacidad total:", capacidad)
        print("Asientos ocupados:", ocupados)
        print("Asientos disponibles:", asientos_disp)

    elif opcion == "3":
        print("\nEntradas vendidas hasta ahora:", entradas_vendidas)

    elif opcion == "4":
        print("\nRecaudacion total: $", recaudacion)

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opcion incorrecta, intenta de nuevo.")