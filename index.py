import time  # Tiempo de ejecucion
import os
'''---------GENERAR COMPROBANTE-------------
--------------------------------------------
type -->Ahorro,Prestamo
name -->Nombre del Usuario
partner -->codigo del socio, si no es socio "no aplica"
date -->fecha de la realizacion
value --> monto
--------------------------------------------
'''


def comprob(type, name, partner, date, value):
  tipo = "   Comprobante de " + str(type)
  nombre = "  Nombre:          |" + str(name)
  socio = "  Socio:           |" + str(partner)
  fecha = "  Fecha:           |" + str(date)
  valor = "  Valor:           |$" + str(value)

  comprobant = [
    "_________________________________", " -----------Banquito----------",
    tipo, "_________________________________", nombre, socio, fecha,
    "_________________________________", valor,
    "_________________________________"
  ]
  for i in range(0, 10, 1):
    print(comprobant[i])


dia = 1
mes = 1
año = 2023

# SOCIO {{INFORMACION},AHORRO TOTAL, ULTIMO AHORRO}
socio = {
  'socio 1': [['Carlos', 123456, 'cuv1'], 25000, 25000],
  'socio 2': [['Camila', 123457, 'cuv2'], 50000, 50000],
  'socio 3': [['Pedro', 123458, 'cuv3'], 150000, 150000],
  'socio 4': [['Lorena', 123459, 'cuv4'], 45000, 45000],
  'socio 5': [['Ana', 123450, 'cuv5'], 25000, 25000]
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
  key = "socio " + str(len(socio) + 1)
  socio[key] = [[], cantidad, cantidad]
  socio[key][0] = [nombre, id, correo]


def Prestamos(tipo, cantidad):
  cuotas = 0
  if tipo == 1:
    num = int(input('Digite el numero del socio: '))
    key = "socio " + str(num)
    montoMax = socio[key][1] * 0.9

    # Si la cantidad a pedir prestada es menor del 90% del total ahorrado del socio
    if (montoMax) >= cantidad:
      print(
        f"El monto maximo que puedes pedir en el prestamo es de: ${montoMax}")
      cuotas = int(input('Digite el numero de cuotas: '))
      # [cuotas faltantes, capital, Costo interes MENSUAL, valor a pagar MENSUAL sin interes,cuotas Totales]   1% mensual
      prest = [cuotas, cantidad, cantidad * 0.01, cantidad / cuotas, cuotas]
      if (prestamosSocios.get(key)) == None:
        prestamosSocios[key] = []
        prestamosSocios[key].append(prest)
      else:
        prestamosSocios[key].append(prest)

    else:
      print("no se puede realizar el prestamo, la cantidad es muy grande.")

  elif tipo == 2:
    id = int(input('Digite el numero del documento de la persona: '))

    if fondoBanco >= cantidad:
      print(
        f"El monto maximo que puedes pedir en el prestamo es de: ${fondoBanco}"
      )
      cuotas = int(input('Digite el numero de cuotas: '))
      key = id
      # [cuotas restantes, capital, Costo interes MENSUAL, valor a pagar MENSUAL sin interes,cuotas Totales]   2% mensual
      prest = [
        cuotas, cantidad, cantidad * 0.02,
        round((cantidad / cuotas), 2), cuotas
      ]
      if (prestamosTerceros.get(id)) == None:
        name = input('Digite el nombre: ')
        email = input('Digite el correo: ')
        personaNatural[key] = [name, email]
        prestamosTerceros[key] = []
        prestamosTerceros[key].append(prest)
      else:
        prestamosTerceros[key].append(prest)
    else:
      print("no se puede realizar el prestamo, la cantidad es muy grande.")

  return cuotas


def Reportes(tipo):
  print("Fonde de Ahorros y Prestamos BANQUITO.LTDA.c\n\
            REPORTES\n")

  if tipo == 1:  #Seleccionar opcion para hacer un reporte del usuario
    opciont = input(
      "Digite la opción correspondiente:\n1.PRESTAMOS\n2.AHORROS\n Opcion: ")
    os.system("clear")
    if opciont == "1":

      print("\nBienvenido, señor(a).")

      buscar_prestamo = int(input("Ingrese su numero de socio: "))
      key = f"socio {buscar_prestamo}"

      if (
          prestamosSocios.get(key)
      ) != None:  #Si la llave es diferente de no existe imprimir el prestamo
        prest = prestamosSocios.get(key)
        print(f"Tiene {len(prest)} prestamos.")
        for k in range(len(prest)):
          # [cuotas restantes, capital, Costo interes MENSUAL, valor a pagar MENSUAL sin interes,cuotas Totales]   2% mensual
          print(f"""_________________________________
            prestamo {k+1}:
            \t Capital:           |{prest[k][1]}
            \t InteresesM:        |{prest[k][2]}
            _________________________________""")

        for i in range(len(prest)):
          cuotas_pagas = prest[i][0] - prest[i][4]
          print(
            f"Tiene hasta el momento {cuotas_pagas} pagadas le restan {prest[i][0]}"
          )  #Reduccion de cuota automatica mensual
      else:
        print("Usted no cuenta con prestamos en el momento")

    elif opciont == "2":  #Reporte de un solo socio o todos los socios del banco
      print("Bienvenido, señor(a).")
      opc_admin = input(
        "\nSeleccione la opción que desea realizar:\n1.Consultar ahorro de un socio\n2.Consultar ahorro de todos los socios\n Opcion: "
      )

      if opc_admin == "1":  #Reporte de un solo socio
        buscar_socio = int(input("Ingrese su numero de socio: "))
        key = f"socio {buscar_socio}"
        Info0 = socio[key][0]

        if (socio.get(key)) != None:
          print(
            f"El socio(a) {Info0[0]} tiene en el momento ${socio[key][1]} en ahorros"
          )
        else:
          print("El codigo que ingreso no pertence a ningun socio")
      elif opc_admin == "2":
        total_ahorros = 0

        for i in range(len(socio)):
          total_ahorros = total_ahorros + socio["socio " + str(i + 1)][1]

        print(f"El total ahorrado de todos los socios es: ${total_ahorros}")
      else:
        os.system("clear")
        print("Opción ingresada no existe. Ingrese una opción válida...\n")
    else:
      print("Opción ingresada no existe. Ingrese una opción válida...")

  elif tipo == 2:

    key = int(input("Ingrese la cedula del usuario: "))

    if (prestamosTerceros.get(key)) != None:
      prest = prestamosTerceros.get(key)
      print(f"Tiene {len(prest)} prestamos.")

      for k in range(len(prest)):
        # [cuotas restantes, capital, Costo interes MENSUAL, valor a pagar MENSUAL sin interes,cuotas Totales]   2% mensual
        print(f"""_________________________________
            prestamo {k+1}:
            \t Capital:           |{prest[k][1]}
            \t InteresesM:        |{prest[k][2]}
            _________________________________""")

      for i in range(len(prest)):
        cuotas_pagas = prest[i][0] - prest[i][4]
        print(
          f"Tiene hasta el momento {cuotas_pagas} pagadas le restan {prest[i][0]}"
        )
    else:
      print("Usted no cuenta con prestamos en el momento")


sociosTemporal = []
personasTemporal = []

while True:

  fecha = f"{dia}/{mes}/{año}"
  print('fondo actual: ', fondoBanco)
  #GENERARCOMPROBANTES
  #comprobantes de ahorro
  for i in range(len(socio)):
    sociosTemporal = socio.get(f"socio {i+1}")[0]
    comprob("Ahorro", sociosTemporal[0], i + 1, fecha,
            socio[f"socio {i+1}"][2])

#comprobantes de prestamos
  for i in prestamosSocios:
    # [cuotas, capital, Costo interes MENSUAL, valor a pagar MENSUAL sin interes]   1% mensual
    prest = prestamosSocios[i]
    sociosTemporal = socio.get(i)[0]
    for j in range(len(prest)):
      comprob("Prestamos", sociosTemporal[0], i, fecha, prest[j][1])

  for i in prestamosTerceros:
    # [cuotas, capital, Costo interes MENSUAL, valor a pagar MENSUAL sin interes]   1% mensual
    prest = prestamosTerceros[i]
    for j in range(len(prest)):
      comprob("Prestamos", personaNatural[i][0], i, fecha, prest[j][1])

  print(f"FECHA: {fecha}")
  opcion = int(
    input("""Seleccione una opción
    \t1. -> Registrar Socio.
    \t2. -> Prestar.
    \t3. -> Ganancias.
    \t4. -> Realizar un reporte.
    \t5. -> Terminar proceso.
    \t6. -> Apagar.
    Opción: """))

  if opcion == 1:
    name = input('Digite el nombre del socio: ')
    ced = int(input('Digite la cedula del socio: '))
    email = input('Digite el correo del socio: ')
    cand0 = int(
      input(
        """Digite cuanto dinero ahorrará, teniendo en cuenta que la cantidad minima es $25000:
                    \t Cantidad: $"""))

    #Verificar si el socio existe
    info = [name, ced, email]
    Booleano = True
    for key in socio:
      if (socio[key][0]) == info:
        Booleano = False

    if Booleano:
      RegistrarSocio(name, ced, email, cand0)
      fondoBanco = fondoBanco + cand0
    else:
      print(
        'El socio ya existe no es posible registrarlo, intente de nuevo ingresar la información'
      )
  elif opcion == 2:
    op = int(
      input("""Seleccione una opción:
        1 -> para un socio.
        2 -> para un tercero.
        : """))

    cand = int(input('Digite la cantidad a prestar: '))
    cu = Prestamos(op, cand)

    if cu > 0:
      fondoBanco = fondoBanco - cand  #Reducir la cantidad del banco menos el prestamo
    else:
      print('no se logro realizar el prestamo.')

  elif opcion == 3:
    op = int(
      input("""Digite la opción a obtener:
      \t1. Ganacias actuales.
      \t2. Proyección de ganancias.
      Opcion: """))
    if op == 1:
      print(f"Las ganancias actuales son de ${ganancias}")
    elif op == 2:
      suma = 0
      for i in prestamosSocios:
        prest = prestamosSocios[i]
        for j in range(len(prest)):
          #valorPorPersona = CostoInteresMensual*CuotasFaltantes
          valorPorPersona = prest[j][2] * prest[j][0]
          suma = suma + valorPorPersona
      for j in prestamosTerceros:
        prest = prestamosTerceros[j]
        for k in range(len(prest)):
          #valorPorPersona = CostoInteresMensual*CuotasFaltantes
          valorPorPersona = prest[k][2] * prest[k][0]
          suma = suma + valorPorPersona
      print(f"La proyección de las ganancias son de ${suma}")
  elif opcion == 4:
    op = int(
      input("""Seleccione una opción:
        1 -> para un socio.
        2 -> para un tercero.
        Opcion: """))
    os.system('clear')
    Reportes(op)

  elif opcion == 5:
    #CAMBIO DE FECHA
    if mes < 12:
      mes = mes + 1
    else:
      mes = 1
      año = año + 1

  #Consignaciones automaticas y calculo de fondo
    for i in range(len(socio)):
      socio[f"socio {i + 1}"][
        1] = socio[f"socio {i + 1}"][1] + socio[f"socio {i + 1}"][2]
      fondoBanco = fondoBanco + socio[f"socio {i + 1}"][2]

    #PAGOS PROGRAMADOS DE PRESTAMOS
    # para restar valor de cuota (se va restando del valor del prestamo y se le suma al fondo)
    for i in prestamosSocios:  #PARA SOCIOS
      prestAuxi = prestamosSocios[i]

      #[cuotas, capital, Costo interes MENSUAL, valor a pagar MENSUAL sin interes]
      # OPERACIONES POR ELEMENTOS
      for j in range(len(prestAuxi)):
        prestAuxi[j][0] = prestAuxi[j][0] - 1  # Resto 1 cuota pagada
        prestAuxi[j][1] = prestAuxi[j][1] - prestAuxi[j][
          3]  # CapitalAPagar = CapitalAPagar - ValorAPagarMensual
        fondoBanco = fondoBanco + prestAuxi[j][
          3]  #FondoBanco = FondoBanco + ValorAPagarMensual
        ganancias = ganancias + prestAuxi[j][
          2]  # Ganancias = Ganancias + costoInteresMensual

      # ELIMINAR PRESTAMOS TERMINADOS
      for k in range(len(prestAuxi)):
        if (prestAuxi[k][0]) == 0:
          prestAuxi.pop(k)

      prestamosSocios[i] = prestAuxi

    for i in prestamosTerceros:  #PARA  TERCEROS
      prestAuxi = prestamosTerceros[i]

      # OPERACIONES POR ELEMENTOS
      for j in range(len(prestAuxi)):
        prestAuxi[j][0] = prestAuxi[j][0] - 1  # Resto 1 cuota pagada
        prestAuxi[j][1] = prestAuxi[j][1] - prestAuxi[j][
          3]  # CapitalAPagar = CapitalAPagar - ValorAPagarMensual
        fondoBanco = fondoBanco + prestAuxi[j][
          3]  #FondoBanco = FondoBanco + ValorAPagarMensual
        ganancias = ganancias + prestAuxi[j][
          2]  # Ganancias = Ganancias + costoInteresMensual

      # ELIMINAR PRESTAMOS TERMINADOS
      for k in range(len(prestAuxi)):
        if (prestAuxi[k][0]) == 0:
          prestAuxi.pop(k)

      prestamosTerceros[i] = prestAuxi

  elif opcion == 6:  #Apagar el proceso del banco
    break
  else:  #Si se selecciona una opcion diferente
    print("Ha ocurrido un error, digite de nuevo la opción. Por favor.")

  print("En espera para volver al menu")
  time.sleep(3)

