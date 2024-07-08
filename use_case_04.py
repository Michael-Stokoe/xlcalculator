

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
filename = r'./oracle_contents_insdi_20231207.xlsx'
compiler = ModelCompiler()
print(f" ###### Current working directory: {os.getcwd()}")
new_model = compiler.read_and_parse_archive(filename, build_code=True)
# print(new_model)
# new_model.persist_to_json_file(json_file_name)
# reconstituted_model = Model()
# reconstituted_model.construct_from_json_file(json_file_name, build_code=True)


input_parms = {
	"contents-insdi!E20": 200000,
	"contents-insdi!E21": 150000,
	"contents-insdi!E22": 100000,
	"contents-insdi!E23": 75000,
	"contents-insdi!E25": 1,
	"contents-insdi!E27": "Timber",
	"contents-insdi!E28": "Tiles",
	"contents-insdi!E30": "",
	"contents-insdi!E33": "Yes",
	"contents-insdi!E37": "Yes",
	"contents-insdi!E38": "Yes",
	"contents-insdi!E39": "Yes",
	"contents-insdi!E40": "Yes",
	"contents-insdi!E41": "Yes"
}
evaluator = Evaluator(new_model)

for key, value in input_parms.items():
    evaluator.set_cell_value(key, value)

total_premium = 10


# temp1 = evaluator.evaluate('contents-insdi!G2')
# print("contents-insdi!G2", temp1)	
temp1 = evaluator.evaluate('contents-insdi!G4')
print("contents-insdi!G4", temp1)	
temp1 = evaluator.evaluate('contents-insdi!G5')
print("contents-insdi!G5", temp1)	
temp1 = evaluator.evaluate('contents-insdi!G6')
print("contents-insdi!G6", temp1)	
temp1 = evaluator.evaluate('contents-insdi!G7')
print("contents-insdi!G7", temp1)	
temp1 = evaluator.evaluate('contents-insdi!G8')
print("contents-insdi!G8", temp1)	
temp1 = evaluator.evaluate('contents-insdi!G9')
print("contents-insdi!G9", temp1)		

temp1 = evaluator.evaluate('contents-insdi!E20')
print("contents-insdi!E20", temp1)	
temp1 = evaluator.evaluate('contents-insdi!E21')
print("contents-insdi!E21", temp1)	
temp1 = evaluator.evaluate('contents-insdi!E22')
print("contents-insdi!E22", temp1)	
temp1 = evaluator.evaluate('contents-insdi!E23')
print("contents-insdi!E23", temp1)	
temp1 = evaluator.evaluate('contents-insdi!H19')
print("contents-insdi!H19", temp1)	
temp1 = evaluator.evaluate('contents-insdi!H20')
print("contents-insdi!H20", temp1)	
temp1 = evaluator.evaluate('contents-insdi!H21')
print("contents-insdi!H21", temp1)		
temp1 = evaluator.evaluate('contents-insdi!H22')
print("contents-insdi!H22", temp1)	
temp1 = evaluator.evaluate('contents-insdi!H23')
print("contents-insdi!H23", temp1)	

temp1 = evaluator.evaluate('contents-insdi!H25')
print("contents-insdi!H25", temp1)	
temp1 = evaluator.evaluate('contents-insdi!H27')
print("contents-insdi!H27", temp1)	
temp1 = evaluator.evaluate('contents-insdi!H28')
print("contents-insdi!H28", temp1)	
# temp1 = evaluator.evaluate('contents-insdi!H30')
# print("contents-insdi!H30", temp1)	
temp1 = evaluator.evaluate('contents-insdi!H33')
print("contents-insdi!H33", temp1)	
temp1 = evaluator.evaluate('contents-insdi!H34')
print("contents-insdi!H34", temp1)	
temp1 = evaluator.evaluate('contents-insdi!H37')
print("contents-insdi!H37", temp1)		
temp1 = evaluator.evaluate('contents-insdi!H38')
print("contents-insdi!H38", temp1)	
temp1 = evaluator.evaluate('contents-insdi!H39')
print("contents-insdi!H39", temp1)		
temp1 = evaluator.evaluate('contents-insdi!H40')
print("contents-insdi!H40", temp1)	
temp1 = evaluator.evaluate('contents-insdi!H41')
print("contents-insdi!H41", temp1)		
temp1 = evaluator.evaluate('contents-insdi!H42')
print("contents-insdi!H42", temp1)																																

result = evaluator.evaluate('contents-insdi!G12')
print(f"Final output: {result}")