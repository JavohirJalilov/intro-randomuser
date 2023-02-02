import requests


class RandomUser:
    def __init__(self) -> None:
        self.url = 'https://randomuser.me/api/'

    def get_randomuser(self) -> dict:
        '''get full data from randomuser
        
        Returns:
            dict: full data
        '''
        response = requests.get(self.url)
        return response.json()

    def get_phone(self) -> str:
        '''get user phone from randomuser
        
        Returns:
            str: user phone
        '''
        data = self.get_randomuser()
        results = data['results'][0]

        return results['phone']
    
    def get_city(self) -> str:
        '''get user city from randomuser
        
        Returns:
            str: user city
        '''
        pass
    
    def get_dob(self) -> dict:
        '''get user dob from randomuser
        
        Returns:
            dict: user dob
        '''
        pass
    
    def get_email(self) -> str:
        '''get user email from randomuser
        
        Returns:
            str: user email
        '''
        pass
    
    def get_first_name(self) -> str:
        '''get user first name from randomuser
        
        Returns:
            str: user first name
        '''
        pass
    
    def get_last_name(self) -> str:
        '''get user last name from randomuser
        
        Returns:
            str: user last name
        '''
        pass
    
    def get_full_name(self) -> str:
        '''get user full name from randomuser
        
        Returns:
            str: user full name
        '''
        return "Ms Kristina Ray"
    
    def get_gender(self) -> str:
        '''get user gender from randomuser
        
        Returns:
            str: user gender
        '''
        pass
    
    def get_id(self) -> dict:
        '''get user id from randomuser
        
        Returns:
            dict: user id
        '''
        pass
    
    def get_id_number(self) -> str:
        '''get user id number from randomuser
        
        Returns:
            str: user id number
        '''
        pass
    
    def get_info(self) -> dict:
        '''get user info from randomuser
        
        Returns:
            dict: user info
        '''
        pass
    
    def get_nat(self) -> str:
        '''get user nat from randomuser
        
        Returns:
            str: user nat
        '''
        pass
    
    def get_picture(self) -> dict:
        '''get user picture from randomuser
        
        Returns:
            dict: user picture
        '''
        pass

user = RandomUser()
print(user.get_phone())