class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if b < 0:
            pos_b = -b
        else:
            pos_b = b

        for i in range(pos_b):
            result = self.add(result, a)
            
        if b < 0:
            result = -result
            
        return result

    def divide(self, a, b):
        if a == 0:
            return 0
        
        if b == 0:
            return "Error"
        
        negative_result = (a < 0) != (b < 0)
        if a < 0:
            a = -a
        if b < 0:
            b = -b    
        
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        
        if negative_result:
            result = -result
        
        return result
    
    def modulo(self, a, b):
        if a == 0:
            return 0
        
        if b == 0:
            return "Error"
        
        if a < 0:
            r = -a
        else:
            r = a
            
        if b < 0:
            abs_b = -b
        else:  
            abs_b = b
                
        while r >= abs_b:
            r = r - abs_b
        
        if a >= 0: 
            result = r 
        else:       
            result = -r
        
        return result
    
# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))