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
