# ============================================================
# Nassau County Housing Development Watchdog - Configuration
# Full Nassau County Coverage — All Towns, Villages, & News
# ============================================================

import os
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")

# --- KEYWORDS TO WATCH FOR ---
KEYWORDS = [
    # Zoning / development types
    "multifamily", "multi-family", "high density", "high-density",
    "mixed use", "mixed-use", "transit oriented", "transit-oriented",
    "TOD", "upzoning", "up-zoning", "rezoning", "re-zoning",
    "accessory dwelling", "ADU", "overlay district",
    "planned unit development", "PUD", "cluster development",

    # Legal / regulatory
    "SEQRA", "zoning variance", "zoning amendment", "zoning change",
    "special use permit", "affordable housing overlay",
    "housing access voucher", "Fair Housing",
    "comprehensive plan", "master plan update",
    "home rule", "home-rule override", "zoning preemption",
    "General Project Plan", "Empire State Development",

    # NYS-specific programs
    "485-a", "485-b", "421-a", "421a", "421g",
    "Pro-Housing", "housing compact", "City of Yes",
    "Governor Hochul", "New York Housing Compact",
    "LIRR station area", "station area planning",
    "housing budget", "housing in the budget",

    # Generic density signals
    "apartment complex", "mixed income", "workforce housing",
    "200 units", "300 units", "400 units", "500 units",
    "six stories", "seven stories", "eight stories",
    "affordable units", "below market rate",
]

