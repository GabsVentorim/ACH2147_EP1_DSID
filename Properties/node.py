from socket import *

class Node:
    def __init__(self, endereco, porta):
        self.endereco = endereco
        self.porta = porta
        self.socket_servidor = None # comeca nulo 

    def iniciar_servidor(self):
        try:
            self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um socket TCP/IP
            self.socket_servidor.bind((self.endereco, self.porta)) # Associa o socket a um endereço e porta
            self.socket_servidor.listen(1) # Coloca o socket em modo de escuta
            print(f"Servidor TCP iniciado em {self.endereco}:{self.porta}")
        except Exception as e:
            print(f"Erro ao iniciar servidor: {e}")

    def aguardar_conexao(self):
        try:
            conexao, endereco_cliente = self.socket_servidor.accept() # Aguarda por uma conexão -> retorna dois valores
            print(f"Conexão recebida de {endereco_cliente}")
            conexao.close()
        except Exception as e:
            print(f"Erro ao aguardar conexão: {e}")
        finally:
            self.fechar_servidor() # Fecha o socket do servidor

    def fechar_servidor(self):
        if self.socket_servidor:
            self.socket_servidor.close()
            print("Servidor TCP encerrado.")

# Exemplo de uso
if __name__ == "__main__":
    endereco = "127.0.0.1"  # Endereço de loopback
    porta = 12345  # Porta escolhida

    no = Node(endereco, porta)
    no.iniciar_servidor()
    no.aguardar_conexao()
