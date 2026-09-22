import os
import requests
import pandas as pd
from dotenv import load_dotenv
from PIL import Image

# charger la cle API depuis .env
load_dotenv()

API_KEY = os.getenv("FOOTBALL_API_KEY")

if not API_KEY:
    print("ERROR : Schlüssel API nicht in die Datei .env")
    exit()


# Premier League
url = "https://api.football-data.org/v4/competitions/PD/standings"

headers = {
    "X-Auth-Token": API_KEY
}

print("Recuperation du classement Premier League ...")#

reponse = requests.get(url, headers=headers)

if reponse.status_code != 200:
    print("Error API : ", reponse.status_code)
    print(reponse.text)
    exit()

data = reponse.json()

# Recuperation du classement general
table = data["standings"][0]["table"]

classement = []

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

for club in table:
    classement.append({
        "POS": club["position"],
        "CLUB": NOMS_COURTS.get(
            club["team"]["name"],
            club["team"]["name"].upper()
        ),
        "PTS": club["points"],
        "MJ": club["playedGames"],
        "DB": club["goalDifference"],
        "LOGO": club["team"]["crest"]
    })

    df = pd.DataFrame(classement)
    print("\n CLASSEMENT PREMIER LEAGUE\n")
    print(df[["POS", "CLUB", "PTS", "MJ", "DB"]])


# ==========================================
# TELECHARGEMENT DES LOGOS
# ==========================================

dossier_logos = "data/logos"

os.makedirs(dossier_logos, exist_ok=True)

print("\nTéléchargement des logos...")

for index, club in enumerate(classement, start=1):

    logo_url = club["LOGO"]

    response_logo = requests.get(logo_url)

    if response_logo.status_code == 200:

        chemin_logo = f"{dossier_logos}/LOGO_{index}.png"

        with open(chemin_logo, "wb") as fichier:
            fichier.write(response_logo.content)

        print(
            f"LOGO_{index} -> {club['CLUB']}"
        )

    else:
        print(
            f"Erreur logo : {club['CLUB']}"
        )


# 
# creation du csv pour canva
#

canva_data = {}

for index, club in enumerate(classement, start=1):
    # Ajouter + devant une difference positive
    difference = club["DB"]

    if difference > 0:
        difference = f"+{difference}"
    elif difference == 0:
        difference = "0"

    canva_data[f"POS_{index}"] = club["POS"]
    canva_data[f"CLUB_{index}"] = club["CLUB"]
    canva_data[f"PTS_{index}"] = club["PTS"]
    canva_data[f"MJ_{index}"] = club["MJ"]
    canva_data[f"DB_{index}"] = difference
    

# Une ligne = une affiche complete
df_canva = pd.DataFrame([canva_data])

df_canva.to_csv(
    "data/premier_league_canva.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\n Fichier Canva cree  !")
print("data/premier_league_canva.csv")

# ==========================================
# URLS DES LOGOS POUR CANVA
# ==========================================

logos_canva = []

for index, club in enumerate(classement, start=1):
    logos_canva.append({
        "FIELD": f"LOGO_{index}",
        "CLUB": club["CLUB"],
        "URL": club["LOGO"]
    })

df_logos = pd.DataFrame(logos_canva)

df_logos.to_csv(
    "data/logos_canva.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nFichier des logos Canva créé !")
print("data/logos_canva.csv")

# ==========================================
# CREATION DE LA COLONNE DES 20 LOGOS
# ==========================================

from PIL import Image

largeur = 150

hauteur_ligne = 90
nombre_clubs = 20

hauteur = hauteur_ligne * nombre_clubs

# Image transparente
image_finale = Image.new(
    "RGBA",
    (largeur, hauteur),
    (255, 255, 255, 0)
)

taille_logo = 60

for index in range(1, nombre_clubs + 1):

    chemin_logo = f"data/logos/LOGO_{index}.png"

    logo = Image.open(chemin_logo).convert("RGBA")

    # Le logo conserve ses proportions
    logo.thumbnail(
        (taille_logo, taille_logo)
    )

    # Centrage horizontal
    x = (largeur - logo.width) // 2

    # Centrage dans chaque ligne
    y = (
        (index - 1) * hauteur_ligne
        + (hauteur_ligne - logo.height) // 2
    )

    image_finale.paste(
        logo,
        (x, y),
        logo
    )

image_finale.save(
    "data/logos_classement.png"
)

print("Colonne des logos créée !")
print("data/logos_classement.png")