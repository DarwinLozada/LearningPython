monto_inicial = int(input("Dime el monto inicial"))
meses = int(input("Dime la cantidad de meses"))

for i in range(meses):
    monto_inicial *= 1.10

print(monto_inicial)
