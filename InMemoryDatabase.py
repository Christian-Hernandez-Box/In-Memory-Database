class InMemoryDatabase:
    def __init__(self):
        self.database = {}
        self.transactions = []
        
    def set(self, name, value):
        if name in self.database:
            print("Provided name already in database.")
        else:
            if self.transactions:
                pass
            
            self.database[name] = value
            print('Value has been set successfully.')
        
    def get(self, name):
        if name not in self.database:
            print('Null')
        else:
            print(self.database[name])
        
    def delete(self, name):
        if name not in self.database:
            print('Provided name not in database.')
        else:
            if self.transactions:
                pass
            
            del self.database[name]
            print('Value successfully deleted.')
            
    def begin(self):
        if self.transactions:
            print('Transaction already open.')
        else:
            self.transactions.append([])
            
    def rollback(self):
        if not self.transactions:
            print('No transaction block open.')
        else:
            for transaction, in reversed(self.transactions.pop()):
                transactionType, name, value = transaction
                if transactionType == 'set':
                    del self.database[name]
                elif transaction == 'delete':
                    self.database[name] = value
                    
                print('Transaction lock has been rolled back.')
                
    def commit(self):
        if not self.transactions:
            print('Transaction block not opened')
        else:
            self.transactions = []
            print('Transaction block has been committed.')
                    
                
# Test Cases
db = InMemoryDatabase()

# Set Method
db.set('test1', 'value1')
db.set('test2', 'value2')
db.set('test1', 'value1')

# Get Method
db.get('test1')
db.get('test2')
db.get('test3')

# Delete Method
db.delete('test1')
db.get('test1')
db.delete('test3')