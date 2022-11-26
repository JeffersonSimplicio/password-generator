positive = ('S', 'SIM', 'Y', 'YES')
negative = ('N', 'NÃO', 'NAO', 'NO', 'NOT')


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


def with_number():
    while True:
        with_num = str(input('Usar números na senha?(S/N) ')).strip().upper()
        if with_num in positive:
            return True
        elif with_num in negative:
            return False
        else:
            print(
                'Resposta invalida!'
                '\nDigite "S" - Caso deseje usar números.'
                '\nDigite "N" - Caso não deseje usar números.'
            )


def with_alphabet():
    while True:
        with_alpha = str(input('Usar letras na senha?(S/N) ')).strip().upper()
        if with_alpha in negative:
            return False
        elif with_alpha in positive:
            return True
        else:
            print(
                'Resposta invalida!'
                '\nDigite "S" - Caso deseje usar números.'
                '\nDigite "N" - Caso não deseje usar números.'
            )


def is_case_sensitive():
    while True:
        sensitive = (
            str(input('Usar letras maiúsculas e minusculas?(S/N) '))
            .strip()
            .upper()
        )
        if sensitive in positive:
            return True
        elif sensitive in negative:
            return False
        else:
            print(
                'Resposta invalida!'
                '\nDigite "S" - Para usar letras maiúsculas e minusculas.'
                '\nDigite "N" - Para usar apenas letras minusculas.'
            )


def with_special_characters():
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
