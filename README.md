# Spawnpoint

**Frontend**: Astro + Tailwind CSS (Hosted on Cloudflare Pages)  
**Backend**: Flask (Hosted on Render)  

## 🚀 Quick Start

### Frontend Setup
```
cd frontend
npm install
npm run dev
```

### Backend Setup
```
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
flask run
```

## 🌐 Deployment

### Frontend (Cloudflare)
1. Connect GitHub repo to Cloudflare Pages
2. Set build command: `npm run build`
3. Set output directory: `dist`

### Backend (Render)
1. Create new Web Service
2. Link GitHub repo
3. Use Render's Python environment
4. Set env vars from `.env.example`

## 🔧 Environment Variables
`.env.example`:
```
# Frontend
PUBLIC_API_URL="https://your-render-service.onrender.com"

# Backend
DATABASE_URL="postgresql://user:pass@localhost/hackdb"
SECRET_KEY="your-secure-key"
```

## 📦 Included Features
- Pre-configured CORS
- SQLAlchemy ORM boilerplate
- Tailwind + Rose Pine theme
- CI/CD templates for GitHub Actions