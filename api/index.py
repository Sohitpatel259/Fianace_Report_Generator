"""Vercel entrypoint that reuses the Flask app defined in app.py."""
from app import app as vercel_app

# Vercel looks for a top-level variable named `app`
app = vercel_app
