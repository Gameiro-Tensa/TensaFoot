from classement import generer_classement


NOMS_COURTS = {
    "Manchester City FC": "MAN CITY",
    "Manchester United FC": "MAN UNITED",
    "Arsenal FC": "ARSENAL",
    "Chelsea FC": "CHELSEA",
    "Liverpool FC": "LIVERPOOL",
    "Newcastle United FC": "NEWCASTLE",
    "Everton FC": "EVERTON",
    "Leeds United FC": "LEEDS UNITED",
    "Brighton & Hove Albion FC": "BRIGHTON",
    "Sunderland AFC": "SUNDERLAND",
    "Crystal Palace FC": "CRYSTAL PALACE",
    "Ipswich Town FC": "IPSWICH TOWN",
    "AFC Bournemouth": "BOURNEMOUTH",
    "Nottingham Forest FC": "NOTTINGHAM",
    "Aston Villa FC": "ASTON VILLA",
    "Tottenham Hotspur FC": "TOTTENHAM",
    "Fulham FC": "FULHAM",
    "Coventry City FC": "COVENTRY",
    "Hull City AFC": "HULL CITY",
    "Brentford FC": "BRENTFORD"
}


generer_classement(
    "PL",
    "premier_league",
    NOMS_COURTS
)