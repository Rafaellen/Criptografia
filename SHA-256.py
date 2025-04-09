import hashlib

def converter(text):
    convert = hashlib.sha256()
    convert.update(text.encode('utf-8'))
    return convert.hexdigest()

texto = "Senha segura!"
hash_convertido = converter(texto)
print(f'Texto original: {texto}')
print(f'Texto convertido para SHA256: {hash_convertido}')
print(f'Tamanho do hash: {len(hash_convertido)}')
