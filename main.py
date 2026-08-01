from domain.customer import Customer
from domain.orders import Order
from domain.shipment import Shipment
from support_requests.TrackingRequest import TrackingRequest


customer = Customer(
    1,
    "Ali",
    "ali@gmail.com",
    "03001234567"
)

order = Order(
    1001,
    customer.get_customer_id(),
    ["Nike Shoes", "T-Shirts"],
    25000,
    "Processing",
    "2026-08-01"
)


shipment = Shipment(
    501,
    order.get_order_id(),
    "DHL",
    "DHL123456789",
    "In Transit",
    "Lahore",
    "2026-08-03"
)

shipments = [shipment]

tracking_request = TrackingRequest(
    1,
    order.get_order_id(),
    "Open",
    "2026-08-01"
)

response = tracking_request.process_request(shipments)

print(response)