import re
def check_day(input_pattern:str) -> bool:
    '''
    Check whether the given pattern matches the dates beteeen 01-31
    Anything not in this set should be considered as invalid
    '''
    date_pattern = r"^(0[1-9]|[12][0-9]|3[01])$"
    # If date_pattern matches input_pattern, return True; 
    # else return False
    if ( re.match(date_pattern,input_pattern)):
        return True
    else:
        return False

def check_email_address(input_pattern:str) -> str:
    '''
    Check whether the given pattern matches the standard email address
    '''
    email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    if ( email_pattern.match(input_pattern)):
        return "a valid email address"
    else:
        return "an invalid email address"
    
if __name__ == '__main__':
    # Test cases for day
    for date in range(40):
        print(f'Day{date} is {check_day(str(date))}')

    # Test cases for email
    emails = ["john.doe@example.com", "jane@gmail.co.uk", "invalid_email"]
    for email in emails:
        print(f'{email:20} is {check_email_address(email)}')

    
