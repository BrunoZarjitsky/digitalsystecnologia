def formata_cpf(cpf: str) -> str:
    '''Formata o cpf para que tenha apenas numeros'''
    return ''.join(filter(str.isdigit, cpf))
