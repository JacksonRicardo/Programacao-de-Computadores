idade = int(input())
ano = idade / 365
mes = ((idade % 365) / 30)
dias = ((idade % 365) % 30)
print("%d ano(s)" %ano)
print("%d mes(es)" %mes)
print("%d dia(s)" %dias)
