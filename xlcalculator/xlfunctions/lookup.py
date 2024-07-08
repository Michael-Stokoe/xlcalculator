from . import xl, xlerrors, func_xltypes


@xl.register()
@xl.validate_args
def CHOOSE(
        index_num: func_xltypes.XlNumber,
        *values,
) -> func_xltypes.XlAnything:
    """Uses index_num to return a value from the list of value arguments.

    https://support.office.com/en-us/article/
        choose-function-fc5c184f-cb62-4ec7-a46e-38653b98f5bc
    """
    if index_num <= 0 or index_num > 254:
        raise xlerrors.ValueExcelError(
            f"`index_num` {index_num} must be between 1 and 254")

    if index_num > len(values):
        raise xlerrors.ValueExcelError(
            f"`index_num` {index_num} must not be larger than the number of "
            f"values: {len(values)}")

    idx = int(index_num) - 1
    return values[idx]


@xl.register()
@xl.validate_args
def VLOOKUP(
        lookup_value: func_xltypes.XlAnything,
        table_array: func_xltypes.XlArray,
        col_index_num: func_xltypes.XlNumber,
        range_lookup=False
) -> func_xltypes.XlAnything:
    """Looks in the first column of an array and moves across the row to
    return the value of a cell.

    https://support.office.com/en-us/article/
        vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1
    """
    print(f"lookup_value: {lookup_value}")
    print(f"table_array: {len(table_array)}") # TODO: Toggle detail vs length logging
    print(f"col_index_num: {col_index_num}")
    print(f"range_lookup: {range_lookup}")
    # if range_lookup:

    #     raise NotImplementedError("Exact match only supported at the moment.")

    col_index_num = int(col_index_num)

    if col_index_num > len(table_array.values[0]):
        raise xlerrors.ValueExcelError(
            'col_index_num is greater than the number of cols in table_array')

    if range_lookup:
        closest_match = None
        input_val_is_num = False
        if func_xltypes.Number.is_type(lookup_value):
            input_val = float(lookup_value)
            input_val_is_num = True        
        for index, row in enumerate(table_array):
            print(f"{index}. row[0]: {row[0]}")
            if func_xltypes.Number.is_type(row[0]):
                row_val = float(row[0])

                # COMPARING NUMBERS
                if input_val_is_num:
                    print(f"Comparing as numbers: input_val: {input_val} vs row_val: {row_val}")
                    if input_val == row_val:
                        print(f"Returning exact match: {row[col_index_num - 1]}")
                        return row[col_index_num - 1]
                    if index == 0 and input_val < row_val:
                        print(f"Lookup value smaller than all values in table_array.")   
                        raise xlerrors.NaExcelError('No match found. Lookup value smaller than all values in table_array.')
                    if row_val < input_val:
                        print(f"Setting closest_match to current row.")
                        closest_match = row
                        continue
                else:
                    print("skipping row because we can't compare numbers and text")
                    continue
            else:
                print("skipping row because we can't compare numbers and text")
                continue

            # COMPARING TEXT
            if not input_val_is_num:
                print(f"Comparing as test: input_val: {input_val} vs row_val: {row_val}")
                if row[0] == lookup_value:
                    print(f"Returning exact match: {row[col_index_num - 1]}")
                    return row[col_index_num - 1]
                if index == 0 and lookup_value < row[0]:
                    print(f"Lookup value smaller than all values in table_array.")
                    raise xlerrors.NaExcelError('No match found. Lookup value smaller than all values in table_array.')
                if lookup_value > row[0]:
                    print(f"Setting closest_match to current row.")
                    closest_match = row

        if closest_match:
            print(f"Returning closest match: {closest_match[col_index_num - 1]}")
            return closest_match[col_index_num - 1]
        else:
            print(f"Could not find values to compare to in the table_array. Are you comparing numbers to text?")
            raise xlerrors.NaExcelError('No match found. Could not find values to compare to in the table_array. Are you comparing numbers to text?')
    else:
        compare = lookup_value.__eq__
        try:
            result = max(row for row in table_array if row and row[0] and compare(row[0]))
            result = result[col_index_num - 1]
            print(f"Vlookup result for {lookup_value} in column {col_index_num} is: {result}")
        except ValueError:
            print(f"Vlookup result for {lookup_value} in column {col_index_num} is: None")
            raise xlerrors.NaExcelError(
                '`lookup_value` not in first column of `table_array`.')
        return result

    # table_array = table_array.set_index(0)

    # if lookup_value not in table_array.index:
        # raise xlerrors.NaExcelError(
        #     '`lookup_value` not in first column of `table_array`.')

    # return table_array.loc[lookup_value].values[0]


@xl.register()
@xl.validate_args
def MATCH(
        lookup_value: func_xltypes.XlAnything,
        lookup_array: func_xltypes.XlArray,
        match_type: func_xltypes.XlAnything = 1,
) -> func_xltypes.XlAnything:
    # assert len(lookup_array.values[0]) == 1

    lookup_array = lookup_array.flat

    if match_type == 1:
        if lookup_array != sorted(lookup_array):
            return xlerrors.NaExcelError(
                "Values must be sorted in ascending order"
            )
    if match_type == -1:
        if lookup_array != sorted(lookup_array, reverse=True):
            return xlerrors.NaExcelError(
                "Values must be sorted in descending order"
            )

    for i, val in enumerate(lookup_array):
        if val == lookup_value:
            return i + 1
        if match_type == 1 and val > lookup_value:
            return i or xlerrors.NaExcelError(
                "No lesser value found."
            )
        if match_type == -1 and val < lookup_value:
            return i or xlerrors.NaExcelError(
                "No greater value found."
            )
    return xlerrors.NaExcelError("No match found.")


@xl.register()
@xl.validate_args
def INDIRECT(
        indirect_address_text: func_xltypes.XlText
) -> func_xltypes.XlExpr:
    print(f"INDIRECT function called with: {indirect_address_text}")
    if "!" not in str(indirect_address_text):
        return xlerrors.NaExcelError("Invalid excel cell address provided.")
    val =  indirect_address_text()
    return val


