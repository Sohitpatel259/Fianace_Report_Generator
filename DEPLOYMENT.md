# Finance Report Generator - Vercel Deployment Guide

## Deployment Steps

### 1. Install Vercel CLI (Optional)
```bash
npm install -g vercel
```

### 2. Deploy to Vercel

#### Option A: Using Vercel CLI
```bash
vercel
```
Follow the prompts and it will deploy your application.

#### Option B: Using Vercel Dashboard
1. Go to [vercel.com](https://vercel.com)
2. Click "Add New Project"
3. Import your GitHub repository
4. Vercel will auto-detect the configuration

### 3. Set Environment Variables

After deployment, you need to add your API keys:

1. Go to your project on Vercel Dashboard
2. Navigate to **Settings** → **Environment Variables**
3. Add the following variables:
   - `GROQ_API_KEY`: Your Groq API key
   - `AGNO_API_KEY`: Your Agno API key

**Important**: Do not commit your `.env` file to GitHub!

### 4. Redeploy

After setting environment variables, trigger a new deployment:
- Push a new commit to your repository, or
- Click "Redeploy" in Vercel Dashboard

## Files Created for Deployment

- **vercel.json**: Vercel configuration for Python app
- **requirements.txt**: Python dependencies
- **.vercelignore**: Files to ignore during deployment
- **.gitignore**: Updated to exclude sensitive files

## Testing Your Deployment

Once deployed, your app will be available at: `https://your-project-name.vercel.app`

Test the endpoints:
- `/` - Home page
- `/health` - Health check endpoint
- `/generate` - Report generation endpoint (POST)

## Troubleshooting

If you encounter issues:
1. Check the Vercel deployment logs
2. Ensure all environment variables are set correctly
3. Verify that requirements.txt includes all necessary packages
4. Check that your API keys are valid

## Local Testing Before Deployment

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
```

Visit `http://localhost:5000` to test locally before deploying.
