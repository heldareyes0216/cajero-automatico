def cajero_automatico():
    saldo = 0
    clave = "1234"
    movimientos = []
    print("==== bienvenidos al cajero ==== ")


    while True:
        print("--- menu pricipal ---")
        print("1. consulta saldo ")
        print("2. retiro ")
        print("3. retiro rapido ")
        print("4. depositar ")
        print("5. tranferencia" )
        print("6. gestion de clave")
        print("7. consulta movimientos ")
        print("8. otras operaciones ")
        print("0. salir ")

        option = int(input("seleccione una opcion: "))

        if option == 1:  
            print(f"saldo actual ${saldo}")

        
        
        elif option == 2:
            try:
                monto = float(input("ingrese monto retirar:" ))
                if monto <= 0:
                   print("monto invalido. ")
                elif monto > saldo:
                    print("fondos insuficientes. ")
                else:
                    saldo -= monto
                    movimientos.append(f"retiro: ${monto}")
                    print(f"retiro exitoso. Nuevo saldo ${saldo}")
            except ValueError:
                print("ingrese un numero valido. ")

                               

        elif option == 3:
        
            clave_ingresada = input("ingrese su clave: ")
            if clave_ingresada != clave:
               print("clave correcta.")

            else:
                monto = 100 
                if saldo >= monto:
                  saldo -= monto
                  movimientos.append(f"retiro rapido: ${monto}")
                  print(f"retiro valido exitoso. Nuevo saldo: ${monto}")
                else:
                    print("fondos insuficientes. ")
 
        

        elif option == 4:
            try:
                monto = float(input("ingrese monto a despositar: "))
                if monto <= 0:
                    print("monto invalido.")
                else:
                    saldo += monto
                    movimientos.append(f"deposito: +${monto}")
                    print(f"deposito exitoso. Nuevo saldo: $ {saldo}")
            except ValueError:
                print("ingrese un  numero valido")




            
                        
cajero_automatico()






 




     




 
        
