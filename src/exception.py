import sys #Used to manipulate different parts of the python runtime environment
from src.logger import logging

# Creates a custom error class
def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # Gets the informatio about which function and whicih line the exception occured
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in pythin script name[{0}] line number[{1}] error message[{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    
    return error_message
    
class CustomError(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail) 
    
    def __str__(self):
        return self.error_message
    
