valor_aplicacao = 100
qtde_aplicada_por_mes = 5
deposito_por_mes = valor_aplicacao * qtde_aplicada_por_mes
total_meses = 60
taxa_mensal = 0.005 #0.5% -> 0.5 / 100
valor_atual = 0
total_rendimentos = 0

for i in range(1,total_meses+1):
    rendimentos = valor_atual * taxa_mensal
    total_rendimentos += rendimentos

    if(total_rendimentos >= valor_aplicacao):
        qtde_comprada_com_rendimentos = total_rendimentos // valor_aplicacao
        total_rendimentos -= valor_aplicacao * qtde_comprada_com_rendimentos
        valor_atual += deposito_por_mes + qtde_comprada_com_rendimentos * valor_aplicacao
    else:
        valor_atual += deposito_por_mes

    print("MES: {} | TOTAL: R${:.2f} | RENDIMENTOS: R${:.2f} | TOTAL RENDIMENTOS: R${:.2f}".format(i,valor_atual,rendimentos,total_rendimentos))