import sqlite3

conexao = sqlite3.connect("empresa.db")

cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE funcionario (
            codigo INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,
            diasTrabalhadis INTEGER,
            valorDia REAL,
            salarioBase REAL,
            comissao REAL
        );
    '''
)

cursor.close()
print("Tabela FUNCIONARIO criada com sucesso!")