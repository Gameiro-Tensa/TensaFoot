import pandas as pd

fichiers = {
    "PL": "data/premier_league/premier_league_canva.csv",
    "LIGA": "data/laliga/laliga_canva.csv",
    "SA": "data/serie_a/serie_a_canva.csv",
    "BL": "data/bundesliga/bundesliga_canva.csv",
    "L1": "data/ligue_1/ligue_1_canva.csv"
}

donnees_finales = {}

for prefixe, chemin in fichiers.items():

    df = pd.read_csv(chemin)

    ligne = df.iloc[0]

    for colonne, valeur in ligne.items():

        nouvelle_colonne = f"{prefixe}_{colonne}"

        donnees_finales[nouvelle_colonne] = valeur


df_final = pd.DataFrame([donnees_finales])

df_final.to_csv(
    "data/classements_canva.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Fichier créé : data/classements_canva.csv")