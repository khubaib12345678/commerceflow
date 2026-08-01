from abc import ABC,abstractmethod

class SupportRequest(ABC):

    def __init__(self, request_id, order_id, request_status, request_date):

        self.__request_id = request_id
        self.__order_id = order_id
        self.__request_status = request_status
        self.__request_date = request_date

    def get_request_id(self):
        return self.__request_id

    def get_order_id(self):
        return self.__order_id

    def get_request_status(self):
        return self.__request_status

    def get_request_date(self):
        return self.__request_date

    @abstractmethod

    def process_request(self):
        pass