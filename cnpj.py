def validar_cnpj(texto: str) -> str:
    while True:
        cnpj: str = str(input(texto)).replace('.', '').replace('/', '').replace('-', '')
        cnpj_invertido = cnpj[-3::-1]
        if not cnpj.isnumeric():
            print('O CNPJ deve ser numérico. ', end='')
        elif len(cnpj) != 14:
            print('O cnpj deve ter exatamente 14 digitos. ', end='')
        else:
            digito_1: int = int(cnpj[-2])
            digito_2: int = int(cnpj[-1])
            calculadores = [i for i in range(2, 10)] + [i for i in range(2, 6)]

            calculo_cnpj = [int(i) * calculador for i, calculador in zip(cnpj_invertido, calculadores)]
            soma = sum(calculo_cnpj)
            validador_1 = 11 - (soma % 11)
            if validador_1 >= 10:
                validador_1 = 0

            cnpj_invertido = f'{validador_1}{cnpj_invertido}'
            calculadores.append(6)

            calculo_cnpj = [int(i) * calculador for i, calculador in zip(cnpj_invertido, calculadores)]
            soma = sum(calculo_cnpj)
            validador_2 = 11 - (soma % 11)
            if validador_2 >= 10:
                validador_2 = 0
            if validador_1 == digito_1 and validador_2 == digito_2:
                print('cnpj válido. ')
                return cnpj
            else:
                print('cnpj inválido. ')


validar_cnpj('por favor digite seu cnpj: ')
