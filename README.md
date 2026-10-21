# Angelou Fiel — AI Automation Portfolio (FastAPI)

A cinematic single-page portfolio with a working contact form. Built with Python + FastAPI.

## Files
- `index.html` — the cinematic front page (edit your text, projects, and contact here)
- `main.py` — the FastAPI app (serves the page + handles the contact form)
- `requirements.txt` — dependencies
- `Procfile` — start command for hosts
- `leads.jsonl` — created automatically; every contact message is saved here

## Run it on your computer
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
Then open http://127.0.0.1:8000

## Put it online — FREE (two ways to get a shareable link)

To share a link with clients, the page has to live online somewhere. Both options below
are free.

### Option A — Easiest: static site + Formspree (always-on, no server)
Best if you just want a fast, always-on link and a working contact form.
1. Sign up at **formspree.io** (free), create a form, and copy its URL
   (e.g. `https://formspree.io/f/abcdxyz`).
2. In `index.html`, set `const FORM_ENDPOINT = "https://formspree.io/f/abcdxyz";`
3. Upload **just `index.html`** to **Netlify** (drag-and-drop at app.netlify.com/drop) or
   **GitHub Pages**. You instantly get a public link.
   - Form submissions now email you through Formspree — no Python server needed.

### Option B — FastAPI on Render (built-in backend)
Best if you want the Python backend and email notifications built in.
1. Push this whole folder to a **GitHub** repo.
2. render.com → **New → Web Service** → connect the repo.
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
3. Deploy → you get a link like `https://your-name.onrender.com`.

> Note: free web-service tiers "sleep" when idle, so the first visit after a quiet spell
> takes a few seconds to wake. Static hosting (Option A) has no sleep.

**Short answer:** yes, you need it hosted to share a link — but Option A is free, always-on,
and takes about 5 minutes.

## Get notified by email (no dashboard needed)

A portfolio doesn't need a dashboard — just set these environment variables and the
contact form will email you every new message (leads are still saved to `leads.jsonl` too):

```
SMTP_HOST=smtp.gmail.com
SMTP_USER=youremail@gmail.com
SMTP_PASS=your-gmail-app-password
NOTIFY_TO=youremail@gmail.com
```

For Gmail you need an **App Password** (turn on 2-Step Verification, then create one) — your
normal password won't work. If you leave these unset, the form simply saves to `leads.jsonl`.

No-code alternative: point the form at **Formspree**, or send leads to an **n8n webhook**
that emails or messages you.

## Make it yours
- **Add your photo:** put a file named `me.jpg` in this folder. Until you do, your initials
  show as a placeholder.
- **Fix your links:** in `index.html`, replace the placeholder Email, Facebook, LinkedIn, and
  GitHub links (search for `yourpage` / `yourname` / `youremail`).
- **Edit your text:** headline, the About bio, the project cards (swap in your real projects
  and your capstone), and the toolkit chips.
- Leads land in `leads.jsonl`.
