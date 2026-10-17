# Library scripts

Run these from a terminal in the vault folder. Commands that change things are dry runs unless you add `--apply` (sync_tidal.py has `--dry-run` instead).

| Command | What it does |
|---|---|
| `python _code/sync_tidal.py --dry-run` | Preview the Tidal sync |
| `python _code/sync_tidal.py` | Import new favorites; fill in missing tracklists, `added` dates and cover links; flag albums you unfavorited (notes and ratings are kept) |
| `python _code/sync_tidal.py --refresh-tracklists` | Replace every tracklist with Tidal's, keeping your ratings |
| `python _code/sync_tidal.py --fix-years` | Set each album's year to its original release year (slow) |
| `python _code/library.py check` | Health report: duplicates, missing covers or tracklists, untagged albums, unknown tags, unused covers. Changes nothing |
| `python _code/library.py tags --apply` | Apply `_scripts/tags.json` to every album and playlist, and add or remove genre pages to match |
| `python _code/library.py retag --apply` | Look up tags on MusicBrainz for albums with none (`--all` also tops up albums with fewer than 4) |

Files: `common.py` holds the shared code (paths, tag rules, note editing, MusicBrainz). Tag rules live in `_scripts/tags.json`.

The first sync opens a Tidal login and saves `tidal_session.json` in the vault. That file is in `.gitignore`. Never commit it.
