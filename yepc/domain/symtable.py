# In The Name Of God
# ========================================
# [] File Name : symtable.py
#
# [] Creation Date : 08-12-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
#
# [] Created By : Saman Fekri (Samanf74@gmail.com)
# =======================================


class SymbolTable:
    '''
    Provides symbol table in our front end compiler

    | Symbol | Type |
    |:------:|:----:|
    | jj1    | int  |

    '''
    def __init__(self, parent):
        self.symbols = {}
        self.header = {}
        self.meta = {}
        self.parent = parent
        self.temp_id_generator = self.temp_id_generator()
        self.scope_id_generator = self.scope_id_generator()

    def temp_id_generator(self):
        seq = 0
        while True:
            yield 'jj' + str(seq)
            seq += 1

    def scope_id_generator(self):
        seq = 0
        while True:
            yield 'js' + str(seq)
            seq += 1

    def new_temp(self, temp_type):
        temp_id = next(self.temp_id_generator)
        self.symbols[temp_id] = temp_type
        return temp_id

    def insert_variable(self, var_id, var_type: str):
        self.symbols[var_id] = var_type

    def insert_scope(self, scope_table):
        temp_id = next(self.scope_id_generator)
        self.symbols[temp_id] = scope_table

    def insert_procedure(self, proc_id, proc_table,
                         start=0, params=[], return_type='void'):
        self.symbols[proc_id] = proc_table
        self.meta[proc_id] = {
            'start': start,
            'params': params,
            'return_type': return_type
        }

    def add_width(self, width):
        self.header[width] = width

    def get_symbol(self, symbol):
        current = self
        result = current.symbols.get(symbol, None)
        while result is None:
            if current.parent is not None:
                current = current.parent
            else:
                raise KeyError(symbol)
            result = current.symbols.get(symbol, None)
        return result

    def get_symbol_meta(self, symbol):
        current = self
        result = current.meta.get(symbol, None)
        while result is None:
            if current.parent is not None:
                current = current.parent
            else:
                raise KeyError(symbol)
            result = current.meta.get(symbol, None)
        return result
