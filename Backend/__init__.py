# app/__init__.py
# This file marks 'app' as a package

from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI(
    title="My Backend API",
    description="A FastAPI backend for my project",
    version="1.0.0"
)

# Import routes
from app.routes import user_routes

# Include router(s)
app.include_router(user_routes.router)