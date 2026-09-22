from classement import generer_classement


NOMS_COURTS = {
    "FC Bayern München": "BAYERN",
    "Borussia Dortmund": "DORTMUND",
    "RB Leipzig": "LEIPZIG",
    "Bayer 04 Leverkusen": "LEVERKUSEN",
    "Eintracht Frankfurt": "FRANKFURT",
    "VfB Stuttgart": "STUTTGART",
    "SC Freiburg": "FREIBURG",
    "1. FSV Mainz 05": "MAINZ 05",
    "TSG 1899 Hoffenheim": "HOFFENHEIM",
    "1. FC Union Berlin": "UNION BERLIN",
    "Borussia Mönchengladbach": "M'GLADBACH",
    "SV Werder Bremen": "WERDER BREMEN",
    "FC Augsburg": "AUGSBURG",
    "FC Schalke 04": "SCHALKE 04",
    "Hamburger SV": "HAMBURG",
    "1. FC Köln": "KÖLN",
    "SC Paderborn 07": "PADERBORN",
    "SV 07 Elversberg": "ELVERSBERG"
}


generer_classement(
    "BL1",
    "bundesliga",
    NOMS_COURTS
)