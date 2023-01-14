import time #tiempo de ejecucion

'''---------GENERAR COMPROBANTE-------------
--------------------------------------------
type -->Ahorro,Prestamo
name -->Nombre del Usuario
partner -->codigo del socio, si no es socio "no aplica"
date -->fecha de la realizacion
value --> monto
--------------------------------------------
'''

def comprob(type,name,partner,date,value):
  tipo="   Comprobante de "+str(type)
  nombre="  Nombre:          |"+str(name)
  socio="  Socio:           |"+str(partner)
  fecha="  Fecha:           |"+str(date)
  valor="  Valor:           |$"+str(value)

  comprobant=["_________________________________",
               " -----------Banquito----------",
              tipo,
               "_________________________________",
               nombre,socio,fecha,
               "_________________________________",
               valor,
               "_________________________________"]
  for i in range(0,10,1):
    print(comprobant[i])


'''---------OBTENER FECHA-------------
--------------------------------------------
day -->dia del mes
month -->mes del año
year -->año
--------------------------------------------
'''
'''
day=int(input("ingresa el dia: "))
month=int(input("ingresa el mes: "))
year=int(input("ingresa el año: "))


dia=day
mes=month
anio=year

while(True):
  fecha=str(dia)+"-"+str(mes)+"-"+str(anio)
  comprob("Ahorro","Jose","no aplica",fecha,"25000")


  if(dia<30):
    dia=dia+1
  else:
    dia=1
    if(mes<12):
      mes=mes+1
    else:
      mes=1
      anio=anio+1

  #print(fecha)
  time.sleep(0.5)#esperar 1 segundo

'''

dia = 1
mes = 1
año = 2023

# SOCIO {{INFORMACION},AHORRO TOTAL, ULTIMO AHORRO}
socio = {
    'socio 1': [['Carlos',123456, 'cuv1'], 25000, 25000],
    'socio 2': [['Camila',123457, 'cuv2'], 50000, 50000],
    'socio 3': [['Pedro',123458, 'cuv3'], 150000, 150000],
    'socio 4': [['Lorena',123459, 'cuv4'], 45000, 45000],
    'socio 5': [['Ana',123450, 'cuv5'], 25000, 25000]
}
# PERSONA NATURAL {{INFORMACION}}
personaNatural = {}
#[PRESTAMOS]
# prestamosSocios [cuotas, capital, Costo interes MENSUAL, valor a pagar MENSUAL sin interes]   1% mensual
prestamosSocios = {}
prestamosTerceros = {}

#print(socio)

#hay que tener en cuenta que aunque sea la suma de los ahorros, no se le puede descontar a el ahorra, queda en deuda
fondoBanco = 0
ganancias = 0
for i in range(len(socio)):
    fondoBanco = fondoBanco + socio["socio " + str(i + 1)][1]

#FUNCIONES: REGISTRO, AHORRO, PRESTAMOS, REPORTES

def RegistrarSocio(nombre, id, correo, cantidad):
    key = "socio " + str(len(socio)+1)
    socio[key] = [[],cantidad, cantidad]
    socio[key][0] = [nombre, id, correo]
    print(socio[key])

#####
'''
def CambiarAhorro(num, cantidad):
    key = "socio " + str(num)
    (socio[key][2]).append(cantidad)
'''

def Prestamos(tipo, cantidad):
    cuotas = 0
    if tipo == 1:
        num = int(input('Digite el numero del socio: '))
        key = "socio " + str(num)
        montoMax = socio[key][1] * 0.9

        # Si la cantidad a pedir pretada es menor del 90% del total ahorrado del socio
        if (montoMax)>= cantidad:
            print(f"El monto maximo que puedes pedir en el prestamo es de: ${montoMax}")
            cuotas = int(input('Digite el numero de cuotas: '))
            # [cuotas, capital, Costo interes MENSUAL, valor a pagar MENSUAL sin interes]   1% mensual
            prest = [cuotas,cantidad,cantidad*0.01,cantidad/cuotas]
            if (prestamosSocios.get(key)) == None:
                prestamosSocios[key]=[]
                prestamosSocios[key].append(prest)
            else:
                prestamosSocios[key].append(prest)

            print(prestamosSocios[key])
        else:
            print("no se puede realizar el prestamo, la cantidad es muy grande.")

    elif tipo == 2:
        id = int(input('Digite el numero del documento de la persona: '))

        if fondoBanco >= cantidad:
            print(f"El monto maximo que puedes pedir en el prestamo es de: ${fondoBanco}")
            cuotas = int(input('Digite el numero de cuotas: '))
            key = id
            # [cuotas, capital, Costo interes MENSUAL, valor a pagar MENSUAL sin interes]   2% mensual
            prest = [cuotas, cantidad, cantidad * 0.02, cantidad / cuotas]
            if (prestamosTerceros.get(id)) == None:
                name = input('Digite el nombre: ')
                email = input('Digite el correo: ')
                personaNatural[key] = {name, email}
                prestamosTerceros[key] = []
                prestamosTerceros[key].append(prest)
            else:
                prestamosTerceros[key].append(prest)

                print(prestamosTerceros[key])
                print(personaNatural[key])
        else:
            print("no se puede realizar el prestamo, la cantidad es muy grande.")

    return cuotas

