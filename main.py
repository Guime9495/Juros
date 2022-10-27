#!/usr/bin/env python


from pandas import DataFrame
from os import system
resumo = []
temp = {}
amort = 0
juros = 0
taxa = 0
pv = 0

system('clear')
def textoBonito(texto):
    print(len(texto) * "=")
    print(texto)
    print(len(texto) * "=")


def periodo(pv, fv, i):
    from math import log
    n = log(fv/pv)/log(1+i)
    return n


def parcela(pv, i, n):
    pmt = (pv * i) / (1 - (1 + i) ** -n)
    return pmt


def salvar(dataframe):
    from os import getcwd
    from datetime import datetime
    while True:
        print("""Qual extensão você quer? 
        1) CSV - Texto separado por vírgulas
        2) XLSX - Arquivo para Excel
        0) Encerrar""")
        res = ' '
        res = input('Escolha uma opção: ').strip()
        if res not in '1230':
            print('Opção inválida...')
        elif res == '1':
            file = f'{datetime.now()}.csv'
            price.to_csv(file)
            print(f'Arquivo salvo em {getcwd()}/{datetime.now()}.csv')
        elif res == '2':
            file = f'{datetime.now()}.xlsx'
            price.to_excel(file)
            print(f'Arquivo salvo em {getcwd()}/{datetime.now()}.xlsx')
        elif res == '0':
            print('Finalizando...')
            break


while True:
    try:
        pv = float(input('Qual o valor do emprestimo? '))
    except ValueError:
        print('Você deve inserir um valor válido')
    if pv > 0:
        break

try:
    n = int(input('Por quanto tempo em meses? '))
except ValueError:
        print('Como não foi informado o tempo do empréstimo então será necessário que seja informado o valor final, '
              'já acrescido de juros para podermos continuar.')
        while True:
            try:
                taxa = float(input('A qual taxa de juros? ex: 2.09 '))
                if taxa > 1:
                    taxa /= 100
                    break
                elif taxa <= 0:
                    print('Insira um valor válido')
                else:
                    break
            except ValueError:
                print('Insira um valor válido')
        while True:
            try:
                fv = float(input('Qual o valor final? '))
                if fv > 0:
                    break
            except ValueError:
                print('Insira um valor válido')
        n = int(periodo(pv, fv, taxa))
        print(f'Será usado o valor de {n} períodos para o cálculo')

while True:
    try:
        taxa = float(input('Qual a taxa de juros? ex:2.09 ').replace('%', ''))
        if taxa > 1:
            taxa /= 100
            break
        elif taxa <= 0:
            print('Insira um valor válido')
        else:
            break
    except (ZeroDivisionError, ValueError, NameError):
        print('Insira um valor válido')

pmt = parcela(pv, taxa, n)


for i in range(0, n):
    if i == 0:
        temp['Juros'] = 0
        temp['Amortização'] = 0
        temp['Saldo Devedor'] = pv
        temp['Parcela'] = 0
        temp['Período'] = 0
        resumo.append(temp.copy())
    juros = pv * taxa
    amort = pmt - juros
    pv = pv - amort
    #per += 1
    temp['Juros'] = juros
    temp['Amortização'] = amort
    temp['Saldo Devedor'] = pv
    temp['Parcela'] = pmt
    temp['Período'] = i + 1
    resumo.append(temp.copy())

price = DataFrame(resumo).round()[['Período', 'Parcela', 'Juros', 'Amortização', 'Saldo Devedor']]
textoBonito(f'{"_Tabela Price_ Guilherme Ribeiro":^55}')
print(price)
salvar(price)