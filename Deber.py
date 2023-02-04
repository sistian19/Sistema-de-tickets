valorFactura = float(input("¿Cuánto es el valor de la factura?:"))
númeroPersonas = input("¿Cuántas personas son?:")
valorPropina = int(input("Cuánto quiere dar de propina(12, 15 0 20%)?:"))
if (str(valorPropina) == "12"):
    resultado = (valorFactura / int(númeroPersonas)) * 1.12
elif (str(valorPropina) == "15"):
    resultado = (valorFactura / int(númeroPersonas)) * 1.15
elif (str(valorPropina) == "20"):
    resultado = (valorFactura / int(númeroPersonas)) * 1.20

print("su valor a pagar es:", round(resultado,2))



