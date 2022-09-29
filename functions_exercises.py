def is_two(z):

   
    if z == '2' or z == 2:
        return True
    else:
        return False

def is_vowel(string):
    if type(string) == str:
        if len(string) == 1:
            if string in ['a','e','o','i','u']:
                return True
    else:
        return False

def calculate_tip(bill_total, tip_percentage = 0.2):
    return tip_percentage * bill_total
    
def get_letter_grade(grade):
    if grade>=88:
        print('A')
    elif grade>=80:
        print('B')
    elif grade>=67:
        print('C')
    elif grade>=60:
        print('D')
    else:
        print('F')