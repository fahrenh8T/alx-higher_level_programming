#!/usr/bin/python3
'''module: 100-my_int
    defines a class MyInt that inherits from int
'''


class MyInt(int):
    '''class: MyInt
        inherits from the int class and
        inverts the behavior of the equality operators
    '''

    def __eq__(self, value):
        '''function: __eq__
            override == opeartor with != behavior
        '''
        return self.real != value

    def __ne__(self, value):
        '''function: __ne__
            override != operator to behave as ==
        '''
        return self.real == value
