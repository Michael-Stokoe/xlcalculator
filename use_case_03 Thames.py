

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
filename = r'./Thames.xlsx'
compiler = ModelCompiler()
print(f" ###### Current working directory: {os.getcwd()}")
new_model = compiler.read_and_parse_archive(filename, build_code=True)
# new_model.persist_to_json_file(json_file_name)
# reconstituted_model = Model()
# reconstituted_model.construct_from_json_file(json_file_name, build_code=True)

evaluator = Evaluator(new_model)

# my_cell = 'Rating Tool!C12'
# print(evaluator.evaluate(my_cell))

# m1 = evaluator.evaluate('Rating Tool!C22')
# print("Rating Tool!C22", m1)

# evaluator.set_cell_value('Rating Tool!B7',550000)

# m3 = evaluator.evaluate('CoverageLimit')
# print("CoverageLimit ", m3)

# m2 = evaluator.evaluate('Rating Tool!N6')
# print("Rating Tool!N6: ", m2)

m2 = evaluator.evaluate('Rating Tool!D7')
print("=Rating Tool!CD7: ", m2)
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
