from classement import generer_classement


NOMS_COURTS = {
    "Lille OSC": "LILLE",
    "AS Monaco FC": "MONACO",
    "Stade Rennais FC 1901": "RENNES",
    "Olympique Lyonnais": "LYON",
    "Paris FC": "PARIS FC",
    "RC Strasbourg Alsace": "STRASBOURG",
    "Paris Saint-Germain FC": "PSG",
    "Stade Brestois 29": "BREST",
    "FC Lorient": "LORIENT",
    "Racing Club de Lens": "LENS",
    "Angers SCO": "ANGERS",
    "ES Troyes AC": "TROYES",
    "Olympique de Marseille": "MARSEILLE",
    "Le Mans FC": "LE MANS",
    "AJ Auxerre": "AUXERRE",
    "Le Havre AC": "LE HAVRE",
    "Toulouse FC": "TOULOUSE",
    "OGC Nice": "NICE"
}

LOGOS_PERSONALISES = {
    "Le Mans FC" : "logos_fixes/LeMansFC.png"
}


generer_classement(
    "FL1",
    "ligue_1",
    NOMS_COURTS,
    LOGOS_PERSONALISES
)