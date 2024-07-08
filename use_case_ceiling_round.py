from xlcalculator import ModelCompiler
from xlcalculator import Model
from xlcalculator import Evaluator

filename = r'./ROUND.xlsx'
compiler = ModelCompiler()
new_model = compiler.read_and_parse_archive(filename, build_code=True)
# print(new_model)
# Save new_model to a file called new_model.json
# new_model.persist_to_json_file("model.json")

evaluator = Evaluator(new_model)

excel_value = evaluator.get_cell_value('Sheet1!A1')
# value = evaluator.evaluate('Sheet1!A1')
print(excel_value)

excel_value = evaluator.get_cell_value('Sheet1!A2')
value = evaluator.evaluate('Sheet1!A2')
print(value)