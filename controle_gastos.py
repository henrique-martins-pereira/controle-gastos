import sqlite3

conn = sqlite3.connect('Gastos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS gastos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        valor FLOAT NOT NULL, 
        categoria TEXT NOT NULL,
        data TEXT NOT NULL
)
''')

conn.commit()

def adicionar_gastos():
    print("ADICIONAR GASTO")
    nome = input("Nome: ").capitalize()
    valor = float(input("Valor: ").replace(",", "."))
    categoria = input("Categoria: ").capitalize()
    data =  input("Data: ")
    cursor.execute("INSERT INTO gastos (nome, valor, categoria, data) VALUES (?,?,?,?)", (nome, valor, categoria, data))
    conn.commit()

def ver_gastos():
    print("VER GASTOS")
    cursor.execute("SELECT * FROM gastos")
    gastos = cursor.fetchall()

    if len(gastos) == 0:
        print("Nenhum gasto adicionado!")
    else:
        for gasto in gastos:
            id, nome, valor, categoria, data = gasto
            print(f"ID: {id} | {nome} | R${valor:.2f} | {categoria} | {data}")

def excluir_gasto():
    print("EXCLUIR GASTO")
    print("Recomendo ver a lista para saber o id")
    id_del = int(input("Selecione o id: "))
    cursor.execute("DELETE FROM gastos WHERE id = ?", (id_del,))
    conn.commit()
    print("Gasto excluído!")

print("CONTROLE DE GASTOS")
while True:
    print("-"*20)
    print("1. Adicionar gasto \n2. Ver gastos \n3. Excluir gasto pelo id \n4.SAIR")
    opc = int(input("Escolha o número correspondente a opção que desejar: "))
    if opc == 1:
        print("-"*20)
        adicionar_gastos()
    elif opc == 2:
        print("-"*20)
        ver_gastos()
    elif opc == 3:
        print("-"*20)
        excluir_gasto()
    elif opc == 4:
        print("-"*20)
        print("Saindo...")
        break
    else:
        print("-"*20)
        print("Opção inválida, digite novamente!")

conn.close()