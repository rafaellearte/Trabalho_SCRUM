class Medico:
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade


class Hospital:
    def __init__(self, nome, medico):
        self.nome = nome
        self.medicos = [medico]

    def adicionar_medico(self, medico):
        self.medicos.append(medico)

    def listar_medicos(self):
        for medico in self.medicos:
            print(f"{medico.nome} - {medico.especialidade}")


# Criando médicos
medico1 = Medico("Carlos", "Cardiologia")
medico2 = Medico("Ana", "Pediatria")

# Criando hospital com pelo menos um médico
hospital = Hospital("Hospital Central", medico1)

# Adicionando outro médico
hospital.adicionar_medico(medico2)

hospital.listar_medicos()