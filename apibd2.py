import mysql.connector

db_config = {
    'user': 'gabrieldecastro1',
    'password': '12we34rt',
    'host': 'db4free.net',
    'database': 'gabriel7812233',
    'port': 3306
}

def connect_to_db():
    return mysql.connector.connect(**db_config)

def get_all_atletas():
    try:
        conn = connect_to_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM atletas")
        atletas = cursor.fetchall()
        conn.close()
        return atletas
    except mysql.connector.Error as error:
        print(f"Erro ao consultar atletas: {error}")
        return None
def get_all_alunos():
    try:
        conn = connect_to_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()
        conn.close()
        return alunos
    except mysql.connector.Error as error:
        print(f"Erro ao consultar alunos: {error}")
        return None
def get_all_notas():

    try:
        conn = connect_to_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM notas")
        notass = cursor.fetchall()
        conn.close()
        return notass
    except mysql.connector.Error as error:
        print(f"Erro ao consultar notas: {error}")
        return None
def create_atleta(nome, idade, esporte, equipe):
    
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        sql = "INSERT INTO atletas (nome, idade, esporte, equipe) VALUES (%s, %s, %s, %s)"
        val = (nome, idade, esporte, equipe)
        cursor.execute(sql, val)
        conn.commit()
        conn.close()
        print(f"Atleta:\n {nome} foi adicionado(a) com sucesso.")
    except mysql.connector.Error as error:
        print(f"Erro ao criar atleta: {error}")


def delete_atleta(atleta_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        sql = "DELETE FROM atletas WHERE id = %s"
        val = (atleta_id,)
        cursor.execute(sql, val)
        conn.commit()
        conn.close()
        print(f"Atleta ID:{atleta_id} foi removido com sucesso.")
    except mysql.connector.Error as error:
        print(f"Erro ao remover atleta: {error}")

def notas(id_aluno):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        sql = "SELECT FROM vw_id_aluno WHERE id = %s"
        val = (id_aluno)
        cursor.execute(sql, val)
        conn.commit()
        conn.close()
        for i in id_aluno:
            print(i)
        
    except mysql.connector.Error as error:
        print(f"Erro ao listar alunos: {error}")

def menu():
    while True:
        print("\n1. Adicionar Atleta")
        print("2. Listar Atletas")      
        print("3. Remover Atleta")
        print("4. Listar Alunos")
        print("5. Listar Notas")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do Atleta: ")
            idade = int(input("Idade do Atleta: "))
            esporte = input("Esporte do Atleta: ")
            equipe = input("Equipe do Atleta: ")
            create_atleta(nome, idade, esporte, equipe)
        elif escolha == "2":
            atletas = get_all_atletas()
            if atletas:
                print("Lista de Atletas:")
                for atleta in atletas:
                    print(f"ID: {atleta['id']}, Nome: {atleta['nome']}, Idade: {atleta['idade']}, Esporte: {atleta['esporte']}, Equipe: {atleta['equipe']}")
            else:
                print("Nenhum atleta cadastrado.")
        elif escolha == "3":
            atleta_id = int(input("Informe o ID do atleta a ser removido: "))
            delete_atleta(atleta_id)
        elif escolha == "4":
            alunos = get_all_alunos()
            if alunos:
                print("Lista de Alunos:")
                for aluno in alunos:
                    print(f"id_aluno: {aluno['id_aluno']}, Nome: {aluno['nome']}, Idade: {aluno['idade']}, curso: {aluno['curso']}")
            else:
                print("Nenhum aluno cadastrado.")

        elif escolha == "5":
            notass = get_all_notas()
            if notass:
                print("Lista de Notas:")
                for nota in notass:
                    print(f"id_aluno: {nota['id_aluno']}, Disciplina: {nota['disciplina']}, Nota: {nota['nota']}")
            else:
                print("Nenhums nota cadastrada.")
        elif escolha == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()