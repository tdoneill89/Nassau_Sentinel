# ============================================================
# Nassau County Housing Development Watchdog - Configuration
# ============================================================
# Edit this file to add/remove keywords, sources, or towns.

# --- TELEGRAM SETTINGS ---
# Set these as GitHub Secrets (see README). Do NOT paste them here.
import os
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")

# --- KEYWORDS TO WATCH FOR ---
# The scraper will alert if ANY of these appear in new content.
KEYWORDS = [
    # Zoning / development types
    "multifamily", "multi-family", "high density", "high-density",
    "mixed use", "mixed-use", "transit oriented", "transit-oriented",
    "TOD", "upzoning", "up-zoning", "rezoning", "re-zoning",
    "accessory dwelling", "ADU",

    # Legal / regulatory
    "SEQRA", "zoning variance", "zoning amendment", "zoning change",
    "special use permit", "affordable housing overlay",
    "housing access voucher", "Fair Housing",

    # NYS-specific programs
    "485-a", "485-b", "421-a", "421a", "421g",
    "Pro-Housing", "housing compact", "City of Yes",
    "Governor Hochul", "New York Housing Compact",

    # Generic density signals
    "apartment complex", "mixed income", "workforce housing",
    "200 units", "300 units", "400 units", "500 units",
    "six stories", "seven stories", "eight stories",
]

# --- SOURCES TO SCRAPE ---
SOURCES = [
    # ---- TOWN WEBSITES ----
    {
        "name": "Village of Lynbrook - Board Agendas",
        "url": "https://www.lynbrook.org/village-board/agendas-minutes",
        "type": "html",
    },
    {
        "name": "Village of Rockville Centre - Board Agendas",
        "url": "https://www.rvcny.gov/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Village of Malverne - Board Meetings",
        "url": "https://www.malvernevillage.org/board-of-trustees",
        "type": "html",
    },
    {
        "name": "Town of Hempstead - Zoning Board",
        "url": "https://www.toh.li/zoning-board",
        "type": "html",
    },

    # ---- NASSAU COUNTY PLANNING ----
    {
        "name": "Nassau County Planning Commission",
        "url": "https://www.nassaucountyny.gov/agencies/Planning/meetingdocs.html",
        "type": "html",
    },
    {
        "name": "Nassau County Legislature - Agenda",
        "url": "https://www.nassaucountyny.gov/agencies/Legislature/index.html",
        "type": "html",
    },

    # ---- NYS LEGISLATION ----
    {
        "name": "NY Senate - Housing Bills Search",
        "url": "https://www.nysenate.gov/legislation/bills/2025?search=housing+density+multifamily",
        "type": "html",
    },
    {
        "name": "NY Senate - Zoning Bills Search",
        "url": "https://www.nysenate.gov/legislation/bills/2025?search=zoning+affordable+housing",
        "type": "html",
    },

    # ---- LOCAL NEWS ----
    {
        "name": "LI Herald - Lynbrook/East Rockaway",
        "url": "https://www.liherald.com/lynbrook/",
        "type": "html",
    },
    {
        "name": "LI Herald - Rockville Centre",
        "url": "https://www.liherald.com/rockvillecentre/",
        "type": "html",
    },
    {
        "name": "LI Herald - Malverne",
        "url": "https://www.liherald.com/malverne/",
        "type": "html",
    },
    {
        "name": "Blank Slate Media - Local Government",
        "url": "https://www.blankslatemedia.com/category/government/",
        "type": "html",
    },
    {
        "name": "Newsday - Long Island Housing",
        "url": "https://www.newsday.com/search/housing+zoning+nassau#",
        "type": "html",
    },
]
