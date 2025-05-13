class HospitalApp:

 def executar(self):
        while True:
            print("\nSistema Hospitalar")
            print("1. Gerenciar Pacientes")
            print("2. Gerenciar Procedimentos")
            print("3. Gerenciar Consultas")
            print("4. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == '1':
                self.gerenciar_pacientes()
            elif opcao == '2':
                self.gerenciar_procedimentos()
            elif opcao == '3':
                self.gerenciar_consultas()
            elif opcao == '4':
                break
            else:
                print("Opção inválida!")
    
    def gerenciar_pacientes(self):
        # Implementar CRUD para pacientes
        pass
        
    def gerenciar_procedimentos(self):
        # Implementar CRUD para procedimentos
        pass
        
    def gerenciar_consultas(self):
        # Implementar CRUD para consultas
        pass
     def salvar_todos_os_dados(self):    