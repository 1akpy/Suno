<div align="center">

<br/>

# 🎵 SunoLoad

[![Suno](https://img.shields.io/badge/Suno-MP3%20Downloader-f97316?style=flat-square)](.)
[![Vercel](https://img.shields.io/badge/Vercel-Ready-000000?style=flat-square&logo=vercel&logoColor=white)](https://vercel.com)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](.)
[![PHP](https://img.shields.io/badge/PHP-any-777BB4?style=flat-square&logo=php&logoColor=white)](.)

<br/>


**Download any Suno track as MP3 in one click.**

[⭐ Star this repo](#)

</div>

---

## How it works

```
suno.com/s/r4t4FIFyoU7GTnX8
        ↓  backend follows the redirect
suno.com/song/453a796e-a8e2-4d28-b24f-40f956cb5321
        ↓  builds a direct link
cdn1.suno.ai/453a796e-....mp3  ✅
```

## Supported links

| Type | Example |
|------|---------|
| Short | `suno.com/s/r4t4FIFyoU7GTnX8` |
| Full  | `suno.com/song/453a796e-...`   |

---

## Hosting options

### ▶ Vercel (recommended, free)

1. Push this repo to GitHub
2. Go to [vercel.com](https://vercel.com) → **Add New Project**
3. Import the repo, Framework: **Other**
4. Hit **Deploy** — done

### ▶ Any Python hosting (Railway, Render, VPS)

```bash
python backend.py
```

Open `http://localhost:8080`

### ▶ Any PHP hosting (Beget, Timeweb, etc.)

Drop `index.html` + `get_full_url.php` on your server — works out of the box.

---

<div align="center">

*Not affiliated with Suno Inc. · For personal use only*

</div>
