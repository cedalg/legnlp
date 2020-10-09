# flask_web/app.py

from flask import Flask, request, render_template
from scrap.scrap import récupérerDonnées, créationDataFrame, save_csv
from bdd.mongodb import connexion_mongoDB, récupérer_les_données
from model.nlp import traitement, cosine_sim, resultat
from mdp import nom_utilisateur, mdp, nom_base_de_donnée, keywords
import pandas as pd

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my-form.html')

#@app.route("/", methods=['POST'])
#def analyse():
#    keywords = request.form["text"]
#    liste_tribunal, liste_formation, liste_dates, liste_numéro, liste_rapporteur, liste_rapporteur_public, liste_avocats, liste_décision= récupérerDonnées(keywords)
#    df = créationDataFrame(liste_tribunal, liste_formation, liste_dates, liste_numéro, liste_rapporteur, liste_rapporteur_public, liste_avocats, liste_décision)
#    df = save_csv(df, keywords)
#    df = connexion_mongoDB(nom_utilisateur, mdp, nom_base_de_donnée, df)
#    df = récupérer_les_données(nom_utilisateur, mdp, nom_base_de_donnée, keywords)
#    df = traitement(df, keywords)
#    cas_personnel = request.form["text1"]
#    df, ligne, score = cosine_sim(df, cas_personnel)
#    result, jp_proche, score = resultat(df, ligne, score)
#    return result, jp_proche, score

@app.route("/resultat")
def affichage_resultat():
    #keywords = request.form["text"]
    #cas_personnel = request.form["text1"]
    cas_personnel = "j'ai été viré pour avoir pris accepté un pot de vin pour l'obtention d'un marché public"
    #liste_tribunal, liste_formation, liste_dates, liste_numéro, liste_rapporteur, liste_rapporteur_public, liste_avocats, liste_décision= récupérerDonnées(keywords)
    #df = créationDataFrame(liste_tribunal, liste_formation, liste_dates, liste_numéro, liste_rapporteur, liste_rapporteur_public, liste_avocats, liste_décision)
    #df = save_csv(df, keywords)
    #df = connexion_mongoDB(nom_utilisateur, mdp, nom_base_de_donnée, df)
    df = récupérer_les_données(nom_utilisateur, mdp, nom_base_de_donnée, keywords)
    df = traitement(df, keywords)
    df, ligne, score = cosine_sim(df, cas_personnel)
    result, jp_proche, score = resultat(df, ligne, score)
    return render_template('resultat.html', tables=[df.head().to_html(classes='data')], titles=df.columns.values, result=result, jp_proche=jp_proche, score=score)

if __name__ == '__main__':
    app.run(debug=True)


