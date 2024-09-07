class Patient:
    def __init__(self, id, name, health_status):
        self._id = id
        self._name = name
        self._health_status = health_status
        self._next_patient = None