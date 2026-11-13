#Cajero automatico
saldo = 00.0  # Saldo inicial de ejemplo

while True:
    print('''
====================CAJERO AUTOMATICO UTC====================
        1.Consultar saldo
        2. Depositar
        3. Retiro
        4. Salir
============================================================='''
    )
    opcion = int(input('Selecciones una opcion: '))
    
    match opcion:
        case 1:
            print(f'Saldo Actual: ${saldo:.2f}')
        
        case 2:
            monto = float(input('Ingrese la cantidad a depositar: $'))
            if monto > 0:
                saldo += monto
                print(f'Depósito exitoso. Nuevo saldo: ${saldo:.2f}')
            else:
                print('El monto debe ser mayor a 0.')
                
        case 3:
            monto = float(input('Ingrese la cantidad a retirar: $'))
            if monto <= 0:
                print('El monto a retirar debe ser mayor a 0.')
            elif monto > saldo:
                print('Saldo insuficiente.')
            else:
                saldo -= monto
                print(f'Retiro exitoso. Nuevo saldo: ${saldo:.2f}')
                
        case 4:
            print('Gracias por utilizar nuestro cajero')
            break
            
        case _:
            print('Opción inválida. Intente de nuevo.')