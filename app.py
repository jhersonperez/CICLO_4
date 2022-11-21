from fastapi import FastAPI
from ROUTES.student_route import student

app=FastAPI()

app.include_router(student)
