# FastAPI Email Sender API

This project is a RESTful API for sending emails using **FastAPI** with **Celery** for task queue management and **Redis** as the message broker and result backend. The project is fully containerized using **Docker**.

## Features

- **FastAPI**: Provides a simple REST API to send emails asynchronously.
- **Celery**: Manages background tasks for sending emails.
- **Redis**: Acts as the message broker and result backend for Celery.
- **Docker**: Containerized deployment for FastAPI, Redis, and Celery workers.

## Requirements

- Docker
- Docker Compose

## Project Structure

```
email-sender/
│
├── app/
│   ├── __init__.py           # Package initialization
│   ├── main.py               # FastAPI application with endpoints
│   ├── celery_worker.py      # Celery configuration and worker setup
│   └── tasks.py              # Celery tasks for sending emails
│
├── Dockerfile                # Dockerfile for building FastAPI app image
├── Dockerfile.celery  # Dockerfile.celery for worker image
├── docker-compose.yml        # Docker Compose file for multi-container setup
├── requirements.txt          # Python dependencies
└── .env                      # Environment variables for Redis configuration
```

## Getting Started

### Prerequisites

Ensure that you have **Docker** and **Docker Compose** installed on your machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/email-sender.git
   cd email-sender
   ```

2. Copy the `.env.example` file to `.env`:

   ```bash
   cp .env.example .env
   ```

3. Open the `.env` file and update the necessary values, such as your SMTP credentials.

4. Build and start the containers:

   ```bash
   docker-compose up --build
   ```

5. Access the FastAPI application at:

   ```
   http://localhost:8000
   ```

### API Endpoints

#### Send Email

- **Endpoint**: `POST /send-email/`
- **Description**: Sends an email asynchronously.
- **Payload**:

  ```json
  {
    "recipient": "recipient@example.com",
    "subject": "Subject of the email",
    "body": "Body of the email"
  }
  ```

- **Response**:
  ```json
  {
    "task_id": "unique_task_id",
    "status": "Email queued"
  }
  ```

#### Check Task Status

- **Endpoint**: `GET /status/{task_id}`
- **Description**: Get the status of an email-sending task by `task_id`.
- **Response**:
  ```json
  {
    "task_id": "unique_task_id",
    "status": "PENDING / SUCCESS / FAILURE"
  }
  ```

### Email Configuration

The email-sending task is defined in the `tasks.py` file. By default, it uses Python's `smtplib` to send emails. Modify the SMTP server settings in the `send_email_task` function to match your email provider's configuration.

```python
with smtplib.SMTP("smtp.example.com", 587) as server:
    server.starttls()
    server.login("your-email@example.com", "your-password")
```

### Docker Compose Services

- **FastAPI**: Serves the REST API for sending and checking email status.
- **Redis**: Acts as a message broker for Celery.
- **Celery Worker**: Processes background tasks for sending emails.

### Stopping the Containers

To stop the containers, run:

```bash
docker-compose down
```

### Troubleshooting

- **Email not being sent**: Check the SMTP settings in `tasks.py` and ensure they are correct.
- **Task status stuck at "PENDING"**: Ensure Redis is running and Celery workers are properly connected.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
