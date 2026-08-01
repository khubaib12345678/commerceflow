class ResponseGenerator:

    def generate_tracking_response(self, shipment):

        carrier = shipment.get_carrier()
        tracking_number = shipment.get_tracking_number()
        shipment_status = shipment.get_shipment_status()
        current_location = shipment.get_current_location()
        estimated_delivery = shipment.get_estimated_delivery()

        response = f""" ========================================
       CommerceFlow AI Assistant
========================================

Shipment Status : {shipment_status}

Carrier : {carrier}
Tracking Number : {tracking_number}

Current Location : {current_location}

Estimated Delivery : {estimated_delivery}


=========================================

"""
        return response