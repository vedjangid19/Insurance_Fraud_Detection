import os
import sys


class InsuranceFraudException(Exception):
    def __init__(self, error_message:Exception, error_detail:sys) -> None:
        super().__init__(error_message)
        self.error_message=InsuranceFraudException.get_detailed_error_message(
            error_message=Exception, 
            error_detail=sys
        )
        
    @staticmethod
    def get_detailed_error_message(error_message:Exception, error_detail:sys)->str:
        """
        error_message: Exception Object
        error_detail: sys Object
        """
        _,_,exec_tb = error_detail.exc_info()
        line_number = exec_tb.tb_lineno
        file_name = exec_tb.tb_frame.f_code.co_filename
        error_message = f"Error occured in scrip: [{file_name}] at line number: [{line_number}] error message: [{error_message}]"
        
        return error_message      
    
    def __str__(self) -> str:
        return self.error_message
    
    def __repr__(self) -> str:
        return InsuranceFraudException.__name__.str()