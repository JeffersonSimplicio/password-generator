import config_pass

size = config_pass.size_password()
with_num = config_pass.with_number()
with_alpha = config_pass.with_alphabet()
if with_alpha:
    case_sensitive = config_pass.is_case_sensitive()
with_symbol = config_pass.with_special_characters()
