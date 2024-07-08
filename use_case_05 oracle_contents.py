

import logging
from xlcalculator import ModelCompiler
from xlcalculator import Model
from xlcalculator import Evaluator
import os
import pprint 
logging.basicConfig(level=logging.DEBUG)

# json_file_name = r'./examples/joel_test1/test1.json'

# filename = r'./examples/joel_test1/test1.xlsx'
# filename = r'./examples/joel_test1/oracle_building_1.xlsx'
# filename = r'./oracle_building_1.xlsx'
filename = r'./oracle_contents_insdi_20240212.xlsx'
compiler = ModelCompiler()
print(f" ###### Current working directory: {os.getcwd()}")
new_model = compiler.read_and_parse_archive(filename, build_code=True)
print(new_model)
# exit(1)
# new_model.persist_to_json_file(json_file_name)
# reconstituted_model = Model()
# reconstituted_model.construct_from_json_file(json_file_name, build_code=True)

evaluator = Evaluator(new_model)

evaluator.set_cell_value('Contents Testing Tool!E20', 100000)
val10 = evaluator.evaluate('Contents Testing Tool!E20')
print("Contents Testing Tool!E20", val10)

evaluator.set_cell_value('Contents Testing Tool!E21', 100000)
val10 = evaluator.evaluate('Contents Testing Tool!E21')
print("Contents Testing Tool!E21", val10)

evaluator.set_cell_value('Contents Testing Tool!E22', 100000)
val10 = evaluator.evaluate('Contents Testing Tool!E22')
print("Contents Testing Tool!E22", val10)

evaluator.set_cell_value('Contents Testing Tool!E23', 100000)
val10 = evaluator.evaluate('Contents Testing Tool!E23')
print("Contents Testing Tool!E23", val10)

evaluator.set_cell_value('Contents Testing Tool!E25', "NCB 03")
val10 = evaluator.evaluate('Contents Testing Tool!E25')
print("Contents Testing Tool!E25", val10)

evaluator.set_cell_value('Contents Testing Tool!E27', "Brick & Plaster")
val10 = evaluator.evaluate('Contents Testing Tool!E27')
print("Contents Testing Tool!E27", val10)

evaluator.set_cell_value('Contents Testing Tool!E28', "Concrete")
val10 = evaluator.evaluate('Contents Testing Tool!E28')
print("Contents Testing Tool!E28", val10)

evaluator.set_cell_value('Contents Testing Tool!E40', "No")
val10 = evaluator.evaluate('Contents Testing Tool!E40')
print("Contents Testing Tool!E40", val10)


val11 = evaluator.evaluate('Contents Testing Tool!E42')
print("Contents Testing Tool!E42", val11)
val11 = evaluator.evaluate('Contents Testing Tool!F42')
print("Contents Testing Tool!F42", val11)
val11 = evaluator.evaluate('Contents Testing Tool!G42')
print("Contents Testing Tool!G42", val11)
val11 = evaluator.evaluate('Contents Testing Tool!H42')
print("Contents Testing Tool!H42", val11)
