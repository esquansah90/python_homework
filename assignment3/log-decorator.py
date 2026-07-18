
# Task1

import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    
    def wrapper(*args, **kwargs):
        pos_params = args if args else "none"
        kw_params = kwargs if kwargs else "none"
       
        result = func(*args, **kwargs)
      
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {pos_params}")
        logger.log(logging.INFO, f"keyword parameters: {kw_params}")
        logger.log(logging.INFO, f"return: {result}")
        logger.log(logging.INFO, "-" * 40)

        return result
    return wrapper

@logger_decorator
def hello_world():
    print("Hello, World!")

@logger_decorator
def many_positional_args(*args):
    return True

@logger_decorator
def many_keyword_args(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    hello_world()
    many_positional_args(10, 20, 30)
    many_keyword_args(name="Esther", school="CTD", course="Python 100")


