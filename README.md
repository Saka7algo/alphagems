# Alphagems

ALPHAGEMS character gallery with 309 entries, username search, shuffle, a keyboard-accessible full-size viewer, and WebP downloads.

Live site: https://chibi-gems.vercel.app

## Run locally

From this directory run `python -m http.server 8000`, then open http://localhost:8000.

The committed `images/`, `thumbs/`, and `characters.json` are ready to serve. No build or dependencies are required for the website.

## Update characters

Keep each character entry in `characters.json` linked to its full-size image in `images/` and its thumbnail in `thumbs/`. Names must be unique.

`build.py` and `sync_characters.py` are optional maintenance scripts requiring Pillow and the original PNG collection in a sibling `fullbody-chibi-white` directory. Original PNGs are maintained separately from this website repository.

## Deploy

Import this repository in Vercel using the Other framework preset, with the repository root as the output directory and no build command. The existing production project is `chibi-gems`.

Local Vercel linkage and authentication files are excluded from Git.
