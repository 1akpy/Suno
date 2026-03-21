<div align="center">

<br/>

# 🎵 SunoLoad

### Download Suno tracks — MP3 & cover in one click

<br/>

[![Live](https://img.shields.io/badge/Live-sunoload.vercel.app-fb923c?style=flat-square)](https://sunoload.vercel.app)
[![License](https://img.shields.io/badge/License-MIT-fb923c?style=flat-square)](LICENSE)
[![API](https://img.shields.io/badge/Powered%20by-OpenSuno%20API-fb923c?style=flat-square)](https://github.com/1akpy/OpenSuno-and-ApiSuno)

<br/>

Paste any Suno link — short or full — and get a built-in player with cover art, waveform visualizer, and one-click download for both MP3 and cover image.

<br/>

</div>

---

## What it does

- Accepts any Suno link: `suno.com/s/xxx` or `suno.com/song/uuid`
- Shows track cover, title and artist
- Built-in audio player with waveform, progress bar and volume control
- Download MP3 and cover image directly from the page
- No backend needed — powered by [OpenSuno API](https://github.com/1akpy/OpenSuno-and-ApiSuno)

---

## How it works

```
suno.com/s/FqENDOXo6l4yKQT0
        ↓  opensuno.vercel.app resolves the link
suno.com/song/453a796e-a8e2-4d28-b24f-40f956cb5321
        ↓  returns direct CDN links
cdn1.suno.ai/453a796e-....mp3          ✅
cdn2.suno.ai/image_453a796e-....jpeg   ✅
```

---

## Usage

Just open `index.html` — no server, no build step, no dependencies.

Or deploy to any static host (Vercel, Netlify, GitHub Pages).

---

<div align="center">

*Not affiliated with Suno Inc. · Unofficial · Personal use only*<br/>
Powered by [OpenSuno API](https://github.com/1akpy/OpenSuno-and-ApiSuno)

</div>
