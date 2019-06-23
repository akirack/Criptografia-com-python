
def cifraDeCesar(msg, valor, lado):

    ctr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    novaMsg = []

    if valor == 0:
        return msg

    for i in msg:

        if lado == 0:
            troca = ctr.index(i) + valor

        elif lado == 1:
            troca = ctr.index(i) - valor

        if(troca >= 26):
            troca = troca - 26

        elif troca < 0:
             troca = 26 + troca

        novaMsg.append(ctr[troca])
    return ''.join(novaMsg)


