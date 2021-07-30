Job_title_domain_classification
==============================
L'objectif est de construire un système prenant en entrée une série d'intitulés de profils professionnels. En sortie, on veut retrouver cette même série avec pour chaque titre, un champ supplémentaire true, false ou non défini selon si le profil concerne le marché de la tech ou non.

## Methodologie

Quelques prétraitements (cleaning) sur le texte assez basique (lowercase, suppression des accents et retrait des entreprises (finalement pas si utile))

### 1e approche
- Approche basée sur un dictionnaire regroupant des termes afin d'identifier facilement si le profil est du marché de la tech

Avantages :
- simple d'implémentation 
- résultats plus que corrects pour une V1

Inconvénients:
- résultats dépendent de la maturité du dictionnaire construit
- maintenabilité du dictionnaire dans le temps

Quelques précisions:
- Dictionnaire construit à partir de quelques termes inscrits en dur + 1 fichier csv issu d'un scrapping des noms de technos (scrap_tech_voc.csv)
- Cas des étudiants traités particulièrement dans cet V1 (Non défini pour l'instant pour la plupart) car nécessité de réaliser un dictionnaire propre aux noms des écoles (probablement)

Conclusions:
- Pour une V1, avec un dictionnaire peu mature (qqls noms de jobs techs + noms de technos scrappés), on atteint 80% de bonnes classifications. J'ai du labélisé à la mano T_T 600-650 lignes du fichier Titres_profils.csv afin d'évaluer la performance de la logic rule
- PS: Il doit y avoir quelques erreurs dans la labelisation à la mano des jobs tech (labelisation à la mano = fastidieux & chronophage)

### 2e approche (à venir)
- Dans un 2nd temps, j'aimerais me baser sur le lien en référence (un article de blog octo). L'idée est d'accentuer un peu le cleaning sur le format texte (retrait des stopwords au minimun)
- Puis d'aborder le sujet avec une approche séquentielle, dans un 1er temps, (BOW - utilisation des ngrams pour voir si capter un contexte de 2/3 mots peut être pertinent pour la classification / approche TF-IDF, countvectorizer)
- Comme les données ne sont pas labelisées, on pourrait essayer avec la logic rule de les labeliser automatiquement / le pb est qu'entrainer un modèle sur ce format revient à demander au modèle de comprendre la logic rule (modulo quelques ajustements en fonction des autres mots dans les titres du profil)
- Ca aurait été intéressant de comparer une approche ML/DL avec la logic rule à condition d'avoir une labelisation des titres de profils controlée par un humaine au préalable 
- Une approche non supervisée ? (mouais ...)

### Quelques notes sur cet exercice
- La plus grande contrainte : une 1è labelisation à la mano 
- On a du vocabulaire français et anglais (en théorie, il faudrait donc inscrire dans le dictionnaire les termes anglais également - sinon effectuer une traduction ou, pr une V1, ne s'occuper que des titres de profils français que l'on aurait pu détecter grâce à du fasttext)


## Requirements
- Python >= 3.8

## Local development

    # Install & run main.py
    virtualenv -p python3.8 venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    make run

## References
- [blog.octo.com](https://blog.octo.com/nlp-une-classification-multilabels-simple-efficace-et-interpretable/)



# TO DO
- Improve quality code : implement unit test, function refactoring, deal with data paths, ...
- Docker + github actions (personal) 
- Clean all csv stored 
- construct a ML model on these labeled data to see performance
- Improve readme