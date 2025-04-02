class empl:
    def __init__(self):
        self.id=123
        print('hello this is attributes its call itself when makin the object')
        self.salary=10000
        self.designation='SDE'
    def travel(self,dest):
        print(f'employee is now travelling to {dest}')    
##create an object/instance of class   
sam=empl()
sam.travel('delhi')    