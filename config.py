# ============================================================
# Nassau County Housing Development Watchdog - Configuration
# Full Nassau County Coverage — All Towns, Villages, & News
# ============================================================

import os
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

# --- KEYWORDS TO WATCH FOR ---
# Focused on actual construction/development proposals of 3+ units in Nassau County.
# Removed broad political keywords to reduce noise.
KEYWORDS = [

    # --- Multi-family construction (the core target) ---
    "multifamily", "multi-family",
    "apartment", "apartments", "apartment complex",
    "condominium", "condominiums", "condo development",
    "townhouse development", "townhomes",
    "mixed use", "mixed-use",
    "residential units", "dwelling units",
    "100 units", "150 units", "200 units", "300 units", "400 units", "500 units",
    "story building", "story residential",

    # --- Density & zoning changes ---
    "upzoning", "up-zoning",
    "rezoning", "re-zoning",
    "zoning change", "zoning amendment", "zoning variance",
    "overlay district", "housing overlay",
    "planned unit development", "PUD",
    "accessory dwelling", "ADU",
    "transit oriented", "transit-oriented", "TOD",
    "LIRR station area", "station area planning",
    "high density", "high-density",
    "density bonus",

    # --- Legal & approval process ---
    "SEQRA",
    "site plan approval",
    "special use permit",
    "comprehensive plan update", "master plan update",
    "affordable housing overlay",
    "below market rate", "affordable units",
    "workforce housing", "mixed income",

    # --- NYS mandates that override local zoning ---
    "Pro-Housing Community",
    "New York Housing Compact",
    "home rule override", "zoning preemption",
    "General Project Plan",
    "485-a", "485-b", "421-a", "421a",

    # --- Financial incentives tied to density ---
    "payment in lieu", "PILOT",
    "tax abatement",
]

