class IdManager :

    def __init__(self,start=0):
        self.initial_id = 0
        self.current_id = self.initial_id

    def next_id(self):
        self.current_id+=1
        return self.current_id-1