class Order:

    def __init__(self, order_id, customer_id, products, amount, status, order_date):

        self.__order_id = order_id
        self.__customer_id = customer_id
        self.__products = products
        self.__amount = amount
        self.__status = status
        self.__order_date = order_date

    def get_order_id(self):
        return self.__order_id
    
    def get_customer_id(self):
        return self.__customer_id

    def get_products(self):
        return self.__products

    def get_amount(self):
        return self.__amount

    def get_status(self):
        return self.__status

    def get_order_date(self):
        return self.__order_date