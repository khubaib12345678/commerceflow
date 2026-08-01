from support_requests.SupportRequest import SupportRequest
from services.shippingServices import ShippingService
from services.ResponseGenerator import ResponseGenerator


class TrackingRequest(SupportRequest):

    def __init__(self, request_id, order_id, request_status, request_date):
        super().__init__(
            request_id,
            order_id,
            request_status,
            request_date
         )

    def process_request(self, shipment):
        shipping_service = ShippingService()
        shipment = shipping_service.track_order(
            self.get_order_id(),
            shipment
        )
        response_generator = ResponseGenerator()

        if shipment:
            return response_generator.generate_tracking_response(shipment)

        else:
            return "NO shipment was found for the given Order ID"

    
