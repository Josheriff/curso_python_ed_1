class Calculator:
    def sum(self, first_num, second_num):
        self._check_all_is_number(first_num, second_num)        
        return first_num + second_num
    
    def _check_all_is_number(self, first_num, second_num):
        if not isinstance(first_num, (int, float)) or not isinstance(second_num, (int, float)):
            raise TypeError

        # SI FUNCIONA ABAJO
        # if (type(first_num) != int and type(first_num) != float) or (type(second_num) != int and type(second_num) != float):
        #     raise TypeError
        

        