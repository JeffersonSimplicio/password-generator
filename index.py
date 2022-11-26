import config_pass
from pass_generator import generator

size: int
with_num: bool
with_alpha: bool
case_sensitive = True
with_symbol: bool

while True:
    size = config_pass.size_password()
    with_num = config_pass.with_number()
    with_alpha = config_pass.with_alphabet()
    if with_alpha:
        case_sensitive = config_pass.is_case_sensitive()
    with_symbol = config_pass.with_special_characters()

    if with_num == with_alpha == with_symbol is False:
        print('Nenhum parâmetro foi selecionado')
    else:
        break

password = generator(size, with_num, with_alpha, case_sensitive, with_symbol)
print('Senha: ', password)
