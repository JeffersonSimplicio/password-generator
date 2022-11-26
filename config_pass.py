def size_password(min_size=4):
    while True:
        try:
            size = int(input(
                f'Qual o tamanho da senha?(Mínimo {min_size} dígitos) '
            ))
        except ValueError:
            print('Por favor, digite um número inteiro valido.')
        else:
            if size < min_size:
                print(f'O valor mínimo aceito é {min_size}')
            else:
                return size


def with_special_characters():
    positive = ('S', 'SIM', 'Y', 'YES')
    negative = ('N', 'NÃO', 'NAO', 'NO', 'NOT')
    while True:
        with_symbol = (
            str(input('Usar caracteres especiais(<=>?@[\]^_`{|}~.)?(S/N) '))
            .strip()
            .upper()
        )
        if with_symbol in positive:
            return True
        elif with_symbol in negative:
            return False
        else:
            print(
                'Resposta invalida!'
                '\nDigite "S" - Caso deseje usar caracteres especiais.'
                '\nDigite "N" - Caso não deseje usar caracteres especiais.'
            )
