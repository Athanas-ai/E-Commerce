# Deployment Steps for Render

## Prerequisites
1. GitHub account (create one at https://github.com)
2. Render account (create one at https://render.com)

## Step 1: Initialize Git Repository
```bash
cd e:\Websites\baskets
git init
git add .
git commit -m "Initial commit - Handcrafted Baskets"
```

## Step 2: Create GitHub Repository
1. Go to https://github.com/new
2. Create a new repository called "handcrafted-baskets"
3. Copy the repository URL

## Step 3: Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/handcrafted-baskets.git
git branch -M main
git push -u origin main
```

## Step 4: Deploy on Render
1. Go to https://dashboard.render.com
2. Click "New +" → "Web Service"
3. Select "Deploy an existing repository"
4. Paste your GitHub repository URL
5. Fill in the details:
   - **Name**: handcrafted-baskets
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

6. Add Environment Variables:
   - `WHATSAPP_NUMBER`: 8132981738 (or your number)
   - `SECRET_KEY`: (generate a random secret key)
   - `DEBUG`: False

7. Click "Create Web Service"

## Files Already Prepared:
✅ Procfile - tells Render how to run the app
✅ requirements.txt - includes gunicorn for production
✅ All code configured for production

Your app will be live in a few minutes!
