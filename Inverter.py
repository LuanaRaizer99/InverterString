def inverter_string(string):
    inverter = ''
    for i in range(len(string) - 1, -1, -1):
        inverter += string[i]
    return inverter

string_original = input("Digite um nome a ser invertido: ")
string_invertida = inverter_string(string_original)
print("Nome invertido:", string_invertida)
