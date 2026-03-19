<div align="center">

<br/>

# 🎵 SunoLoad

[![Suno](https://img.shields.io/badge/Suno-MP3%20Downloader-f97316?style=flat-square)](.)
[![Vercel](https://img.shields.io/badge/Vercel-Ready-000000?style=flat-square&logo=vercel&logoColor=white)](https://vercel.com)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](.)
[![PHP](https://img.shields.io/badge/PHP-any-777BB4?style=flat-square&logo=php&logoColor=white)](.)

<br/>

**[ [🇷🇺 Русский](#-русский) · [🇬🇧 English](#-english) ]**

</div>

---

## 🇷🇺 Русский

Скопируй ссылку на любой трек с Suno и скачай его как MP3 — без регистрации, без расширений, без лишних шагов.

<br/>

### Как это работает

```
suno.com/s/r4t4FIFyoU7GTnX8
        ↓  бэкенд следует редиректу
suno.com/song/453a796e-a8e2-4d28-b24f-40f956cb5321
        ↓  собирается прямая ссылка
cdn1.suno.ai/453a796e-....mp3  ✅
```

<br/>

### Какие ссылки подходят

| Тип | Пример |
|-----|--------|
| Короткая | `suno.com/s/r4t4FIFyoU7GTnX8` |
| Полная   | `suno.com/song/453a796e-...`   |

<br/>

### Как задеплоить себе

> Хочешь поднять свою копию? Вот три способа — выбери любой.

**▸ Vercel** (бесплатно, проще всего)

1. Залей репозиторий на GitHub
2. Зайди на [vercel.com](https://vercel.com) → **Add New Project**
3. Выбери репо, Framework: **Other**
4. Нажми **Deploy** — всё готово

**▸ Python** (Railway, Render, VPS)

```bash
python backend.py
```

**▸ PHP** (Beget, Timeweb и любой другой шаред-хостинг)

Загрузи `index.html` и `get_full_url.php` — работает сразу из коробки.

---

## 🇬🇧 English

Copy any Suno track link and download it as MP3 — no account, no extension, no extra steps.

<br/>

### How it works

```
suno.com/s/r4t4FIFyoU7GTnX8
        ↓  backend follows the redirect
suno.com/song/453a796e-a8e2-4d28-b24f-40f956cb5321
        ↓  builds a direct link
cdn1.suno.ai/453a796e-....mp3  ✅
```

<br/>

### Supported link formats

| Type | Example |
|------|---------|
| Short | `suno.com/s/r4t4FIFyoU7GTnX8` |
| Full  | `suno.com/song/453a796e-...`   |

<br/>

### Self-hosting

> Want to run your own copy? Pick any option below.

**▸ Vercel** (free, easiest)

1. Push this repo to GitHub
2. Go to [vercel.com](https://vercel.com) → **Add New Project**
3. Import the repo, Framework: **Other**
4. Hit **Deploy** — you're done

**▸ Python** (Railway, Render, VPS)

```bash
python backend.py
```

**▸ PHP** (any shared hosting)

Upload `index.html` + `get_full_url.php` — works out of the box.

---

<div align="center">

<br/>

*Not affiliated with Suno Inc. · For personal use only*

</div>
