# Alestav Project

This API has been created to satisfy the following technical requirements from a client.

## Technical task
1. Models:

* Orders (id, agent name, auto number, date, transporter, driver, user)
* Order services (id, service name, quantity, price, currency, user who added the service, add time)
* Invoice (id, invoice number, invoice date, requisites)

3. Relationships:
* One order – one invoice
* One order – many services

4. Create an API with Django Rest Framework. Implement:
* Login/password authorization and use of JWT-tokens or equivalent
* Creating/updating/deletion of orders
* Creating/updating/deletion of services for an order (by ID)
* Creating/deletion of invoice for an order

5. Additional tasks:
* Get order, invoice and order related services information by invoice id
* Get summed up price for the services for a certain period (request needs to specify from and to dates)
* Get information (auto, data, agent, transporter, service) for a certain service (by a service id)
* Generate Swagger UI for testing
