import sqlite3

produto_nome = input('Qual o nome do produto: ')
produto_preco = float(input('Qual o preço do produto: '))
produto_quantidade = float(input('Qual a quantidade desse produto: '))


# Definindo o estoque inicial de produtos
produtos = {
    'Coca': 0,
    'Biscoito': 0,
    'Sorvete': 0
}
total_compra = 0

estoque = produtos.get(produto_nome)


if estoque is None:
    print('Produto não encontrado.')
else:
   
      
        preco_total = produto_preco * produto_quantidade

     
        produtos[produto_nome] -= produto_quantidade
        print(f'O Cliente esta levando os seguintes produtos: {produto_nome}')
        print(f'O preço total é: R${preco_total}')
    





conexao = sqlite3.connect('registro_produtos.db')


cursor = conexao.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    )
''')


cursor.execute('INSERT INTO produtos (nome, preco) VALUES (?, ?)', (produto_nome, produto_preco))


conexao.commit()


conexao.close()

