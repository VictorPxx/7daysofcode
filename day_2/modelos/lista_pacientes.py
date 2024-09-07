from modelos.paciente import Patient

class PatientList:
    def __init__(self):
        self._head = None
        self._tail = None
        
    def add_patient(self, id, name, health_status):
        new_patient = Patient(id, name, health_status) # Instância um novo paciente
        if self._head: # Se já tem paciente na lista, o novo paciente vai para o final e vira a calda da lista
            self._tail._next_patient = new_patient
            self._tail = new_patient
        else: # Caso a lista estiver vazia, o paciente se tornará cabeça e calda da lista
            self._head = new_patient
            self._tail = new_patient
            
    def remove_patient(self, id):
        if self._head is None: # Se a lista está vazia, mostrará um IndexError
            raise IndexError('the list is empty')
        elif self._head._id == id: # Se o paciente há ser removido for o head, o próximo nó se tornará o head
            self._head = self._head._next_patient
            if self._head is None: # Se a lista ficar vazia, tail também será atualizado
                self._tail = None
            raise IndexError('the list is empty')
        else: # A lista contendo pacientes, percorremos-a até encontrar o paciente a ser removido
            current_patient = self._head
            while current_patient._next_patient is not None:
                if current_patient._next_patient._id == id:
                    # Quando encontrarmos o paciente a ser removido, atualizamos o ponteiro para o próximo paciente
                    current_patient._next_patient = current_patient._next_patient._next_patient
                    if current_patient._next_patient is None:
                        # Se não tiver um próximo paciente, o mesmo vira a calda
                        self._tail = current_patient
                        raise IndexError('the list is empty')
                current_patient = current_patient._next_patient
                
    def patient_list(self):
        if self._head is None: # Se a lista está vazia, print avisando
            print('A lista está vazia')
        else: # Caso contrário imprime a lista de pacientes
            current_patient = self._head
            while current_patient is not None:
                # Equanto o existir paciente na lista, imprime (ID, NOME, ESTADO DE SAÚDE) e atualiza o ponteiro para o próximo paciente
                print(f'ID: {current_patient._id}, Nome: {current_patient._name}, Estádo de saúde: {current_patient._health_status}')
                current_patient = current_patient._next_patient