# main.py

print('================================')
print(f'Running main.py - module name: {__name__}')

import sys 
sys.path.append('/home/srirev/01_Origin Educations/My_Session/Modules/Examples/User_Exerices/Importers')
import module1

print(module1)

module1.pprint_dict('main.globals', globals())



print('================================')