pedidos = 0      # contador de pedidos válidos 
urgentes = 0     # contador de pedidos com prioridade 1 ou 2 
total = 0        # totalizador de minutos 
maior = 0        # maior tempo estimado 
 
# 2. Ciclo: só termina quando houver 10 pedidos válidos 
while pedidos < 10: 
    # 3. Entrada (se escrever texto em vez de número, trata como inválido) 
    try: 
        prioridade = int(input("Prioridade (1 a 5): ")) 
        tempo = float(input("Tempo estimado (min): ")) 
    except ValueError: 
        print("Dados inválidos, tente novamente") 
        continue 
 
    # 4. Validação: prioridade fora de 1-5 OU tempo <= 0 
    if prioridade < 1 or prioridade > 5 or tempo <= 0: 
        print("Dados inválidos, tente novamente") 
    else: 
        # 5. Pedido válido: só agora o contador avança 
        pedidos += 1 
 
        # 6. Regra de urgente: prioridade 1 OU 2 
        if prioridade == 1 or prioridade == 2: 
            urgentes += 1 
 
        # 7. Totalizador e máximo 
        total += tempo 
        if tempo > maior: 
            maior = tempo 
 
# 8. Média, calculada depois da recolha 
media = total / 10 
 
# 9. Classificação: CRÍTICA primeiro, depois ELEVADA, depois NORMAL 
if urgentes >= 5 or total > 600: 
    classe = "CRÍTICA" 
elif urgentes >= 3 or total > 480: 
    classe = "ELEVADA" 
else: 
    classe = "NORMAL" 
 
# 10. Resultados 
print("Urgentes:", urgentes) 
print("Total de minutos:", total) 
print("Média:", media) 
print("Maior estimativa:", maior) 
print("Classificação:", classe) 
