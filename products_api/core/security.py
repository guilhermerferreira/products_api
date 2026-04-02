from pwdlib import PasswordHash


pwd_context = PasswordHash()


def get_password_hash(password: str) -> str:
    '''Recebe uma senha e devolve a mesma criptografada'''
    return pwd_context.hash(password)  # hash() criptografa a senha


def verify_password(plain_password: str, hashed_password: str) -> bool:
    ''' Recebe uma senha descriptografada e compara com a criptografada
        se for igual retorna True
    '''
    return pwd_context.verify(plain_password, hashed_password) # verify() faz a comparação