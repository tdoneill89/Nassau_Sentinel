# Nassau County Housing Development Watchdog 🏘️🚨

Automatically scrapes town websites, county planning boards, NYS legislation,
and local news for high-density housing development activity — and blasts alerts
to a Telegram channel.

**Runs free, automatically, every day at 8 AM via GitHub Actions.**

---

## What It Watches For

- Village board agendas: Lynbrook, Rockville Centre, Malverne, Town of Hempstead
- Nassau County Planning Commission meeting docs
- NYS Senate housing/zoning legislation
- LI Herald (Lynbrook, RVC, Malverne editions), Blank Slate Media, Newsday

**Keywords include:** multifamily, rezoning, Transit-Oriented Development, SEQRA,
mixed-use, accessory dwelling units, affordable housing overlay, 485-a, 421-a,
Governor Hochul housing compact, and more. (All editable in `config.py`.)

---

## Setup — Step by Step (~20 minutes)

### STEP 1 — Create a Telegram Bot

1. Open Telegram and search for **@BotFather**
2. Send it: `/newbot`
3. Follow the prompts — give your bot a name like `NassauWatchdog`
4. BotFather will give you a **bot token** (looks like `1234567890:ABCdef...`)
   → **Copy and save this. You'll need it in Step 3.**

### STEP 2 — Create Your Telegram Channel and Get Its ID

1. In Telegram, create a new **Channel** (e.g. "Nassau Housing Watch")
2. Add your bot as an **Administrator** of that channel
3. Post any message to the channel
4. Visit this URL in your browser (replace YOUR_TOKEN):
   ```
   https://api.telegram.org/botYOUR_TOKEN/getUpdates
   ```
5. Look for `"chat":{"id":` — the number after it is your **Chat ID**
   (for channels it will be a negative number like `-1001234567890`)
   → **Copy this too.**

### STEP 3 — Set Up the GitHub Repository

1. Go to [github.com](https://github.com) and create a **free account** if you don't have one
2. Click **"New repository"** → name it `nassau-watchdog` → set to **Private**
3. Upload all files from this project to the repo (drag and drop works)
4. Make sure the folder structure looks like this:
   ```
   nassau-watchdog/
   ├── .github/
   │   └── workflows/
   │       └── watchdog.yml
   ├── main.py
   ├── config.py
   ├── scrapers.py
   ├── state_manager.py
   ├── notifier.py
   ├── requirements.txt
   └── seen_items.json
   ```

### STEP 4 — Add Your Secret Credentials to GitHub

*This keeps your bot token out of the code (important for security).*

1. In your GitHub repo, click **Settings** → **Secrets and variables** → **Actions**
2. Click **"New repository secret"** and add:
   - Name: `TELEGRAM_TOKEN` → Value: your bot token from Step 1
   - Name: `TELEGRAM_CHAT_ID` → Value: your chat ID from Step 2

### STEP 5 — Enable GitHub Actions

1. Click the **Actions** tab in your repo
2. If prompted, click **"I understand my workflows, go ahead and enable them"**
3. To do a test run immediately: click your workflow → **"Run workflow"**

That's it! 🎉 The bot will now run every morning at 8 AM and send you alerts.

---

## Customization

### Add/remove keywords
Edit the `KEYWORDS` list in `config.py`.

### Add a new source to watch
Add an entry to the `SOURCES` list in `config.py`:
```python
{
    "name": "Your Source Name",
    "url": "https://example.com/page-to-watch",
    "type": "html",
},
```

### Change the schedule
Edit the `cron` line in `.github/workflows/watchdog.yml`.
Use [crontab.guru](https://crontab.guru) to build a schedule.

### Add more subscribers
Invite people to your Telegram channel. Everyone in the channel gets the alerts.

---

## How the "No Duplicates" System Works

After each run, the script saves fingerprints of everything it found to
`seen_items.json` and commits that file back to your repo. The next day,
it only alerts you about items it has **never seen before**. This means:
- First run will send a lot of alerts (everything is "new")
- After that, only genuinely new content triggers alerts

---

## Troubleshooting

| Problem | Fix |
|---|---|
| No alerts on first run | Check the Actions tab for error logs |
| "Telegram send failed" | Double-check your secrets in GitHub Settings |
| Bot can't post to channel | Make sure the bot is an Admin of the channel |
| A website isn't being scraped | Some sites block bots; check the Actions log for `[WARN]` messages |

---

## Project Files

| File | Purpose |
|---|---|
| `main.py` | Entry point — runs the full pipeline |
| `config.py` | All keywords and source URLs (edit this!) |
| `scrapers.py` | Fetches each URL and finds keyword matches |
| `state_manager.py` | Tracks what's been seen to avoid duplicates |
| `notifier.py` | Formats and sends Telegram messages |
| `seen_items.json` | Auto-updated "database" of seen items |
| `.github/workflows/watchdog.yml` | GitHub Actions automation schedule |
