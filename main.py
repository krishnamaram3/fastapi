'''
This module is intended to to create Endpoints for the Request Management App.
'''
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from typing import Optional
# Database
from database.db_operations import get_all_stones
# Logging 
from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()
app = FastAPI(title="Clous Stones", version="1.0.0",docs_url="/csp/api/docs", openapi_url="/csp/api/openapi.json", debug=True )

# Create the router object so that we can define the API endpoints
router = APIRouter(prefix="/csp/api")

# Add the Middleware 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@router.get("/stones")
def get_stones():
    list_of_stones = get_all_stones()
    return {"stones": list_of_stones}

# Include the router in the main FastAPI app
app.include_router(router)

