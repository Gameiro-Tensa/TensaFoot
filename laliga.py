from classement import generer_classement


NOMS_COURTS = {
    "FC Barcelona": "BARCELONA",
    "Deportivo Alavés": "ALAVÉS",
    "Sevilla FC": "SEVILLA",
    "Real Madrid CF": "REAL MADRID",
    "Real Betis Balompié": "REAL BETIS",
    "RC Deportivo La Coruña": "DEPORTIVO",
    "Club Atlético de Madrid": "ATLETICO",
    "CA Osasuna": "OSASUNA",
    "Real Sociedad de Fútbol": "REAL SOCIEDAD",
    "Athletic Club": "ATHLETIC CLUB",
    "Levante UD": "LEVANTE",
    "RCD Espanyol de Barcelona": "ESPANYOL",
    "Real Racing Club de Santander": "RACING",
    "Rayo Vallecano de Madrid": "RAYO VALLECANO",
    "Getafe CF": "GETAFE",
    "RC Celta de Vigo": "CELTA VIGO",
    "Villarreal CF": "VILLARREAL",
    "Málaga CF": "MÁLAGA",
    "Elche CF": "ELCHE",
    "Valencia CF": "VALENCIA"
}


generer_classement(
    "PD",
    "laliga",
    NOMS_COURTS
)