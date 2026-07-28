class Customer:

    def __init__(self, customer_id, name, email, phone):

        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__phone = phone

    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone
    