

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
filename = r'./Personal Lines - Rating engine and testing tool (3 November)(insdi v1 0) 2023-11-30 v1 0.xlsx'
compiler = ModelCompiler()
print(f" ###### Current working directory: {os.getcwd()}")
new_model = compiler.read_and_parse_archive(filename, build_code=True)
print(new_model)
# exit(1)
# new_model.persist_to_json_file(json_file_name)
# reconstituted_model = Model()
# reconstituted_model.construct_from_json_file(json_file_name, build_code=True)

evaluator = Evaluator(new_model)

evaluator.set_cell_value('buildings-insdi!D19', 3000000)
val10 = evaluator.evaluate('buildings-insdi!D19')
print("buildings-insdi!D19", val10)
evaluator.set_cell_value('buildings-insdi!D25', "Tiles")

val20 = evaluator.evaluate('buildings-insdi!B2')
print("buildings-insdi!B2", val20)
val23 = evaluator.evaluate('buildings-insdi!G19')
print("buildings-insdi!G19", val23)
val24 = evaluator.evaluate('buildings-insdi!G22')
print("buildings-insdi!G22", val24)
val25 = evaluator.evaluate('buildings-insdi!G24')
print("buildings-insdi!G24", val25)
val26 = evaluator.evaluate('buildings-insdi!G25')
print("buildings-insdi!G25", val26)
val30 = evaluator.evaluate('buildings-insdi!F2')
print("buildings-insdi!F2", val30)
val27 = evaluator.evaluate('buildings-insdi!G40')
print("buildings-insdi!G40", val27)
val31 = evaluator.evaluate('buildings-insdi!F12')
print("buildings-insdi!F12", val31)


# c1 = evaluator.evaluate('contents-insdi!G12')
# print("contents-insdi!G12", c1)
# c2 = evaluator.evaluate('contents-insdi!G13')
# print("contents-insdi!G13", c2)

# m1 = evaluator.evaluate('motor-insdi!E19')
# print("motor-insdi!E19", m1)
# m2 = evaluator.evaluate('motor-insdi!E19')
# print("motor-insdi!E19", m2)

# val2 = evaluator.evaluate('Sheet1!B9')
# print("Sheet1!B9", val2)
# val3 = evaluator.evaluate('Sheet1!B10')
# print("Sheet1!B10", val3)
# val4 = evaluator.evaluate('Sheet1!B11')
# print("Sheet1!B11", val4)
# val5 = evaluator.evaluate('Sheet1!B12')
# print("Sheet1!B12", val5)
# val4 = evaluator.evaluate('Hundred')
# print("value 'evaluated' for Hundred with a defined name:", val4)
# val5 = evaluator.evaluate('Tenth!C1')
# print("value 'evaluated' for Tenth!C1 with a defined name:", val5)
# val6 = evaluator.evaluate('Tenth!C2')
# print("value 'evaluated' for Tenth!C2 with a defined name:", val6)
# val7 = evaluator.evaluate('Tenth!C3')
# print("value 'evaluated' for Tenth!C3 with a defined name:", val7)

# evaluator.set_cell_value('First!A2', 88)
# val17 = evaluator.evaluate('First!A2')
# print("New value for First!A2 is", val17)
