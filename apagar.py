def soma(valor_original, a, b):
    valor_original += a
    valor_original += b
    return valor_original

def mudar_valor_list(lista_passada):
    lista_passada[0] = 1
    lista_passada[1] = 2

def set_correct_time(wrong_time):
    aux_time =  int(wrong_time[:2]) - 3
    new_time = str(aux_time).rjust(2, '0') + wrong_time[2:]
    return new_time

hora = '22:02:3345'
new_time = set_the_right_time(hora)
print(new_time)




