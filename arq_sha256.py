import hashlib
import os

def calcular_hash_arquivo(caminho_arq):
    sha256 = hashlib.sha256()
    
    with open(caminho_arq, 'rb') as arq:
        # leitura do arq em blocos, p/ lidar com arqs grandes
        while True:
            bloco = arq.read(65536) # 64kb
            if not bloco:
                break
            sha256.update(bloco)
            
    return sha256.hexdigest()

# verificamos a integridade de um arq comparando os caminhos. 
def verificar_integridade(caminho_original, caminho_copia): 
    hash_original = calcular_hash_arquivo(caminho_original)
    hash_copia = calcular_hash_arquivo(caminho_copia)
    
    if hash_original == hash_copia:
        print("Os arquivos são idênticos! Nenhuma alteração foi detectada.")
        return True
    else:
        print("Os arquivos são diferentes! O arquivo foi alterado.")
        print(f"Hash original: {hash_original}")
        print(f"Hash da cópia: {hash_copia}")
        return False
    
    