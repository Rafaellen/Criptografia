import hmac 
import hashlib
import base64

# function p/ gerar HMAC SHA256
def gerar_hmac(mensagem, chave_secreta):
    mmensagem_bytes = mensagem.encode('utf-8')
    chave_bytes = chave_secreta.encode('utf-8')
    
    # cria o HMAC usando SHA256
    hmac_gerado = hmac.new(chave_bytes, mmensagem_bytes, hashlib.sha256)

    # retornando em b64 p/ melhor visualização
    return base64.b64encode(hmac_gerado.digest()).decode('utf-8')


# function para verificar HMAC
def verificar_hmac(mensagem, hmac_recebido, chave_secreta):
    hmac_calculado = gerar_hmac(mensagem, chave_secreta)
    
    # comparação segura (evitar ataques de tempo)
    return hmac.compare_digest(hmac_calculado, hmac_recebido)

# Exemplo de uso
chave = "senhaSuperSecreta123"
mensagem = "Dados importantes para proteger"

# Gera HMAC
hmac_assinatura = gerar_hmac(mensagem, chave)
print("Assinatura HMAC:", hmac_assinatura)  # Ex: q5k4LxVW4Z3X7jF6T2mN9oY...

# Verifica HMAC
valido = verificar_hmac(mensagem, hmac_assinatura, chave)
print("Válido?", valido)  # True

# Teste com mensagem adulterada
valido_falso = verificar_hmac("Dados falsos", hmac_assinatura, chave)
print("Válido (mensagem falsa)?", valido_falso)  # False