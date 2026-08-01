# Commerceflow-shipment-tracker

A simple Object-Oriented Programming (OOP) project that simulates an e-commerce shipment tracking system.

This project demonstrates the core principles of Object-Oriented Programming by processing a customer's tracking request through multiple classes with clear responsibilities.

---

## Project Overview

CommerceFlow simulates the following workflow:

Customer → Order → Shipment → Tracking Request → Shipping Service → Response Generator

When a customer requests the status of an order, the system:

1. Receives a tracking request.
2. Searches for the shipment using the order ID.
3. Retrieves shipment information.
4. Generates a clean tracking response.
5. Displays the response in the terminal.

---

## Features

- Customer Management
- Order Management
- Shipment Tracking
- Tracking Request Processing
- Shipping Service
- Response Generation
- Clean terminal output

---

## Object-Oriented Programming Concepts

This project demonstrates the following OOP principles:

### Encapsulation

Sensitive data is stored using private attributes and accessed through getter methods.

Example:

- Customer
- Order
- Shipment

---

### Inheritance

`TrackingRequest` inherits from the abstract `SupportRequest` class.

```text
SupportRequest
      │
      ▼
TrackingRequest
```

---

### Abstraction

`SupportRequest` is an Abstract Base Class (ABC) that defines a common interface for all future support requests.

```python
@abstractmethod
def process_request():
    pass
```

---

### Polymorphism

`TrackingRequest` provides its own implementation of the `process_request()` method.

---

### Composition

`TrackingRequest` collaborates with:

- ShippingService
- ResponseGenerator

instead of implementing all responsibilities itself.

---

### Single Responsibility Principle

Each class has one dedicated responsibility.

| Class | Responsibility |
|--------|----------------|
| Customer | Stores customer information |
| Order | Stores order information |
| Shipment | Stores shipment information |
| SupportRequest | Base class for support requests |
| TrackingRequest | Handles shipment tracking requests |
| ShippingService | Finds shipments using Order ID |
| ResponseGenerator | Creates formatted tracking responses |

---

## Project Structure

```text
commerceflow/

│
├── domain/
│   ├── customer.py
│   ├── orders.py
│   └── shipment.py
│
├── services/
│   ├── shippingServices.py
│   └── ResponseGenerator.py
│
├── support_requests/
│   ├── SupportRequest.py
│   └── TrackingRequest.py
│
├── main.py
├── README.md
├── LICENSE
└── .gitignore
```

---

## Sample Output

```text
========================================
        CommerceFlow AI Assistant
========================================

Shipment Status : In Transit

Carrier : DHL
Tracking Number : DHL123456789

Current Location : Lahore

Estimated Delivery : 2026-08-03

========================================
```

---

## Technologies Used

- Python 3
- Object-Oriented Programming
- Abstract Base Classes (ABC)

---

## Future Improvements

Possible future enhancements include:

- Return Request
- Refund Request
- Cancel Request
- AI Response Generation
- Database Integration
- REST API
- Multiple Shipping Providers
- Unit Testing

---

## Learning Objectives

This project was built to practice:

- Object-Oriented Programming
- Software Design
- Code Organization
- Class Relationships
- Inheritance
- Abstraction
- Encapsulation
- Polymorphism
- Composition

---

## Author

**Khubaib Naveed**

Aspiring AI Engineer • Machine Learning Engineer • Software Engineer

GitHub: *(https://github.com/khubaib12345678)*

---

## License

This project is licensed under the MIT License.