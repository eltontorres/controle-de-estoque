import sqlite3

#banco = sqlite3.connect('Supermercado.db')
#cursor = banco.cursor()


#cursor.execute("CREATE TABLE estoque (codigo INTEGER PRIMARY KEY, data text, produto text, barra integer, descricao text, custo float, venda float, quantidade integer)")

def adicionar_produto(novo_produto):
    """ 
    Adiciona um novo produto ao banco de dados "

    Arguments:
        novo_produto: um dicionario com as informações do produto { 'id' : 1 , 'produto' : 'arroz', 'preco' : 10 , 'quantidade' : 100} 
    
    Returns:
        Sem retornos

    """
    banco = sqlite3.connect('Supermercado.db')
    cursor = banco.cursor()
    cursor.execute(f"INSERT INTO estoque (data, produto, barra, descricao, custo, venda, quantidade) VALUES('{novo_produto['data']}', '{novo_produto['produto']}', '{novo_produto['barra']}', '{novo_produto['descricao']}', '{novo_produto['custo']}', '{novo_produto['venda']}','{novo_produto['quantidade']}' )")
    banco.commit()
    banco.close()

def remover_produto(codigo):
    """ 
    Remove um determinado produto do banco de dados
    
    Arguments: 
        produto: nome do produto que irá ser removido
    
    Returns:
        Sem retornos
    """
    banco = sqlite3.connect('Supermercado.db')
    cursor = banco.cursor()
    cursor.execute(f"DELETE FROM estoque WHERE codigo = '{codigo}'")
    banco.commit()
    banco.close

def atualizar_estoque(codigo, atualizar_local, atualizar_novo_valor):
    """  
    Atualiza uma determinada informação do produto

    Arguments:
        codigo: codigo do produto que terá suas informações alteradas
        atualizar_local: nome do campo que ser atualizado (id, produto, preco ou quantidade)
        atualizar_novo_valor: valor que irá ser adicionado e substituir o antigo.

    Returns:
        Sem retornos    
    """
    banco = sqlite3.connect('Supermercado.db')
    cursor = banco.cursor()
    cursor.execute(f"UPDATE estoque SET {atualizar_local} = {atualizar_novo_valor} WHERE produto = '{codigo}' ")
    banco.commit()
    banco.close()

def recuperando_dados():
    """ 
    Recupera todos os itens presentes no banco de dados

    Arguments:
        Nenhum argumento precisa ser passado
    
    Returns: 
        row: Uma lista com tuplas contendo as informações dos produtos.
    """
    banco = sqlite3.connect('Supermercado.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM estoque")
    row = cursor.fetchall()

    #print(row) deve ser utilizado caso queria mostrar no terminal os itens presentes no banco de dados
    return row

def existCode(codigo):
    banco = sqlite3.connect('Supermercado.db')
    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM estoque WHERE codigo = {codigo}")
    row = cursor.fetchall()
    banco.close()
    if row != []:
        return True
    return False 
