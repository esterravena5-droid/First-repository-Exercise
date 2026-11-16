def classificar_latencia(latencia):
    if latencia <= 50:
        return "Boa"
    else:
        return "Rever ligação"


latencia = int(input("Latência em ms: "))

resultado = classificar_latencia(latencia)

print(resultado)