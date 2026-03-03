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

        elif option == 5:
            clave_ingresada = input("ingrese su clave") 
            if clave_ingresada !=clave:
                print("clave incorrecta")
            else:
                try:
                    cuenta_destino = input("ingrese numero de cuenta destino")
                    
                    if not cuenta_destino.isdigit():
                        print("numero de cuenta invalido")
                    
                    else:
                        monto = float(input("ingrese monto a transferir"))
                        
                        if monto <=0:
                            print ("monto invalido")
                        elif monto > saldo:
                            print("fondos insuficientes.")
                        else:
                            saldo -= monto
                            movimientos.append(f"transferencia a {cuenta_destino}: -${monto}")
                        print (f"Transferencia exitosa. Nuevo saldo: ${saldo}")
                except ValueError:
                    print("ingrese numero valido")
        
        
        elif option == 6: 
            clave_actual = input("ingrese su clave actual")
            
            if clave_actual!= clave:
                print("clave incorrecta")
            else:
                nueva_clave = input("ingrese nueva clave:")
                confirmar_clave =input("confirme nueva clave")
                
                if nueva_clave != confirmar_clave:
                    print("las claes no coinciden")
                elif len(nueva_clave) !=4 or not nueva_clave.isdigit():
                    print("ña cñave debe tener 4 numeros")
                else:
                    clave = nueva_clave
                    print("Clave actualizada exitosamente")
                    
        
        elif option ==7:
            if len(movimientos) == 0:
                print("No hay movimientos registrados")
            else:
                print ("\n==== HISTORIAL DE MOVIMIENTOS ====")
                for i, movimientos in enumerate(movimientos,start=1):
                    print(f"{i}. {movimientos}")
        
        
        
        elif option == 8:
            print("\n--- PAGOS ---")
            print("1. Pagar luz")
            print("2. Pagar agua")
            print("3. Pagar internet")
            print("4. Pagar tarjeta de credito")
            print("0. Volver")
            sub_option = int(input("Seleccione una opcion: "))

        if sub_option == 0:
            print("Volviendo al menu principal")

        else:
            clave_ingresada = input("Ingrese su clave: ")

        if clave_ingresada != clave:
            print("Clave incorrecta.")
        else:
            try:
                monto = float(input("Ingrese monto a pagar: "))

                if monto <= 0:
                        print("Monto invalido.")
                elif monto > saldo:
                        print("Fondos insuficientes.")
                else:
                        saldo -= monto

                if sub_option == 1:
                        movimientos.append(f"Pago luz: -${monto}")
                        print(f"Pago de luz exitoso. Nuevo saldo: ${saldo}")

                elif sub_option == 2:
                        movimientos.append(f"Pago agua: -${monto}")
                        print(f"Pago de agua exitoso. Nuevo saldo: ${saldo}")

                elif sub_option == 3:
                        movimientos.append(f"Pago internet: -${monto}")
                        print(f"Pago de internet exitoso. Nuevo saldo: ${saldo}")

                elif sub_option == 4:
                        movimientos.append(f"Pago tarjeta credito: -${monto}")
                        print(f"Pago de tarjeta exitoso. Nuevo saldo: ${saldo}")

                else:
                        print("Opcion invalida.")

            except ValueError:
                print("Ingrese un numero valido.") 
                print(f"Cuenta: 123456789")
                print(f"Saldo disponible: ${saldo}")
                print(f"Clave actual: **")
                
            
                        
cajero_automatico()






 




     




 
        
