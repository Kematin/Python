'''
import module
from module import class, variable, function
from module.class import atribute or method
from module import * (import all)

from module import class as c
some_class = c()
'''
import module
from module import Commands as Com

def use_module():
    print(module.variable) # output the variable from the module
    module.secret() # use fuction from module

    com = Com()
    com.return_commands(6, 5) # use method from module class
    com.print_message('HEllooooo')


use_module()

