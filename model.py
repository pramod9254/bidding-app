from abc import ABC


class User2(ABC):
    def __init__(self, id, name, username: str, password: str, is_seller: bool):
        self.id = id
        self.name = name
        self.username = username
        self.password = password
        self.is_seller = is_seller

    def get_id(self):
        """

        :return: the user's username
        """
        return self.id
    
    def get_username(self):
        """

        :return: the user's username
        """
        return self.username
    
    def get_name(self):
        """

        :return: the user's username
        """
        return self.name
    
    def get_full_name(self):
        """

        :return: the user's username
        """
        return self.name
    
    def get_is_seller(self):
        """

        :return: the user's username
        """
        if self.is_seller == 1:
            return 'Seller'
        else:
            return 'Buyer'

