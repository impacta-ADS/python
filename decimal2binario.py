'''
    TRANSFORMAR BINÁRIO EM DECIMAL

'''
continuar=True
contador=0
numeroDecimal=0
while continuar:
    numeroBinario=int(input("Digite um número binario:"))
    numeroBinarioInicial=numeroBinario
    if numeroBinario>0:
        continuar=False
while (numeroBinario!=0):
    resto=numeroBinario%10
    numeroDecimal=numeroDecimal+resto*(2**contador)
    numeroBinario=numeroBinario//10
    contador+=1
    
print(f"O número binário {numeroBinarioInicial} é igual a {numeroDecimal} em base decimal")
