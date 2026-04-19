
tipo_moneda=int(input("Tipo de Moneda(1: bolivares, 2: dolares): "))
if tipo_moneda not in (1,2):
    print("Error: Presione solo 1 o 2 para seleccionar el tipo de moneda")
    exit()
tipo_cuenta = int(input("Tipo de Cuenta (1: Ahorro, 2: Corriente): "))
if tipo_cuenta not in (1,2):
    print("Error: Presione solo 1 o 2 para seleccionar el tipo de cuenta.")
    exit()  
if tipo_cuenta == 1 and tipo_moneda == 1:
    print("cuenta ahorro de bolivares")
   
elif tipo_cuenta == 1 and tipo_moneda == 2:
    print ("cuenta corriente de bolivares")
   
elif tipo_cuenta == 2 and tipo_moneda == 1:
    print("cuenta ahorro de dolares")
   
elif tipo_cuenta == 2 and tipo_moneda == 2:
    print("cuenta corriente de dolares")
    
maximo_retiro_bolivares = 10000
maximo_retiro_dolares = 100
if tipo_cuenta == 2:
    print("Se infomra al usuario que los retiros por cuenta corriente tienen una comision del 5%")

Cantidad_disponible = [1000, 10, 20, 50, 100]
if tipo_moneda == 1:
    print ("monto maximo para rertiro: 10000 bolivares")
elif tipo_moneda == 2:
    print ("montos disponibles por rertiro: 10,20,50,100")

retiro = int (input("ingrese el monto a retirar:"))
if tipo_moneda == 2 and retiro < 0:
    print("Error: Transacción denegada, monto no puede ser negativo")
if retiro % 10 != 0:
    print("Error: cantidad invalida, la cantidad debe ajustarse a los billetes disponibles")
    exit()
elif tipo_moneda == 2 and retiro > 100:
    print("Error: se excede monto permitido para retiro en dolares")
    exit()
else: retiro > 0 <= 100
print ("Validando transaccion... estamos contando su dinero")

if tipo_moneda == 1 and retiro <0:
    print("Error transaccion denegada, saldo no puede ser negativo")
elif tipo_moneda == 1 and retiro > 10000:
    print("error transaccion denegada, excede monto maximo para bolivares")
    exit()
if retiro % 10 != 0:
    print("Error: monto no es valido con las demonicaciones disponibles")
    exit()
else: tipo_moneda == 1 and retiro > 0 <= 10000
print("Espere un momento..")

resto = retiro
billetes_10 = resto // 10
resto %= 10
billetes_20 = resto // 20
resto %= 20
billetes_50 = resto // 50
resto %= 50
billetes_100 = resto // 100
resto %= 100

if tipo_cuenta == 2:
    comision = retiro * 0.05
else:
    comision = 0

total = retiro + comision

match tipo_moneda, tipo_cuenta:
    case 1,1: 
        print("/n desglose de monto total y cantidad de billetes a entregar")
        print(f"billetes de 10: {billetes_10}")
        print(f"billetes de 20: {billetes_20}")
        print(f"billetes de 50: {billetes_50}")
        print(f"billetes de 100: {billetes_100}")
        print(f"total a retirar: {retiro} bolivares")   
    case 1,2: 
        print("/n desglose de monto total y cantidad de billetes a entregar")
        print(f"billetes de 10: {billetes_10}")
        print(f"billetes de 20: {billetes_20}")
        print(f"billetes de 50: {billetes_50}")
        print(f"billetes de 100: {billetes_100}")
        print(f"Total a retirar: {retiro + comision} bolivares")  
    case 2,1:
        print("/n desglose de monto total y cantidad de billetes a entregar")
        print(f"billetes de 10: {billetes_10}")
        print(f"billetes de 20: {billetes_20}")
        print(f"billetes de 50: {billetes_50}")
        print(f"billetes de 100: {billetes_100}")
        print(f"total a retirar: {retiro} dolares")
    case 2,2:
        print("/n desglose de monto total y cantidad de billetes a entregar")
        print(f"billetes de 10: {billetes_10}")
        print(f"billetes de 20: {billetes_20}")
        print(f"billetes de 50: {billetes_50}")
        print(f"billetes de 100: {billetes_100}")
        print(f"total a retirar: {retiro + comision} dolares")
        
exit("Transaccion completada, gracias por usar nuestros servicio")




    



    

    







    
    
    