sociosTemporal = []
personasTemporal = []

while True:
    fecha = f"{dia}/{mes}/{año}"
    print('fondo actual: ', fondoBanco)
    #GENERARCOMPROBANTES
    #comprobantes de ahorro
    for i in range(len(socio)):
        sociosTemporal = socio.get(f"socio {i+1}")[0]
        comprob("Ahorro",sociosTemporal[0],i+1,fecha,socio[f"socio {i+1}"][2])
    #comprobantes de prestamos


    print(f"FECHA: {fecha}")
    opcion = int(input("""Seleccione una opción
    \t1. -> Registrar Socio.
    \t2. -> Prestar.
    \t3. -> Realizar un reporte.
    \t4. -> Terminar proceso.
    \t5. -> Apagar.
    Opción: """))

    if opcion == 1:
        name = input('Digite el nombre del socio: ')
        ced = int(input('Digite la cedula del socio: '))
        email = input('Digite el correo del socio: ')
        cand0 = int(input("""Digite cuanto dinero ahorrará, teniendo en cuenta que la cantidad minima es $25000:
                    \t Cantidad: $"""))

        info = [name,ced,email]

        if (socio.get(info))==None:
            RegistrarSocio(name, ced, email, cand0)
        else:
            print('El socio ya existe no es posible registrarlo, intente de nuevo ingresar la información')
    elif opcion == 2:
        op = int(input("""Seleccione una opción:
        1 -> para un socio.
        2 -> para un tercero."""))

        cand = int(input('Digite la cantidad a prestar: '))
        cu = Prestamos(op, cand)

        if cu>0:
            fondoBanco = fondoBanco - cand
        else:
            print('no se logro realizar el prestamo.')

    elif opcion == 3:
        print("se selecciono 3")

    elif opcion == 4:
    #CAMBIO DE FECHA
        if mes<12:
            mes=mes+1
        else:
            mes=1
            año=año+1

    #Consignaciones automaticas y calculo de fondo
        for i in range(len(socio)):
            socio[f"socio {i + 1}"][1] = socio[f"socio {i + 1}"][1] + socio[f"socio {i + 1}"][2]
            fondoBanco = fondoBanco + socio[f"socio {i + 1}"][2]


        #PAGOS PROGRAMADOS DE PRESTAMOS
        # para restar valor de cuota (se va restando del valor del prestamo y se le suma al fondo)
        for i in prestamosSocios: #PARA SOCIOS
            prestAuxi = prestamosSocios[i]


            #[cuotas, capital, Costo interes MENSUAL, valor a pagar MENSUAL sin interes]
            # OPERACIONES POR ELEMENTOS
            for j in range(len(prestAuxi)):
                prestAuxi[j][0] = prestAuxi[j][0] - 1  # Resto 1 cuota pagada
                prestAuxi[j][1] = prestAuxi[j][1] - prestAuxi[j][3]  # CapitalAPagar = CapitalAPagar - ValorAPagarMensual
                fondoBanco = fondoBanco + prestAuxi[j][3] #FondoBanco = FondoBanco + ValorAPagarMensual
                ganancias = ganancias + prestAuxi[j][2] # Ganancias = Ganancias + costoInteresMensual

            # ELIMINAR PRESTAMOS TERMINADOS
            for k in range(len(prestAuxi)):
                if (prestAuxi[k][0]) == 0:
                    prestAuxi.pop(k)

            prestamosSocios[i] = prestAuxi

        for i in prestamosTerceros: #PARA  TERCEROS
            prestAuxi = prestamosTerceros[i]

            # OPERACIONES POR ELEMENTOS
            for j in range(len(prestAuxi)):
                prestAuxi[j][0] = prestAuxi[j][0] - 1  # Resto 1 cuota pagada
                prestAuxi[j][1] = prestAuxi[j][1] - prestAuxi[j][3]  # CapitalAPagar = CapitalAPagar - ValorAPagarMensual
                fondoBanco = fondoBanco + prestAuxi[j][3] #FondoBanco = FondoBanco + ValorAPagarMensual
                ganancias = ganancias + prestAuxi[j][2] # Ganancias = Ganancias + costoInteresMensual

            # ELIMINAR PRESTAMOS TERMINADOS
            for k in range(len(prestAuxi)):
                if (prestAuxi[k][0]) == 0:
                    prestAuxi.pop(k)

            prestamosTerceros[i] = prestAuxi

    elif opcion == 5:
        break
    else:
        print("Ha ocurrido un error, digite de nuevo la opción. Por favor.")

    print("En espera para volver al menu")
    time.sleep(5)
