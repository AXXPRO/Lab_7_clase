from Erori.erori import SortError


def sortare_buble(lista_de_sortat, **params):
    """
    Functie custom de sortare ce foloseste metoda bulelor pentru a sorta
    param: lista_de _sortat este o LISTA cu ORICE tip de elemente
    param: optionale : va suporta doar 2 argumente, key, si reverse
    Va returna o lista sortata dupa cheie
    Va arunca o eroare SortError in lipsa unui parametru key
    """

    if "key" not in params and "cmp" not in params:
        raise SortError("Trebuie data o cheie!\n")
    if "reverse" not in params:
        invers = False
    else:
         invers = params["revers"]
    if "key" in params:
        functie_sortare = params["key"]
    else:
        functie_sortare = params["cmp"]

    lista_noua = lista_de_sortat[:]
    ok = False
    while not ok:

        ok = True
        for i in range(len(lista_noua) -1):
            
            if functie_sortare(lista_noua[i+1]) < functie_sortare(lista_noua[i]):
                
                lista_noua[i], lista_noua[i + 1] = lista_noua[i + 1], lista_noua[i]
                ok = False
    
    if invers:
        lista_intoarsa = []
        for i in range(len(lista_noua)):
            lista_intoarsa.append(lista_noua.pop())
        return lista_intoarsa
    
    return lista_noua
    
def shellSort(lista_de_sortat, **params):
    # code here
    if "key" not in params and "cmp" not in params:
        raise SortError("Trebuie data o cheie!\n")
    if "reverse" not in params:
        invers = False
    else:
         invers = params["reverse"]
    if "key" in params:
        functie_sortare = params["key"]
    else:
        functie_sortare = params["cmp"]

    lista_noua = lista_de_sortat[:]
    n = len(lista_de_sortat)
    gap=n//2
     
     
    while gap>0:
        j=gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j<n:
            i=j-gap # This will keep help in maintain gap value
             
            while i>=0:
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                if functie_sortare(lista_noua[i+gap])>functie_sortare(lista_noua[i]):
 
                    break
                else:
                    lista_noua[i+gap],lista_noua[i]=lista_noua[i],lista_noua[i+gap]
 
                i=i-gap # To check left side also
                            # If the element present is greater than current element
            j+=1
        gap=gap//2  
    if invers:
        lista_intoarsa = []
        for i in range(len(lista_noua)):
            lista_intoarsa.append(lista_noua.pop())
        return lista_intoarsa
    return lista_noua