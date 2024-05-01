from datetime import date
nasc = int(input("Digite o seu ano de nascimento: "))
sexo = str(input("Digite o seu sexo (MASCULINO/FEMININO): ")).strip().upper()
ano_atual = date.today().year
idade = ano_atual - nasc
if sexo == "FEMININO".upper():
    print("Mulheres Não precisam fazer o alistamento militar")
else:
    if idade < 18:
        saldo = 18 - idade
        print("Voce ainda não completou 18 anos. ainda faltam {} anos para o seu alistamento".format(saldo))
        ano = ano_atual + saldo
        print("Seu alistamento sera em {} ano".format(ano))
    elif idade == 18:
        print("Voce deve se alistar IMEDIATAMENTE")
    else:
        saldo1 = idade - 18
        print("Voce ja deveria ter se alistado há {} anos.".format(saldo1))
        ano = ano_atual - saldo1
        print("Seu alistamento deveria ter sido no ano de {}".format(ano))