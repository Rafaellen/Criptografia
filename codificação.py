import base64

# function p/ codificar para base64
def codificar_base64(texto):
    texto_bytes = texto.encode('utf-8') # converte texto p/ bytes
    texto_codificado = base64.b64encode(texto_bytes) # codifica p/ b64
    
    return texto_codificado.decode('utf-8') # converte os bytes p/ str

# function para decodificar b64
def decodificar_base64(cod_text): 
    texto_bytes = base64.b64decode(cod_text) # decodifica p/ b64
    return texto_bytes.decode('utf-8') # converte bytes p/ str

# Exemplo de uso
texto_original = "Thiago viado"
texto_codificado = codificar_base64(texto_original)
texto_decodificado = decodificar_base64(texto_codificado)

print("Original:", texto_original)
print("Codificado:", texto_codificado)  # Ex: T2zDoSwgbXVuZG8gSldUhQ==
print("Decodificado:", texto_decodificado)