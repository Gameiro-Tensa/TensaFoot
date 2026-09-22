import os
import requests
import pandas as pd
from dotenv import load_dotenv
from PIL import Image


load_dotenv()

API_KEY = os.getenv("FOOTBALL_API_KEY")


def generer_classement(code_competition, nom_dossier, noms_courts, logos_personalises=None):

    if logos_personalises is None:
        logos_personalises = {}

    if not API_KEY:
        print("ERREUR : clé API introuvable dans le fichier .env")
        return

    url = (
        f"https://api.football-data.org/v4/"
        f"competitions/{code_competition}/standings"
    )

    headers = {
        "X-Auth-Token": API_KEY
    }

    print(f"\nRécupération du classement : {nom_dossier}")

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Erreur API :", response.status_code)
        print(response.text)
        return

    data = response.json()

    table = data["standings"][0]["table"]

    classement = []

    for club in table:

        nom_api = club["team"]["name"]

        logo = logos_personalises.get(
            nom_api,
            club["team"]["crest"]
        )

        classement.append({
            "POS": club["position"],
            "CLUB": noms_courts.get(
                nom_api,
                nom_api.upper()
            ),
            "PTS": club["points"],
            "MJ": club["playedGames"],
            "DB": club["goalDifference"],
            "LOGO": logo
        })

    # Toujours remettre les clubs dans l'ordre du classement ok
    classement.sort(
        key=lambda club: club["POS"]
    )

    df = pd.DataFrame(classement)

    print("\nCLASSEMENT\n")
    print(df[["POS", "CLUB", "PTS", "MJ", "DB"]])

    # =========================
    # DOSSIERS
    # =========================

    dossier_data = f"data/{nom_dossier}"
    dossier_logos = f"{dossier_data}/logos"

    os.makedirs(
        dossier_logos,
        exist_ok=True
    )

    # =========================
    # CSV CANVA
    # =========================

    canva_data = {}

    for index, club in enumerate(
        classement,
        start=1
    ):

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

    df_canva = pd.DataFrame(
        [canva_data]
    )

    fichier_csv = (
        f"{dossier_data}/"
        f"{nom_dossier}_canva.csv"
    )

    df_canva.to_csv(
        fichier_csv,
        index=False,
        encoding="utf-8-sig"
    )

    print("\nCSV Canva créé :")
    print(fichier_csv)

    # =========================
    # TELECHARGEMENT LOGOS
    # =========================

# =========================
# TELECHARGEMENT LOGOS
# =========================

    print("\nTéléchargement des logos...")

    for index, club in enumerate(
    classement,
    start=1
    ):

        logo_source = club["LOGO"]

        chemin_logo = (
            f"{dossier_logos}/"
            f"LOGO_{index}.png"
        )

        # =========================
        # LOGO LOCAL
        # =========================

        if os.path.exists(logo_source):

            try:
                logo = Image.open(
                    logo_source
                ).convert("RGBA")

                logo.save(
                    chemin_logo,
                    "PNG"
                )

                print(
                    f"LOGO_{index} -> "
                    f"{club['CLUB']} "
                    f"(logo personnalisé)"
                )

            except Exception as e:
                print(
                    f"ERREUR LOGO_{index} -> "
                    f"{club['CLUB']} | {e}"
                )

        # =========================
        # LOGO INTERNET
        # =========================

        else:

            try:
                response_logo = requests.get(
                    logo_source
                )

                if response_logo.status_code == 200:

                    with open(
                        chemin_logo,
                        "wb"
                    ) as fichier:

                        fichier.write(
                            response_logo.content
                        )

                    print(
                        f"LOGO_{index} -> "
                        f"{club['CLUB']}"
                    )

                else:

                    print(
                        f"ERREUR LOGO_{index} -> "
                        f"{club['CLUB']} | "
                        f"HTTP {response_logo.status_code}"
                    )

                    print(
                        f"URL : {logo_source}"
                    )

            except Exception as e:

                print(
                    f"ERREUR LOGO_{index} -> "
                    f"{club['CLUB']} | {e}"
                )

    # =========================
    # IMAGE VERTICALE LOGOS
    # =========================

    largeur = 150
    hauteur_ligne = 90
    taille_logo = 60

    nombre_clubs = len(classement)

    hauteur = (
        hauteur_ligne
        * nombre_clubs
    )

    image_finale = Image.new(
        "RGBA",
        (largeur, hauteur),
        (255, 255, 255, 0)
    )

    for index in range(
        1,
        nombre_clubs + 1
    ):

        chemin_logo = (
            f"{dossier_logos}/"
            f"LOGO_{index}.png"
        )


        if not os.path.exists(chemin_logo):
            print(
                f"Logo manquant : LOGO_{index}.png"
            )
            continue

        logo = Image.open(
            chemin_logo
        ).convert("RGBA")

        logo.thumbnail(
            (taille_logo, taille_logo)
        )

        x = (
            largeur - logo.width
        ) // 2

        y = (
            (index - 1) * hauteur_ligne
            + (
                hauteur_ligne
                - logo.height
            ) // 2
        )

        image_finale.paste(
            logo,
            (x, y),
            logo
        )

    fichier_logos = (
        f"{dossier_data}/"
        f"logos_classement.png"
    )

    image_finale.save(
        fichier_logos
    )

    print("\nImage logos créée :")
    print(fichier_logos)