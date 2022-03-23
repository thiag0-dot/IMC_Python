print('--------------------------------------------------------------------------------')
#Lendo a altura e peso

altura = float(input('Insira sua altura:'))
peso = float(input('Insira seu peso:'))
print('')

#Fazendo o calculo do imc

imc = peso/(altura*altura)

#vendo qual o seu imc

if imc < 18.5 and imc == 18.5 :
    print('CUIDADO! Voce esta abaixo do peso.')
    print('Seu IMC é de: {:.2f}'.format(imc))
elif imc > 18.6 and imc < 24.9 :
    print('Voce esta com o peso normal PARABENS')
    print('Seu IMC é de: {:.2f}'.format(imc))
elif imc > 25 and imc < 29.9 :
    print('CUIDADO! Voce esta com obesidade classe I')
    print('Seu IMC é de: {:.2f}'.format(imc))
elif imc > 35 and imc < 39.9 :
    print('CUIDADO! Voce esta com obesidade classe II')
    print('Seu IMC é de: {:.2f}'.format(imc))
elif imc > 40 :
    print('CUIDADO! Voce esta com obesidade classe III')
    print('Seu IMC é de: {:.2f}'.format(imc))
print('--------------------------------------------------------------------------------')