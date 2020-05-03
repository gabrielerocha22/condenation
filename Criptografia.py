alfabeto="abcdefghijklmnopqrstuvxwyz"
numero_casa = 3

def criptografia (mensagem):
    m = ""
    for c in mensagem:
        if c in alfabeto:
            index = alfabeto.index (c)
            alfabeto[index + numero_casa]
            m += alfabeto[(index + numero_casa % len (alfabeto))] 
        else:
            m += c
    return m 

def descriptografia (mensagem2):
    m = ""
    for c in mensagem2:
        if c in alfabeto:
            index = alfabeto.index (c)
            alfabeto[index - numero_casa]
            m += alfabeto[(index - numero_casa) % len (alfabeto)]
        else: 
            m += c 
    return m 

print ("1. Criptografar 2. Descriptografar uma mensagem criptografada")
escolha=input()
if escolha== "1":
    mensagem=input()
    print(criptografia(mensagem))
elif escolha == "2":
    mensagem2=input()
    print(descriptografia(mensagem2))
else:
    print ("error")

