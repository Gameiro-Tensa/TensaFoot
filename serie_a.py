from classement import generer_classement


NOMS_COURTS = {
    "AS Roma": "ROMA",
    "FC Internazionale Milano": "INTER MILAN",
    "SS Lazio": "LAZIO",
    "Como 1907": "COMO",
    "AC Milan": "AC MILAN",
    "Juventus FC": "JUVENTUS",
    "Frosinone Calcio": "FROSINONE",
    "Atalanta BC": "ATALANTA",
    "Cagliari Calcio": "CAGLIARI",
    "Udinese Calcio": "UDINESE",
    "US Sassuolo Calcio": "SASSUOLO",
    "SSC Napoli": "NAPOLI",
    "Torino FC": "TORINO",
    "US Lecce": "LECCE",
    "ACF Fiorentina": "FIORENTINA",
    "Bologna FC 1909": "BOLOGNA",
    "Parma Calcio 1913": "PARMA",
    "AC Monza": "MONZA",
    "Genoa CFC": "GENOA",
    "Venezia FC": "VENEZIA"
}


generer_classement(
    "SA",
    "serie_a",
    NOMS_COURTS
)