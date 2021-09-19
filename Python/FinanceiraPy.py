import math
from decimal import Decimal
import numpy as np
import pandas as pd

QTD_DIGITOS = 2

#############
###
#############

def FVsimples(PV, i, n):
    PV = Decimal(str(PV))
    i = Decimal(str(i))
    n = Decimal(str(n))
    return PV * (1 + i*n)

def PVsimples(FV, i, n):
    FV = Decimal(str(FV))
    i = Decimal(str(i))
    n = Decimal(str(n))
    return FV / (1 + i*n)

def N_simples(FV, PV, i):
    PV = Decimal(str(PV))
    FV = Decimal(str(FV))
    i = Decimal(str(i))
    return ((FV / PV) - 1)/i

def I_simples(FV, PV, n, digitos=5):
    PV = Decimal(str(PV))
    FV = Decimal(str(FV))
    n = Decimal(str(n))
    i = ((FV / PV) - 1)/n
    i = i.quantize(Decimal(str(10 ** -digitos)))
    return i

def FVcomposto(PV, i, n):
    PV = Decimal(str(PV))
    i = Decimal(str(i))
    n = Decimal(str(n))
    return PV * ( (1 + i) ** n)

def PVcomposto(FV, i, n):
    FV = Decimal(str(FV))
    i = Decimal(str(i))
    n = Decimal(str(n))
    return FV * ( 1 / ( (1 + i) ** n) )

def N_composto(FV, PV, i):
    PV = Decimal(str(PV))
    FV = Decimal(str(FV))
    i = Decimal(str(i))
    return Decimal.log10(FV/PV) / Decimal.log10(1 + i)

def I_composto(FV, PV, n, digitos=5):
    PV = Decimal(str(PV))
    FV = Decimal(str(FV))
    n = Decimal(str(n))
    i = (FV/PV) ** (1/n) - 1
    i = i.quantize(Decimal(str(10 ** -digitos)))
    return i

def imprimeFVsimples(PV, i, n):
    PV = Decimal(str(PV))
    i = Decimal(str(i))
    n = round(abs(n))
    parc = PV * i
    aux = PV + parc
    print("-----")
    print("Valores por período: (Opção: Juros Simples)")
    print("---")
    print("Valor Inicial: ${}".format(PV))
    for idx in range(1, n+1):
        print("Perido {}: ${}".format(idx, aux))
        aux = aux + parc
    print("-----")
    
def imprimeFVcomposto(PV, i, n):
    PV = Decimal(str(PV))
    i = Decimal(str(i))
    n = round(abs(n))
    aux = PV * (1+i)
    print("-----")
    print("Valores por período: (Opção: Juros Compostos)")
    print("---")
    print("Valor Inicial: ${}".format(PV))
    for idx in range(1, n+1):
        print("Perido {}: ${}".format(idx, aux))
        aux = aux * (1+i)
    print("-----")







def PVparcelas(PMT, i, n):
    PMT = Decimal(str(PMT))
    i = Decimal(str(i))
    n = Decimal(str(n))
    aux = (1+i) ** n
    return PMT * (  (aux - 1)/(i * aux)  )

def FVparcelas(PMT, i, n):
    PMT = Decimal(str(PMT))
    i = Decimal(str(i))
    n = Decimal(str(n))
    aux = (1+i) ** n
    return PMT * (  ( (1+i) ** n - 1 ) / i  )

def PMT_PV_parcelas(PV, i, n):
    PV = Decimal(str(PV))
    i = Decimal(str(i))
    n = Decimal(str(n))
    aux = (1+i) ** n
    return PV * (  (i * aux) / (aux - 1)  )

def PMT_FV_parcelas(FV, i, n):
    FV = Decimal(str(FV))
    i = Decimal(str(i))
    n = Decimal(str(n))
    return FV * (  i / ( (1+i) ** n - 1)  )









