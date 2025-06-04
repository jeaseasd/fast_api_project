from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import GPA
from calculator import calculate_gpa

app = FastAPI()

# CORS 설정
origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/gpa")
async def compute_gpa(student_data: GPA):
    return calculate_gpa(student_data)