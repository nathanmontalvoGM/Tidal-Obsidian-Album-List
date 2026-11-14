**Replaced by the GitHub Action** (`.github/workflows/tidal-sync.yml`, see `_code/README.md`), which syncs every morning without the PC. If you created the Windows task below, remove it so the two don't create the same notes:

    schtasks /delete /tn "Sync Tidal" /f

Old command, for reference:

    schtasks /create /tn "Sync Tidal" /tr "\"C:\Users\Nathan\AppData\Local\Programs\Python\Python312\python.exe\" \"C:\Users\minec\Documents\GitHub\Tidal-Obsidian-Album-List\_code\sync_tidal.py\"" /sc daily /st 23:00