def tabelaAMERICANO(PV, i, n, digitos=QTD_DIGITOS):
    PV = Decimal(str(PV))
    i = Decimal(str(i))
    n = round(abs(n))
    aux = Decimal(str(i * PV))
    juros = [aux]
    prestacoes = [aux]
    juros = juros * (n+1)
    prestacoes = prestacoes * (n+1)
    juros[0] = Decimal(str(0))
    prestacoes[0] = Decimal(str(0))
    prestacoes[n] = PV + aux
    saldo_devedor = [PV] * (n+1)
    saldo_devedor[n] = Decimal(str(0))
    amortizacao = [Decimal(str(0))] * (n+1)
    amortizacao[n] = PV
    tabela = gerarTabela(juros, amortizacao, prestacoes, saldo_devedor, digitos)
    return tabela

def tabelaPRICE(PV, i, n, digitos=QTD_DIGITOS):
    n = round(abs(n))
    prestacoes = [PMT_PV_parcelas(PV, i, n)]
    PV = Decimal(str(PV))
    i = Decimal(str(i))
    prestacoes = prestacoes * (n+1)
    prestacoes[0] = Decimal(str(0))
    saldo_devedor = [PV]
    juros = [Decimal(str(0))]
    amortizacao = [Decimal(str(0))]
    for k in range(1, n+1):
        juros.append(i * saldo_devedor[k-1])
        amortizacao.append(prestacoes[k] - juros[k])
        saldo_devedor.append(saldo_devedor[k-1] - amortizacao[k])
    tabela = gerarTabela(juros, amortizacao, prestacoes, saldo_devedor, digitos)
    return tabela

def tabelaSAC(PV, i, n, digitos=QTD_DIGITOS):
    PV = Decimal(str(PV))
    i = Decimal(str(i))
    n = round(abs(n))
    amortizacao = [PV/n]
    amortizacao = amortizacao * (n+1)
    amortizacao[0] = Decimal(str(0))
    saldo_devedor = [PV]
    juros = [Decimal(str(0))]
    prestacoes = [Decimal(str(0))]
    for k in range(1, n+1):
        juros.append(i * saldo_devedor[k-1])
        prestacoes.append(amortizacao[k] + juros[k])
        saldo_devedor.append(saldo_devedor[k-1] - amortizacao[k])
    tabela = gerarTabela(juros, amortizacao, prestacoes, saldo_devedor, digitos)
    return tabela

def gerarTabela(p_juros, p_amortizacao, p_prestacoes, p_saldo_devedor, digitos=QTD_DIGITOS):
    n = len(p_juros)
    indices = list(range(n))
    indices.append('Total')
    tabela = pd.DataFrame()
    juros = pd.Series(p_juros)
    amortizacao = pd.Series(p_amortizacao)
    prestacoes = pd.Series(p_prestacoes)
    saldo_devedor = pd.Series(p_saldo_devedor)

    juros = juros.apply(lambda x: x.quantize(Decimal(str(10 ** -digitos))))
    amortizacao = amortizacao.apply(lambda x: x.quantize(Decimal(str(10 ** -digitos))))
    prestacoes = prestacoes.apply(lambda x: x.quantize(Decimal(str(10 ** -digitos))))
    saldo_devedor = saldo_devedor.apply(lambda x: x.quantize(Decimal(str(10 ** -digitos))))
 
    juros = juros.append(pd.Series(juros.sum()))
    amortizacao = amortizacao.append(pd.Series(amortizacao.sum()))
    prestacoes = prestacoes.append(pd.Series(prestacoes.sum()))
    saldo_devedor = saldo_devedor.append(
        pd.Series(Decimal(p_saldo_devedor[-1]).quantize(Decimal(str(10 ** -digitos)))))

    tabela['Juros'] = juros
    tabela['Amortização'] = amortizacao
    tabela['Prestação'] = prestacoes
    tabela['Saldo Devedor'] = saldo_devedor
    tabela = tabela.applymap(lambda x: '$ {}'.format(x))
    tabela.index = indices
    
    return tabela