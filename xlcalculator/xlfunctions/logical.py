from typing import Tuple, Union

from . import xl, xlerrors, func_xltypes


@xl.register()
@xl.validate_args
def AND(
        *logicals: Tuple[func_xltypes.XlExpr]
) -> func_xltypes.XlBoolean:
    """Determine if all conditions in a test are TRUE

    https://support.office.com/en-us/article/
        and-function-5f19b2e8-e1df-4408-897a-ce285a19e9d9
    """
    if not logicals:
        raise xlerrors.NullExcelError('logical1 is required')

    # Use delayed evaluation to minimize th amount of values to evaluate.
    for logical in logicals:
        val = logical()
        for item in xl.flatten([val]):
            if func_xltypes.Blank.is_blank(item):
                continue
            if not bool(item):
                return False

    return True


@xl.register()
@xl.validate_args
def FALSE() -> func_xltypes.XlBoolean:
    """Returns the logical value FALSE.

    https://support.office.com/en-us/article/
        false-function-2d58dfa5-9c03-4259-bf8f-f0ae14346904
    """
    return False


@xl.register()
@xl.validate_args
def OR(
        *logicals: Tuple[func_xltypes.XlExpr]
) -> func_xltypes.XlBoolean:
    """Determine if any conditions in a test are TRUE.

    https://support.office.com/en-us/article/
        or-function-7d17ad14-8700-4281-b308-00b131e22af0
    """
    if not logicals:
        raise xlerrors.NullExcelError('logical1 is required')

    # Use delayed evaluation to minimize th amount of valaues to evaluate.
    for logical in logicals:
        val = logical()
        for item in xl.flatten([val]):
            if func_xltypes.Blank.is_blank(item):
                continue
            if bool(item):
                return True

    return False


@xl.register()
@xl.validate_args
def IF(
        logical_test: func_xltypes.XlExpr,
        value_if_true: func_xltypes.XlExpr = True,
        value_if_false: func_xltypes.XlExpr = False
):
    """Return one value if a condition is true and another value if it's false.

    https://support.office.com/en-us/article/
        if-function-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2
    """
    # Use delayed evaluation to only evaluate the true or false value but not
    # both.
    return value_if_true() if logical_test() else value_if_false()


@xl.register()
@xl.validate_args
def IFERROR(
        logical_test: func_xltypes.XlExpr,
        value_if_error: func_xltypes.XlExpr = True,
):
    """Return the given value if the logical test results in an error, otherwise return the results of the logicalß test.

    https://support.microsoft.com/en-us/office/
        iferror-function-c526fd07-caeb-47b8-8bb6-63f3e417f611
    """
    # Use delayed evaluation to only evaluate the true or false value but not
    # both.
    result = value_if_error() if isinstance(logical_test(), xlerrors.ExcelError) else logical_test()
    print(f"IFERROR result: {result}")
    return result


@xl.register()
@xl.validate_args
def NOT(logical: func_xltypes.XlExpr) -> func_xltypes.XlBoolean:
    """Return inverse of boolean representation of value.

    https://support.microsoft.com/en-us/office/
        not-function-9cfc6011-a054-40c7-a140-cd4ba2d87d77
    """
    return not bool(logical())


@xl.register()
@xl.validate_args
def TRUE() -> func_xltypes.XlBoolean:
    """Returns the logical value TRUE.

    https://support.office.com/en-us/article/
        true-function-7652c6e3-8987-48d0-97cd-ef223246b3fb
    """
    return True

@xl.register()
@xl.validate_args
def IFS(*args: Tuple[Union[func_xltypes.XlExpr, func_xltypes.XlAnything]]) -> func_xltypes.XlAnything:
    """Checks whether one or more conditions are met and returns a value corresponding to the first TRUE condition.

    Args:
        *args: Variable number of arguments representing the conditions and corresponding values.

    Returns:
        The value corresponding to the first TRUE condition.

    Raises:
        xlerrors.ValueExcelError: If the condition is not a boolean value.
        xlerrors.NaExcelError: If none of the conditions are met.

    Reference:
    - https://support.office.com/en-gb/f1/topic/36329a26-37b2-467c-972b-4a39bd951d45
    """
    for i in range(0, len(args), 2):
        if result := args[i]():
            # print(f"result: {result in [True, False]}")
            if result and result in [True, False]:
                return args[i+1]()
            else: # result is not a True or False value
                print("Error: IFS condition did not result in a boolean value.")
                return xlerrors.ValueExcelError("Condition is not a boolean value.")
    print("Error: No IFS conditions resulted in a True value.")
    return xlerrors.NaExcelError()




# @xl.register()
# @xl.validate_args
# def IFS(
#     logical_test: func_xltypes.XlExpr,
#     value_if_true: func_xltypes.XlAnything,
#     *ifsList: Tuple[Union[
#         func_xltypes.XlExpr, func_xltypes.XlAnything
#     ]]
# ) -> func_xltypes.XlAnything:
#     """Checks whether one or more conditions are met and returns a value corresponding to the first TRUE condition..

#     https://support.office.com/en-gb/f1/topic/36329a26-37b2-467c-972b-4a39bd951d45
#     """

#     print(f'if list: {ifsList}')

#     if logical_test():
#         print(f"logical_test: {logical_test()}")
#         return value_if_true()
#     else:
#         for item in ifsList:
#             print(f"item: {item}")
#             if item[0]():
#                 return item[1]()

#         return xlerrors.ValueExcelError("No true conditions found.")

