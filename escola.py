import mysql.connector

# Definição da classe Aluno para representar os dados de um aluno
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

# Definição da classe Turma para representar os dados de uma turma
class Turma:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

# Classe SistemaEscolar para gerenciar interações com o banco de dados
class SistemaEscolar:
    def __init__(self):
        # Conexão com o banco de dados MySQL
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="he182555@",
            database="escola_db"
        )
        # Cria um cursor para executar consultas SQL
        self.cursor = self.conexao.cursor()

    def adicionar_aluno(self, nome, matricula):
        # Cria um objeto Aluno com os dados fornecidos
        aluno = Aluno(nome, matricula)
        # Query SQL para inserir o aluno na tabela 'alunos'
        query = "INSERT INTO alunos (nome, matricula) VALUES (%s, %s)"
        valores = (aluno.nome, aluno.matricula)
        # Executa a query SQL com os valores fornecidos
        self.cursor.execute(query, valores)
        # Comita a transação para efetivar a inserção no banco de dados
        self.conexao.commit()
        print(f"Aluno {aluno.nome} adicionado com sucesso!")

    def listar_turmas(self):
        # Query SQL para selecionar todas as turmas disponíveis
        query = "SELECT id, nome FROM turmas"
        self.cursor.execute(query)
        # Obtém todos os registros resultantes da query
        turmas = self.cursor.fetchall()
        if not turmas:
            print("Nenhuma turma encontrada.")
        else:
            print("Turmas disponíveis:")
            # Itera sobre os registros obtidos e imprime os IDs e nomes das turmas
            for turma in turmas:
                print(f"{turma[0]}. {turma[1]}")

    def adicionar_turma(self, nome, professor):
        # Cria um objeto Turma com os dados fornecidos
        turma = Turma(nome, professor)
        # Query SQL para inserir a turma na tabela 'turmas'
        query = "INSERT INTO turmas (nome, professor) VALUES (%s, %s)"
        valores = (turma.nome, turma.professor)
        # Executa a query SQL com os valores fornecidos
        self.cursor.execute(query, valores)
        # Comita a transação para efetivar a inserção no banco de dados
        self.conexao.commit()
        print(f"Turma {turma.nome} adicionada com sucesso!")

    def adicionar_aluno_turma(self, matricula_aluno, id_turma):
        # Query SQL para inserir um aluno em uma turma específica na tabela 'turma_aluno'
        query = "INSERT INTO turma_aluno (turma_id, aluno_matricula) VALUES (%s, %s)"
        valores = (id_turma, matricula_aluno)
        # Executa a query SQL com os valores fornecidos
        self.cursor.execute(query, valores)
        # Comita a transação para efetivar a inserção no banco de dados
        self.conexao.commit()
        print(f"Aluno adicionado à turma com sucesso!")

    def menu_adicionar_aluno_turma(self):
        # Método para exibir o menu e adicionar um aluno a uma turma específica
        self.listar_turmas()
        id_turma = input("Digite o ID da turma à qual deseja adicionar o aluno: ")
        matricula_aluno = input("Digite a matrícula do aluno que deseja adicionar: ")
        self.adicionar_aluno_turma(matricula_aluno, id_turma)

    def fechar_conexao(self):
        # Método para fechar a conexão com o banco de dados
        self.cursor.close()
        self.conexao.close()

# Exemplo de uso do programa
if __name__ == "__main__":
    # Instancia o objeto SistemaEscolar para iniciar o sistema
    sistema_escolar = SistemaEscolar()

    # Exibindo menu para operações no sistema escolar
    while True:
        print("\n===== MENU =====")
        print("1. Adicionar aluno")
        print("2. Adicionar turma")
        print("3. Listar turmas")
        print("4. Adicionar aluno a uma turma")
        print("5. Sair do programa")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Solicita nome e matrícula do aluno para adicionar ao sistema
            nome = input("Digite o nome do aluno: ")
            matricula = input("Digite a matrícula do aluno: ")
            sistema_escolar.adicionar_aluno(nome, matricula)
        elif opcao == "2":
            # Solicita nome da turma e nome do professor para adicionar ao sistema
            nome_turma = input("Digite o nome da turma: ")
            professor = input("Digite o nome do professor: ")
            sistema_escolar.adicionar_turma(nome_turma, professor)
        elif opcao == "3":
            # Lista todas as turmas disponíveis no sistema
            sistema_escolar.listar_turmas()
        elif opcao == "4":
            # Exibe o menu para adicionar um aluno a uma turma específica
            sistema_escolar.menu_adicionar_aluno_turma()
        elif opcao == "5":
            # Encerra o loop e finaliza a execução do programa
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

    # Ao finalizar o programa, fecha a conexão com o banco de dados
    sistema_escolar.fechar_conexao()
