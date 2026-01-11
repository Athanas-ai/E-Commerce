"""
Configuration file for Handcrafted Baskets Flask app.
Customize these settings as needed.
"""

import os

# Flask Settings
SECRET_KEY = os.getenv('SECRET_KEY', 'change-this-in-production')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///baskets.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Upload Settings
UPLOAD_FOLDER = 'uploads'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload

# WhatsApp
WHATSAPP_NUMBER = os.getenv('WHATSAPP_NUMBER', '8132981738')  # Replace with actual number

# Admin Settings
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
