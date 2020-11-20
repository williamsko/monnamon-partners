from monnamon.exception.data_exception import DataException

def validate_data(func):
    print("Inside decorator")

    def inner(*args, **kwargs):
        print("Inside inner function")
        print("Decorated the function")
        print (kwargs)
        print (args)
        for key in args[0]:
            if key not in args[1]:
                msg = f'field {key} not allowed in data. Required keys are {args[0]}'
                raise DataException(msg)
        return func
    return inner  # this is the fun_obj mentioned in the above content
