# Areesh Rashid — Portfolio

Single-page Streamlit portfolio: skills, deployed AI apps, and product/design case studies.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy — GitHub

1. Create a new repo on GitHub, e.g. `portfolio` (github.com/areeshrashid6).
2. From this folder:
   ```bash
   git init
   git add .
   git commit -m "Initial portfolio"
   git branch -M main
   git remote add origin https://github.com/areeshrashid6/portfolio.git
   git push -u origin main
   ```

## Deploy — Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with your GitHub account.
2. Click **Create app** → **From existing repo**.
3. Select:
   - Repository: `areeshrashid6/portfolio`
   - Branch: `main`
   - Main file path: `app.py`
4. Click **Deploy**. Your portfolio will be live at a URL like:
   `https://portfolio-<random-id>.streamlit.app`

## Updating the site later

Any push to `main` on GitHub auto-redeploys the Streamlit app — no manual redeploy step needed.

## Editing content

All content (skills, projects, case studies, contact info) lives at the top of `app.py` in the
`SKILLS`, `LIVE_PROJECTS`, and `CASE_STUDIES` lists — edit those directly, no need to touch the
styling below.
