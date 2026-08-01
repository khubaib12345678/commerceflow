
class Shipment:

    def __init__(self, shipment_id, order_id, carrier, tracking_number, shipment_status, current_location, estimated_delivery):

        self.__shipment_id = shipment_id
        self.__order_id = order_id
        self.__carrier = carrier
        self.__tracking_number = tracking_number
        self.__shipment_status = shipment_status
        self.__current_location = current_location
        self.__estimated_delivery = estimated_delivery

    def get_shipment_id(self):
        return self.__shipment_id

    def get_order_id(self):
        return self.__order_id

    def get_carrier(self):
        return self.__carrier

    def get_tracking_number(self):
        return self.__tracking_number

    def get_shipment_status(self):
        return self.__shipment_status

    def get_current_location(self):
        return self.__current_location

    def get_estimated_delivery(self):
        return self.__estimated_delivery
    