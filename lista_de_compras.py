class ListaDeCompras:
    
    def __init__(self):
        self._itens = []
        self._qtd_itens = []
    
    def adicionar_item(self, produto, quantidade):
        if not produto or not isinstance(produto, str):
            print('Nome do produto é inválido!')
        if not isinstance(quantidade, int) or quantidade <=0:
            print('Quantidade inválida!')
        self._itens.append(produto)
        self._qtd_itens.append(quantidade)
        
    def remove_itens(self, produto):
        if produto not in self._itens:
            print(f'{produto} não está na lista')
        else: 
            posicao = self._itens.index(produto)
            self._itens.pop(posicao)
            self._qtd_itens.pop(posicao)
        
    def listar_itens(self):
        if self._itens:
            print('Lista de compras: ')
            for i in range(len(self._itens)):
                print(f'{self._itens[i]}: {self._qtd_itens[i]}')
        else:
            print('A lista está vazia.')
            
def main():
    lista1 = ListaDeCompras()
    lista1.adicionar_item('Cuscuz Coringa', 10)
    lista1.adicionar_item('Cuscuz Sinhá', 20)
    lista1.adicionar_item('Cuscuz Tio Luiz', 30)


    lista1.remove_itens('Cuscuz Tio Luiz')

    lista1.listar_itens()
       

if __name__ == "__main__":
    main()