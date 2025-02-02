from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List, Optional

app = FastAPI()

# Enable CORS to allow requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Load student data from the JSON file
students_data = {}

with open("q-vercel-python.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    # Create a dictionary with name as the key and marks as the value
    for student in data:
        students_data[student["name"]] = student["marks"]

# API route to fetch marks based on student names
@app.get("/api")
def get_marks(name: Optional[List[str]] = Query(None)):
    if name:
        # Fetch marks for the requested names, maintaining the same order
        marks = [students_data.get(n) for n in name]
        return {"marks": marks}
    
    return {"marks": []}  # Return an empty list if no names are provided
