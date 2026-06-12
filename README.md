# Cloud Native E-Commerce Platform

A cloud-native e-commerce platform built using FastAPI microservices, PostgreSQL, Docker, Prometheus, and Grafana.

This project follows microservices architecture principles with independent services, database separation, Docker-based deployment, inter-service communication, and observability.

---

## Architecture

```text
                    Grafana
                       ↑
                  Prometheus
                       ↑

-----------------------------------------------------

User Service        : 5400
Product Service     : 5500
Inventory Service   : 5600
Order Service       : 5700
Payment Service     : 5800

-----------------------------------------------------

                  PostgreSQL
```

---

## Features

### User Service
- User registration
- User login
- JWT authentication
- Password hashing

### Product Service
- Product CRUD operations

### Inventory Service
- Inventory management
- Stock reduction API

### Order Service
- Order creation
- Inventory validation
- Inter-service communication

### Payment Service
- Payment creation
- Payment status updates

---

## Monitoring

Implemented monitoring and observability using:

- Prometheus
- Grafana

Metrics are exposed through:

```text
/metrics
```

Prometheus scrapes metrics from all services and Grafana visualizes them.

---

## Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- Pydantic

### Database
- PostgreSQL

### DevOps
- Docker
- Docker Compose

### Monitoring
- Prometheus
- Grafana

### Language
- Python

---

## Project Structure

```text
cloud-native-ecommerce-platform/

├── user-service
├── product-service
├── inventory-service
├── order-service
├── payment-service

├── prometheus
│   └── prometheus.yml

├── docker-compose.yml
├── README.md
└── .gitignore
```

---

## Inter-Service Communication

```text
Order Service
       ↓
Inventory Service
       ↓
Inventory Database
```

The Order Service validates stock availability and reduces inventory before creating an order.

---

## Future Enhancements

- Kubernetes deployment
- Azure Kubernetes Service (AKS)
- Azure Container Registry (ACR)
- AI-powered Operations Assistant
- CI/CD Pipeline
- Alerting with Grafana