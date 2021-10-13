def get_longest_arithmetic_progression(lista):
    '''

    :param lista:
    :return: scea mai lugnga secventa care este progresie aritmetica
    '''
    list_secvente =[]
    for start in range (0,len(lista)):
        for end in range (start+1,len(lista) +1) :
            # parcurgem lista pe secvente
            sunt_o_progresire = True
            o_lista=lista[start:end]
            if len(o_lista)>1:
                r = o_lista[1] - o_lista[0]
                for index in range(2,len(o_lista)):
                    # verificam daca ratia este ramane la fel ,pentru a verifica daca secventa este progresie
                    if o_lista[index] - o_lista[index-1] != r:
                        sunt_o_progresire=False
                if sunt_o_progresire:
                    list_secvente.append(o_lista)
            else:
                list_secvente.append(o_lista)
    if len(list_secvente) > 0 :
        max_sec = []
        for secvente in list_secvente:
            if len(secvente) > len(max_sec):
                max_sec = secvente
        return max_sec
    else:
        return None

def test_get_longest_arithmetic_progression():
    assert get_longest_arithmetic_progression([1,2,3,4,1]) ==[1,2,3,4]
    assert get_longest_arithmetic_progression([100,200,300,2,3,4]) == [100,200,300]
    assert get_longest_arithmetic_progression([-10,-11,-12,-13,3,4]) == [-10,-11,-12,-13]
    assert get_longest_arithmetic_progression([10,11,12]) == [10,11,12]
    assert get_longest_arithmetic_progression([]) == None

def get_longest_div_k(lista,k):
    '''
    :param lista:
    :param k:
    :return: secventa maxima divizibila cu k
    '''
    list_secvente = []
    for start in range (0,len(lista)):
        for end in range (start+1,len(lista) +1) :
            divizibila=True
            for element in lista[start:end] :
                if element % k != 0 :
                  divizibila=False
            if divizibila :
                list_secvente.append(lista[start:end])
    if len(list_secvente) > 0 :
        max_sec=[]
        for secvente in list_secvente :
            if len(secvente) > len(max_sec) :
                max_sec=secvente
        return max_sec
    else:
        return None
def test_get_longest_div_k():
    assert get_longest_div_k([10,20,30,40,1,2],10)==[10,20,30,40]
    assert get_longest_div_k([2,3,4,5,1,3,12,2,4,6,8],2)==[12,2,4,6,8]
    assert get_longest_div_k([11,22,33,99],11) == [11,22,33,99]
    assert get_longest_div_k([],2)==None
def get_media_unei_liste(lista):
    s=0
    for element in lista :
        s+=element
    return s/len(lista)
def get_longest_average_below(lista, average):
    list_secvente = []
    for start in range(0, len(lista)):
        for end in range(start + 1, len(lista) + 1):
            for element in lista[start:end]:
                if get_media_unei_liste(lista[start:end])< average:
                    list_secvente.append(lista[start:end])
    if len(list_secvente) > 0 :
        max_sec=[]
        for secvente in list_secvente :
            if len(secvente) > len(max_sec) :
                max_sec=secvente
        return max_sec
    else:
        return None
def test_get_longest_average_below():
    assert get_longest_average_below([1,2,3],2.5)==[1,2,3]
    assert get_longest_average_below([10, 20 ,30, 40 ,213 ,321, 2], 30) == [10, 20, 30, 40]
    assert get_longest_average_below([1,2,3],1)== None
    assert get_longest_average_below([1,2,3],-10)== None
    assert get_longest_average_below([],10)== None
def citire_lista ():
    result_list = []
    string_list = input("Introduceti elementele listei cu spatiu intre ele :")
    lista_elemente = string_list.split(sep=" ")

    for element_str in lista_elemente :
        element=int(element_str)
        result_list.append(element)
    return result_list
def main():
    lista=[]
    sfarsit=False
    while sfarsit == False :
        print(
            """
            1.Citire lista
            2.Cea mai lunga secventa divizibila cu k
            3.Cea mai lunga secventa care este progresie aritmetica
            4.Cea mai lunga secventa a carei medie este mai mica decat un numar citit
            X.Inchide program
            """
        )
        optiune = input("Alege optiune :")
        if optiune == '1':
            lista = citire_lista()
        elif optiune == '2' :
            n=int(input("Dati k:"))
            print(f'Cea mai lunga secventa divizibila cu {n} este:')
            print(get_longest_div_k(lista,n))
        elif optiune == '3':
            print("Cea mai lunga secventa care este progresie aritetica este:")
            print(get_longest_arithmetic_progression(lista))
        elif optiune =='4' :
            nr_citit=float(input("Dati un numar:"))
            print("Cea mai lunga secventa a carei medie este mai mica decat un numar citit este: ")
            print (get_longest_average_below(lista,nr_citit))
        elif optiune == 'x' :
            sfarsit = True
        else:
            print("Optiune invalida")
    test_get_longest_div_k()
    test_get_longest_arithmetic_progression()
    test_get_longest_average_below()
if __name__ == '__main__':
    main()