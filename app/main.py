# main.py

from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel, EmailStr
from celery.result import AsyncResult
from app.tasks import send_email_task

app = FastAPI()

class EmailRequest(BaseModel):
    recipient: EmailStr
    subject: str
    body: str

@app.post("/send-email/")
async def send_email(email_request: EmailRequest):
    try:
        task = send_email_task.delay(
            email_request.recipient,
            email_request.subject,
            email_request.body
        )
        return {"task_id": task.id, "status": "Email queued"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/status/{task_id}")
async def get_status(task_id: str):
    task_result = AsyncResult(task_id)
    return {"task_id": task_id, "status": task_result.state}
