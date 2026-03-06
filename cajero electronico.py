def cajero_automatico():
    saldo = 0
    clave = "1234"
    movimientos = []
    from datetime import datetime
    ahora = datetime.now()
    fecha_formateada = ahora.strftime("%d/%m/%Y, %H:%M:%S")

    print("==== Bienvenidos al cajero ==== ")


    while True:
        print("\n--- menu pricipal ---")
        print("1. deposito ")
        print("2. retiro ")
        print("3. consulta saldo ")
        print("4. tranferencia" )
        print("5. gestión de clave")
        print("6. consulta movimientos ")
        print("7. otras operaciones ")
        print("0. salir ")

        try:
            option = int(input("seleccione una opción: "))
        except ValueError:
            print("Ingrese un número válido.")
            continue

    #deposito  

        if option == 1:

         try:
            monto = float(input("Ingrese monto a depositar: "))

            if monto <= 0:
                print("Monto invalido.")

            else:
                saldo_anterior = saldo
                saldo += monto

                movimientos.append(f"Deposito: +${monto}")

                print("\n====== COMPROBANTE ======")
                print("Fecha y hora:", fecha_formateada)
                print("Tipo: Deposito")
                print(f"Monto: ${monto}")
                print(f"Saldo anterior: ${saldo_anterior}")
                print(f"Saldo actual: ${saldo}")
                print("Estado: APROBADO")
                


         except ValueError:
          print("Ingrese un numero valido.")  

        
    #retiro          


        elif option == 2:
            try:
                monto = float(input("ingrese monto retirar:" ))
                if monto <= 0:
                   print("monto invalido. ")
                elif monto > saldo:
                    print("fondos insuficientes. ")
                else:
                    saldo -= monto
                    movimientos.append(f"retiro: -${monto}")

                    print("\n==== COMPROBANTRE ====")
                    print("Tipo: retiro")
                    print(f"Monto: ${monto}")
                    print(f"Saldo anterior: ${saldo_anterior}")
                    print(f"saldo actual: ${saldo}")
                    print("Estado: APROBADO")
                    print("==========================")
                    
            except ValueError:
                print("ingrese un numeor valido. ")

    #consultar saldo                           

        elif option == 3:
            print(f"saldo actual: ${saldo}")

    #transferencia           

        elif option == 4:
            clave_ingresada = input("ingrese su clave: ")

            if clave_ingresada != clave:
                print("clave incorrecta.")
            else:
                try:
                 
                    cuenta_destino = input("ingrese cuenta destino: ")

                    if not cuenta_destino.isdigit():
                        print("numero de cuenta invalido")

                    else:
                        monto = float(input("ingrese monto a transferir: "))

                        if monto <= 0:
                            print("monto invalido.")

                        elif monto > saldo: 
                            print("fondos insuficientes")

                        else:
                            saldo -= monto
                            movimientos.append(f"Transferencia a {cuenta_destino}: -${monto}")
                            print("\n==== COMPROBANTE ====")
                            print("Fecha y hora:", fecha_formateada)
                            print("Tipo: transferencia")
                            print(f"Monto: {monto}")
                            print(f"Saldo anterior {saldo_anterior}")
                            print(f"Saldo actual: {saldo}")
                            print("Estado: APROBADO.")
                            print("======================")

                except ValueError:
                    print("ingrese un numero valido.")

        #gestion de clave           

        elif option == 5:
            clave_actual = input("ingrese su clave actual: ")

            if clave_actual != clave:
                print("clave incorrecta.")
            else:
                nueva_clave = input("igrese nueva clave: ") 

                confirmar_clave = input("confirme nueva clave: ")

                if nueva_clave != confirmar_clave:
                   print("las claves no coinciden")

                elif len(nueva_clave) != 4 or not nueva_clave.isdigit():
                   print("la clave debe contener 4 digitos.")

                else:
                   clave = nueva_clave
                   print("Clave actualizada exitosamente.")


        #consultar movimientos      

        elif option == 6:
            if len(movimientos) == 0:
                print("No hay movimientos registrados.")
            else:
                print("\n==== HISTORIAL DE MOVIMIENTOS ====")

                for i, movimiento in enumerate(movimientos, start=1):
                    print(f"{i}. {movimiento}")
                    
 

        #otras operaciones            

        elif option == 7:

            print("\n---PAGOS---")
            print("1. pagar luz")
            print("2. pagar agua")
            print("3. pagar tarjeta de credito")
            print("0. volver")

            try:
                sub_option = int(input("Seleccione una opción: "))

            except ValueError:
                print("Ingrese un número válido.") 
                continue   

            

            if sub_option == 0:
                print("volviendo al menu principal")

            else:
                clave_ingresada = input("ingrese su clave: ")

                if clave_ingresada != clave:
                    print("clave incorrecta.")

                else:
                    try:
                        monto = float(input("ingrese monto a pagar: ")) 

                        if monto <= 0:
                            print("Monto invalido.")

                        elif monto > saldo:
                            print("\n==== COMPROBANTE ====")
                            print("Tipo: Pago servivios")
                            print(f"Monto: ${monto}")
                            print(f"Saldo actual: ${saldo}")
                            print("Estado: RECHAZADO")
                            print("fondos insuficientes.")
                            print("======================")

                        else:
                            saldo_anterior = saldo
                            saldo -= monto

                            if sub_option == 1:
                            
                                movimientos.append(f"pago luz: -${monto}")

                                print("\n====== COMPROBANTE ======")
                                print("Tipo: Pago Luz")
                                print(f"Monto: ${monto}")
                                print(f"Saldo anterior: ${saldo_anterior}")
                                print(f"Saldo actual: ${saldo}")
                                print("Estado: APROBADO")
                                print("=========================")

                            elif sub_option == 2:
                                

                                movimientos.append(f"pago agua: -${monto}")
                                print("\n====== COMPROBANTE ======")
                                print("Tipo: Pago Luz")
                                print(f"Monto: ${monto}")
                                print(f"Saldo anterior: ${saldo_anterior}")
                                print(f"Saldo actual: ${saldo}")
                                print("Estado: APROBADO")
                                print("=========================")
                                
                            elif sub_option == 3:
                                

                                movimientos.append(f"pago tarjeta credito. Nuevo saldo: -${saldo}")
                                print("\n====== COMPROBANTE ======")
                                print("Tipo: Pago Luz")
                                print(f"Monto: ${monto}")
                                print(f"Saldo anterior: ${saldo_anterior}")
                                print(f"Saldo actual: ${saldo}")
                                print("Estado: APROBADO")
                                print("=========================")

                            if sub_option == 0:
                                print("0. volver")


                    except ValueError:
                        print("ingrese un numero valido.")

                    

        elif option == 0:
              print("Gracias por usar el cajero.") 
              break      
                            

            

                        
cajero_automatico()   










            



          
        








  
    






     

                      





                
                        
                        








 




     




 
        
