from datetime import date

class todonode():

    def __init__(self, context = None, date: date | None = None):
        self.context = context
        self.date = date.isoformat() if date else None
        print(self.date) 