# --- SOURCES TO SCRAPE ---
SOURCES = [

    # ================================================================
    # TOWN GOVERNMENTS (govern unincorporated areas + oversee villages)
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
    # SOUTH SHORE VILLAGES — LIRR West Hempstead/Long Beach Branch
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
        "name": "Village of Valley Stream - Planning/Zoning",
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
        "name": "Village of Baldwin - Civic News",
        "url": "https://www.baldwinny.gov/",
        "type": "html",
    },
    {
        "name": "Village of Oceanside - Community Board",
        "url": "https://www.nassaucountyny.gov/2092/Oceanside",
        "type": "html",
    },
    {
        "name": "Village of Hewlett - Board",
        "url": "https://www.villageofhewlett.org/",
        "type": "html",
    },
    {
        "name": "Village of Woodmere - Board",
        "url": "https://www.woodmere.us/",
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
        "name": "Village of Hewlett Bay Park - Board",
        "url": "https://www.hewlettbaypark.com/",
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
    # CENTRAL NASSAU — LIRR Main Line Corridor (HIGH PRIORITY — TOD)
    # ================================================================

    {
        "name": "Village of Garden City - Board Agendas",
        "url": "https://www.gardencityny.net/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Village of Garden City - Planning/Zoning",
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
        "name": "Village of Westbury - Zoning Board",
        "url": "https://www.westburyny.gov/160/Zoning-Board-of-Appeals",
        "type": "html",
    },
    {
        "name": "Village of Carle Place - News",
        "url": "https://www.nassaucountyny.gov/2067/Carle-Place",
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
    {
        "name": "Village of Stewart Manor - Board",
        "url": "https://www.stewartmanor.org/",
        "type": "html",
    },
    {
        "name": "Village of Elmont - Community Board",
        "url": "https://www.nassaucountyny.gov/2078/Elmont",
        "type": "html",
    },

    # ================================================================
    # NORTH SHORE — Great Neck, Port Washington, Manhasset Area
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
        "name": "Village of Great Neck Estates - Board",
        "url": "https://www.greatneckestates.net/",
        "type": "html",
    },
    {
        "name": "Village of Manhasset - Community Board",
        "url": "https://www.nassaucountyny.gov/2088/Manhasset",
        "type": "html",
    },
    {
        "name": "Village of Port Washington - Community Board",
        "url": "https://www.nassaucountyny.gov/2097/Port-Washington",
        "type": "html",
    },
    {
        "name": "Village of Roslyn - Board Agendas",
        "url": "https://www.roslynvillage.com/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Village of Roslyn Heights - Community Board",
        "url": "https://www.nassaucountyny.gov/2100/Roslyn-Heights",
        "type": "html",
    },
    {
        "name": "Village of Sands Point - Board",
        "url": "https://www.sandspointvillage.org/",
        "type": "html",
    },
    {
        "name": "Village of Kings Point - Board",
        "url": "https://www.kingspoint.org/",
        "type": "html",
    },
    {
        "name": "Village of Lake Success - Board",
        "url": "https://www.lakesuccess.com/",
        "type": "html",
    },

    # ================================================================
    # EAST NASSAU — Hicksville, Levittown, Plainview, Bethpage Area
    # (LIRR Main & Oyster Bay Branch — HIGH PRIORITY — TOD)
    # ================================================================

    {
        "name": "Hicksville Community - Nassau County Board",
        "url": "https://www.nassaucountyny.gov/2082/Hicksville",
        "type": "html",
    },
    {
        "name": "Levittown Community - Nassau County Board",
        "url": "https://www.nassaucountyny.gov/2086/Levittown",
        "type": "html",
    },
    {
        "name": "Village of Bethpage - Community Board",
        "url": "https://www.nassaucountyny.gov/2063/Bethpage",
        "type": "html",
    },
    {
        "name": "Village of Plainview - Community Board",
        "url": "https://www.nassaucountyny.gov/2096/Plainview",
        "type": "html",
    },
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
        "name": "Village of Syosset - Community Board",
        "url": "https://www.nassaucountyny.gov/2105/Syosset",
        "type": "html",
    },
    {
        "name": "Village of Jericho - Community Board",
        "url": "https://www.nassaucountyny.gov/2084/Jericho",
        "type": "html",
    },
    {
        "name": "Village of Oyster Bay - Board Agendas",
        "url": "https://www.oysterbayvillage.net/AgendaCenter",
        "type": "html",
    },
    {
        "name": "Village of East Meadow - Community Board",
        "url": "https://www.nassaucountyny.gov/2074/East-Meadow",
        "type": "html",
    },
    {
        "name": "Village of Uniondale - Community Board",
        "url": "https://www.nassaucountyny.gov/2108/Uniondale",
        "type": "html",
    },
    {
        "name": "Village of Hempstead - Board Agendas",
        "url": "https://www.villageofhempstead.org/AgendaCenter",
        "type": "html",
    },

    # ================================================================
    # NYS GOVERNOR'S OFFICE
    # ================================================================

    {
        "name": "Governor Hochul - Press Releases",
        "url": "https://www.governor.ny.gov/news",
        "type": "html",
    },
    {
        "name": "Governor Hochul - Pro-Housing Communities",
        "url": "https://www.governor.ny.gov/programs/pro-housing-communities",
        "type": "html",
    },

    # ================================================================
    # NYS LEGISLATURE
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
        "name": "NY Senate - Housing Density Bills",
        "url": "https://www.nysenate.gov/legislation/bills/2025?search=housing+density+multifamily",
        "type": "html",
    },
    {
        "name": "NY Senate - Zoning Bills",
        "url": "https://www.nysenate.gov/legislation/bills/2025?search=zoning+affordable+housing",
        "type": "html",
    },
    {
        "name": "NY Senate - TOD Long Island Bills",
        "url": "https://www.nysenate.gov/legislation/bills/2025?search=transit+oriented+development+Long+Island",
        "type": "html",
    },
    {
        "name": "NY Senate - Home Rule Override Bills",
        "url": "https://www.nysenate.gov/legislation/bills/2025?search=home+rule+zoning+override",
        "type": "html",
    },

    # ================================================================
    # NYS AGENCIES
    # ================================================================

    {
        "name": "NYS Department of State - Pro-Housing",
        "url": "https://dos.ny.gov/pro-housing-communities",
        "type": "html",
    },
    {
        "name": "Empire State Development - Press Releases",
        "url": "https://esd.ny.gov/esd-media-center/press-releases",
        "type": "html",
    },

    # ================================================================
    # LOCAL & REGIONAL NEWS
    # ================================================================

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
        "name": "LI Herald - Malverne/West Hempstead",
        "url": "https://www.liherald.com/malverne/",
        "type": "html",
    },
    {
        "name": "LI Herald - Valley Stream",
        "url": "https://www.liherald.com/valleystream/",
        "type": "html",
    },
    {
        "name": "LI Herald - Baldwin",
        "url": "https://www.liherald.com/baldwin/",
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
        "name": "LI Herald - Floral Park",
        "url": "https://www.liherald.com/floralpark/",
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
        "name": "Blank Slate Media - North Shore News",
        "url": "https://www.blankslatemedia.com/",
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
        "name": "Newsday - Long Island Development",
        "url": "https://www.newsday.com/search/development+rezoning+long+island#",
        "type": "html",
    },
    {
        "name": "Long Island Business News - Development",
        "url": "https://libn.com/category/real-estate/",
        "type": "html",
    },
]
