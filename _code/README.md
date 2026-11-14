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
| `python _code/library.py retag --apply` | Look up tags on MusicBrainz for albums with none (`--all` also tops up albums with fewer than 4). Albums whose tags you edited on the album page are skipped |

Files: `common.py` holds the shared code (paths, tag rules, note editing, MusicBrainz). Tag rules live in `_scripts/tags.json`.

The first sync opens a Tidal login and saves `tidal_session.json` in the vault. That file is in `.gitignore`. Never commit it.

Tags: the Tidal sync only sets tags when it creates a new album note; it never changes an existing album's tags. To fix one album, use Edit tags on its page. To remove a junk tag everywhere, add it to the blocklist in `_scripts/tags.json` and run `library.py tags --apply`.

## Automatic sync (GitHub Actions)

`.github/workflows/tidal-sync.yml` runs `sync_tidal.py` on GitHub's servers every morning (about 5:23 AM Central), commits any new albums and pushes. Your PC doesn't need to be on. Obsidian on the PC and phone picks the changes up on its next pull.

- **Setup (once):** GitHub repo → Settings → Secrets and variables → Actions → New repository secret. Name it `TIDAL_SESSION` and paste the whole contents of `tidal_session.json` from your PC.
- **Run it now / preview:** GitHub → Actions → Tidal sync → Run workflow (tick "dry run" to only see what it would do).
- **If a run fails with "Tidal login failed":** run `python _code/sync_tidal.py` once on your PC (it opens the Tidal login), then replace the `TIDAL_SESSION` secret with the new `tidal_session.json`. GitHub emails you when a run fails.
- Don't also schedule the sync on your PC: two syncs that haven't seen each other's commits can both create the same new album note and conflict. Running it by hand on the PC now and then is fine; pull first.
