from modelos.lista_pacientes import PatientList

def main():
    lista_de_pacientes = PatientList()
    
    lista_de_pacientes.patient_list()
    lista_de_pacientes.add_patient(1, 'José', 'Estável')
    lista_de_pacientes.add_patient(2, 'Joaquim', 'Estável')
    lista_de_pacientes.add_patient(3, 'Neide', 'Tratamento intensivo')
    lista_de_pacientes.add_patient(4, 'Noel', 'Crítico')
    
    lista_de_pacientes.patient_list()
    
    lista_de_pacientes.remove_patient(3)
    print()
    lista_de_pacientes.patient_list()
    

if __name__ == "__main__":
    main()