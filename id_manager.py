class id_manager :

    def __init__(self,start):
        self.initial_id = 0
        self.current_id = self.initial_id

    def next_id(self):
        self.current_id+=1
        return self.current_id-1