# --- SOURCES TO SCRAPE ---
SOURCES = [

    # ================================================================
    # TOWN GOVERNMENTS
    # ================================================================
    {
        "name": "Town of Hempstead - Board Agendas",
        "url": "https://www.toh.li/town-clerk/agendas-minutes",
        "type": "html",
    },
    {
        "name": "Town of Hempstead - Zoning Board",
        "url": "https://www.toh.li/zoning-board",
        "type": "html",
    },
    {
        "name": "Town of Hempstead - Building Department",
        "url": "https://www.toh.li/building-department",
        "type": "html",
    },
    {
        "name": "Town of North Hempstead - Board Agendas",
        "url": "https://www.northhempsteadny.gov/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Town of North Hempstead - Planning Board",
        "url": "https://www.northhempsteadny.gov/165/Planning-Board",
        "type": "html",
    },
    {
        "name": "Town of North Hempstead - Zoning Board",
        "url": "https://www.northhempsteadny.gov/166/Zoning-Board-of-Appeals",
        "type": "html",
    },
    {
        "name": "Town of Oyster Bay - Board Agendas",
        "url": "https://www.oysterbaytown.com/agendas-minutes/",
        "type": "html",
    },
    {
        "name": "Town of Oyster Bay - Planning Board",
        "url": "https://www.oysterbaytown.com/departments/planning/",
        "type": "html",
    },
    {
        "name": "Town of Oyster Bay - Zoning Board",
        "url": "https://www.oysterbaytown.com/departments/zoning-board-of-appeals/",
        "type": "html",
    },

    # ================================================================
    # NASSAU COUNTY
    # ================================================================
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
    {
        "name": "Nassau County - Press Releases",
        "url": "https://www.nassaucountyny.gov/news",
        "type": "html",
    },

    # ================================================================
    # SOUTH SHORE VILLAGES
    # ================================================================
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
        "name": "Village of Rockville Centre - Planning Board",
        "url": "https://www.rvcny.gov/190/Planning-Board",
        "type": "html",
    },
    {
        "name": "Village of Malverne - Board Meetings",
        "url": "https://www.malvernevillage.org/board-of-trustees",
        "type": "html",
    },
    {
        "name": "Village of Valley Stream - Board Agendas",
        "url": "https://www.valleystream.gov/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Village of Valley Stream - Zoning Board",
        "url": "https://www.valleystream.gov/168/Zoning-Board-of-Appeals",
        "type": "html",
    },
    {
        "name": "Village of Freeport - Board Agendas",
        "url": "https://www.freeportny.gov/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Village of Freeport - Planning Board",
        "url": "https://www.freeportny.gov/175/Planning-Board",
        "type": "html",
    },
    {
        "name": "Village of Lawrence - Board Agendas",
        "url": "https://www.villageoflawrence.com/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Village of Cedarhurst - Board",
        "url": "https://www.cedarhurst.gov/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Village of Long Beach - Board Agendas",
        "url": "https://www.longbeachny.gov/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Village of Long Beach - Planning Board",
        "url": "https://www.longbeachny.gov/167/Planning-Board",
        "type": "html",
    },

    # ================================================================
    # CENTRAL NASSAU — LIRR Main Line (HIGH PRIORITY — TOD targets)
    # ================================================================
    {
        "name": "Village of Garden City - Board Agendas",
        "url": "https://www.gardencityny.net/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Village of Garden City - Planning Board",
        "url": "https://www.gardencityny.net/190/Planning-Board",
        "type": "html",
    },
    {
        "name": "Village of Mineola - Board Agendas",
        "url": "https://www.mineolany.gov/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Village of Mineola - Planning Board",
        "url": "https://www.mineolany.gov/175/Planning-Board",
        "type": "html",
    },
    {
        "name": "Village of Westbury - Board Agendas",
        "url": "https://www.westburyny.gov/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Village of Floral Park - Board Agendas",
        "url": "https://www.floralpark.net/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Village of New Hyde Park - Board Agendas",
        "url": "https://www.newhyideparkny.us/AgendaCenter",
        "type": "html",
    },

    # ================================================================
    # NORTH SHORE
    # ================================================================
    {
        "name": "Village of Great Neck - Board Agendas",
        "url": "https://www.greatneckvillage.org/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Village of Great Neck Plaza - Board Agendas",
        "url": "https://www.greatneckplaza.net/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Village of Roslyn - Board Agendas",
        "url": "https://www.roslynvillage.com/AgendaCenter",
        "type": "html",
    },

    # ================================================================
    # EAST NASSAU — LIRR branches (HIGH PRIORITY — TOD targets)
    # ================================================================
    {
        "name": "Village of Farmingdale - Board Agendas",
        "url": "https://www.farmingdale.org/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Village of Farmingdale - Planning Board",
        "url": "https://www.farmingdale.org/172/Planning-Board",
        "type": "html",
    },
    {
        "name": "Village of Oyster Bay - Board Agendas",
        "url": "https://www.oysterbayvillage.net/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Village of Hempstead - Board Agendas",
        "url": "https://www.villageofhempstead.org/AgendaCenter",
        "type": "html",
    },

    # ================================================================
    # NYS LEGISLATURE — Bills only, no statewide press releases
    # ================================================================
    {
        "name": "NY Senate Housing Committee",
        "url": "https://www.nysenate.gov/committees/housing-construction-and-community-development",
        "type": "html",
    },
    {
        "name": "NY Assembly Housing Committee",
        "url": "https://nyassembly.gov/comm/?id=19",
        "type": "html",
    },
    {
        "name": "NY Senate - Multi-family Housing Bills",
        "url": "https://www.nysenate.gov/legislation/bills/2025?search=multifamily+housing+nassau",
        "type": "html",
    },
    {
        "name": "NY Senate - TOD Long Island Bills",
        "url": "https://www.nysenate.gov/legislation/bills/2025?search=transit+oriented+development+Long+Island",
        "type": "html",
    },
    {
        "name": "NY Senate - Zoning Override Bills",
        "url": "https://www.nysenate.gov/legislation/bills/2025?search=zoning+override+affordable+housing",
        "type": "html",
    },
    {
        "name": "NYS Department of State - Pro-Housing",
        "url": "https://dos.ny.gov/pro-housing-communities",
        "type": "html",
    },

    # ================================================================
    # LOCAL & REGIONAL NEWS
    # ================================================================
    {
        "name": "LI Herald - Lynbrook",
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
        "name": "LI Herald - Valley Stream",
        "url": "https://www.liherald.com/valleystream/",
        "type": "html",
    },
    {
        "name": "LI Herald - Freeport",
        "url": "https://www.liherald.com/freeport/",
        "type": "html",
    },
    {
        "name": "LI Herald - Long Beach",
        "url": "https://www.liherald.com/longbeach/",
        "type": "html",
    },
    {
        "name": "LI Herald - Garden City",
        "url": "https://www.liherald.com/gardencity/",
        "type": "html",
    },
    {
        "name": "LI Herald - Mineola",
        "url": "https://www.liherald.com/mineola/",
        "type": "html",
    },
    {
        "name": "LI Herald - Great Neck",
        "url": "https://www.liherald.com/greatneck/",
        "type": "html",
    },
    {
        "name": "LI Herald - Oyster Bay",
        "url": "https://www.liherald.com/oyster-bay/",
        "type": "html",
    },
    {
        "name": "Blank Slate Media - Local Government",
        "url": "https://www.blankslatemedia.com/category/government/",
        "type": "html",
    },
    {
        "name": "Anton Media - Nassau News",
        "url": "https://www.antonmediagroup.com/category/news/",
        "type": "html",
    },
    {
        "name": "Newsday - Long Island Housing",
        "url": "https://www.newsday.com/search/housing+zoning+nassau#",
        "type": "html",
    },
    {
        "name": "Long Island Business News - Real Estate",
        "url": "https://libn.com/category/real-estate/",
        "type": "html",
    },
]
