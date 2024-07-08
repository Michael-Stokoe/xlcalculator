

import logging
from xlcalculator import ModelCompiler
from xlcalculator import Model
from xlcalculator import Evaluator
import os
import json
from pydantic import BaseModel, Field
from typing import Any, Optional
from typing import Any
logging.basicConfig(level=logging.DEBUG)
import jsonpickle


filename = r'./use_case_indirect_test.xlsx'
compiler = ModelCompiler()
print(f" ###### Current working directory: {os.getcwd()}")
new_model = compiler.read_and_parse_archive(filename, build_code=True)
# print(new_model)
# Save new_model to a file called new_model.json
new_model.persist_to_json_file("model_indirect.json")

evaluator = Evaluator(new_model)

# class Cell(BaseModel):
#     address: str
#     name: str
#     value: Any
#     value_type: Optional[str] = None
#     value_type: Optional[str] = Field(None, pattern="^(Text|Number|Lookup)$")
#     value_options: Optional[list[Any]] = None
#     audit: Optional[bool] = None


# inputs = [
#     Cell(address="Rating tool!D8", name="Cover Type", value="Group Personal Accident", value_type="Text"),
#     Cell(address="Rating tool!D9", name="Scope of cover", value="24 hour cover", value_type="Text"),
#     Cell(address="Rating tool!D11", name="Total cover benefit amount requested by customer", value=1000000, value_type="Number"),
#     Cell(address="Rating tool!D13", name="Class of Business", value="Class 3", value_type="Text"),
#     Cell(address="Rating tool!D15", name="Number of employees", value=55, value_type="Number"),
#     Cell(address="Rating tool!D19", name="Do you want to add a Death benefit?", value="Yes", value_type="Text"),
#     Cell(address="Rating tool!D20", name="Death benefit multiplier requested by customer", value=1, value_type="Number"),
#     Cell(address="Rating tool!D21", name="Do you want to add a Permanent Total Disablement benefit?", value="Yes", value_type="Text"),
#     Cell(address="Rating tool!D22", name="Disablement benefit multiplier requested by customer", value=3, value_type="Number"),
#     Cell(address="Rating tool!D26", name="Do you want to add a Temporary Total Disablement benefit?", value="Yes", value_type="Text"),
#     Cell(address="Rating tool!D27", name="What period of cover do you want for the temporary benefit?", value="52 weeks", value_type="Text"),
#     Cell(address="Rating tool!D29", name="Do you want to add per medical emergency cover?", value="No", value_type="Text"),
#     Cell(address="Rating tool!D30", name="Per medical emergency cover amount?", value=200, value_type="Number"),
# ]

# outputs = [
#     Cell(address="Rating tool!D34", name="Death Benefit total cost", value=1500, value_type="Number"),
#     Cell(address="Rating tool!D35", name="Permanent Total Disablement benefit Cost", value=3390, value_type="Number"),
#     Cell(address="Rating tool!D36", name="Temporary Total Disablement benefit Cost", value=210600, value_type="Number"),
#     Cell(address="Rating tool!D37", name="Medical Emergency cover cost", value=0, value_type="Number"),
#     Cell(address="Rating tool!D40", name="Total Premium Cost", value=150843, value_type="Number"),
#     Cell(address="Rating tool!D41", name="Monthly premium", value=12570.25, value_type="Number")
# ]

# print(inputs[0].name, inputs[0].value) 

# for cell in inputs:
#     evaluator.set_cell_value(cell.address, cell.value)

# for cell in outputs:
#     print(f"cell: {cell.name} value: {evaluator.evaluate(cell.address)}")

# my_cell = 'Rating engine!M18'
# print(f"Result for {my_cell} [{evaluator.evaluate(my_cell)}]")

# my_cell = 'Rating engine!N18'
# print(f"Result for {my_cell} [{evaluator.evaluate(my_cell)}]")

# my_cell = 'Rating engine!O22'
# print(f"Result for {my_cell} [{evaluator.evaluate(my_cell)}]")

# my_cell = 'Rating engine!E11'
# print(f"Result for {my_cell} [{evaluator.evaluate(my_cell)}]")

my_cell = 'Sheet1!A4'
print(f"Result for {my_cell} [{evaluator.evaluate(my_cell)}]")