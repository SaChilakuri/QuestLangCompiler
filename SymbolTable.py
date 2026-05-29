class Symbol:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value
    
class SymbolTable:
    def __init(self, parent=None):
        self.symbols={}
        self.parent = parent
    
    def insert(self,symbol):
        if symbol.name in self.symbols:
            raise Exception(f"Semantic Error: Symbol '{symbol.name}' already declared.")
        self.symbols[symbol.name] = symbol
    
    def lookup(self,name):
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent is not None:
            return self.parent.lookup(name)
        return None
