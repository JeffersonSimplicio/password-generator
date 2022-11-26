def size_password():
    while True:
        size = str(
            input('Qual o tamanho da senha?(Mínimo 4 dígitos) ')
            ).strip()
        return size
