# SunoLoad 🎵

<div align="center">

![Badge](https://img.shields.io/badge/Suno-MP3%20Downloader-f5a623?style=for-the-badge&logo=music&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-Ready-000000?style=for-the-badge&logo=vercel&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)

**[ [🇷🇺 Русский](#-русский) · [🇬🇧 English](#-english) ]**

</div>

---

## 🇷🇺 Русский

Вставь ссылку на трек с Suno — скачай MP3 в один клик.

### Как это работает

```
suno.com/s/r4t4FIFyoU7GTnX8
        ↓  бэкенд следует редиректу
suno.com/song/453a796e-a8e2-4d28-b24f-40f956cb5321
        ↓  собирается прямая ссылка
cdn1.suno.ai/453a796e-....mp3  ✅
```

### Поддерживаемые ссылки

| Тип | Пример |
|-----|--------|
| Короткая | `suno.com/s/r4t4FIFyoU7GTnX8` |
| Полная   | `suno.com/song/453a796e-...`   |

### Где хостить

**Vercel** (бесплатно, рекомендуется)
1. Залей репозиторий на GitHub
2. Зайди на [vercel.com](https://vercel.com) → **Add New Project**
3. Выбери репо, Framework: **Other**
4. **Deploy** — готово

**Python хостинг** (Railway, Render, VPS)
```bash
python backend.py
```

**PHP хостинг** (Beget, Timeweb и др.)

Залей `index.html` + `get_full_url.php` — работает сразу.

---

## 🇬🇧 English

Paste a Suno link — download MP3 in one click.

### How it works

```
suno.com/s/r4t4FIFyoU7GTnX8
        ↓  backend follows the redirect
suno.com/song/453a796e-a8e2-4d28-b24f-40f956cb5321
        ↓  builds a direct link
cdn1.suno.ai/453a796e-....mp3  ✅
```

### Supported links

| Type | Example |
|------|---------|
| Short | `suno.com/s/r4t4FIFyoU7GTnX8` |
| Full  | `suno.com/song/453a796e-...`   |

### Hosting

**Vercel** (free, recommended)
1. Push this repo to GitHub
2. Go to [vercel.com](https://vercel.com) → **Add New Project**
3. Import the repo, Framework: **Other**
4. Hit **Deploy** — done

**Python hosting** (Railway, Render, VPS)
```bash
python backend.py
```

**PHP hosting** (any shared hosting)

Drop `index.html` + `get_full_url.php` — works out of the box.

---

<div align="center">

*Not affiliated with Suno Inc. · For personal use only*

</div>
