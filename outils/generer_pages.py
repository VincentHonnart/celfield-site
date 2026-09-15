#!/usr/bin/env python3
"""Génère les pages thématiques de celfield.com.

    python3 outils/generer_pages.py

Pourquoi un générateur : le site n'a pas d'étape de build Netlify (seul `public/`
est publié). Les pages sont donc produites ICI, puis commitées. Un seul gabarit
garantit que l'en-tête, le pied, le fil d'Ariane et les données structurées
restent identiques d'une page à l'autre — huit copies à la main divergeraient
dès la première retouche.

Ce que fait le script :
  1. écrit public/<slug>/index.html pour chaque page de contenu_pages.PAGES ;
  2. remplace, dans public/index.html, le pied de page et la grille « Solutions »
     entre leurs balises <!-- ...:DEBUT --> / <!-- ...:FIN --> ;
  3. réécrit public/sitemap.xml.

Le contenu vit dans contenu_pages.py. Ne rien y affirmer que l'application ne
fait pas : ces pages engagent CelField auprès de prospects.
"""
import datetime, html, json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
from contenu_pages import PAGES, GROUPES  # noqa: E402

RACINE = os.path.join(ICI, '..', 'public')
SITE = 'https://celfield.com'
CSS_V = '3'
AUJOURDHUI = datetime.date.today().isoformat()

COCHE = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#7FC1A0" '
         'stroke-width="3" stroke-linecap="round"><path d="M4 12.5l5 5L20 6.5"/></svg>')
FLECHE = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
          'stroke-width="2.6" stroke-linecap="round"><path d="M5 12h13M13 6l6 6-6 6"/></svg>')
IMAGES = {  # nom -> (largeur, hauteur, texte alternatif)
    'capture-tableau-de-bord.webp': (1360, 850, "Tableau de bord CelField : chiffre d'affaires et commandes"),
    'capture-fiche-pharmacie.webp': (1360, 850, 'Fiche pharmacie CelField avec historique des commandes'),
    'capture-prise-de-commande.webp': (1360, 850, 'Prise de commande CelField : catalogue, quantités et totaux'),
    'capture-trade.webp': (1360, 850, 'Calendrier des opérations commerciales dans CelField'),
    'capture-lecture-ia.webp': (1360, 476, "Dépôt d'un bon de commande pour lecture par l'IA dans CelField"),
}

e = html.escape


def url_page(p):
    return f"{SITE}/{p['slug']}/"


def nav(prefixe_ancres):
    a = prefixe_ancres
    return f'''<nav>
  <div class="wrap">
    <a class="nav-logo" href="/" aria-label="CelField, accueil">
      <img width="346" height="84" src="/assets/img/logo-celfield.png" alt="CelField" style="height:28px;width:auto">
    </a>
    <div class="nav-links">
      <a href="{a}#solutions">Solutions</a>
      <a href="{a}#fonctions">Fonctions</a>
      <a href="/lecture-ia-bon-de-commande/">IA</a>
      <a href="{a}#tarifs">Tarifs</a>
      <a class="nav-cta" href="{a}#demo">Demander une démo</a>
    </div>
  </div>
</nav>'''


def pied():
    cols = []
    for titre, slugs in GROUPES:
        liens = '<br>\n        '.join(
            f'<a href="/{s}/">{e(P[s]["court"])}</a>' for s in slugs)
        cols.append(f'''      <div>
        <div class="foot-h">{e(titre)}</div>
        {liens}
      </div>''')
    cols.append('''      <div>
        <div class="foot-h">CelField</div>
        <a href="/#fonctions">Fonctions</a><br>
        <a href="/#tarifs">Tarifs</a><br>
        <a href="/#apercu">Aperçu</a><br>
        <a href="/#demo">Demander une démo</a>
      </div>''')
    return f'''<!-- PIED:DEBUT (généré par outils/generer_pages.py) -->
<footer>
  <div class="wrap">
    <div class="foot">
      <div>
        <div style="margin-bottom:16px">
          <img width="346" height="84" src="/assets/img/logo-celfield.png" alt="CelField" style="height:34px;width:auto" loading="lazy">
        </div>
        <p>CRM et prise de commande pour les agents commerciaux en pharmacie, parapharmacie, beauté et bien-être.</p>
      </div>
{chr(10).join(cols)}
    </div>
    <div class="foot-bottom">
      <span>© {datetime.date.today().year} CelField · Tous droits réservés</span>
      <span>celfield.com · celfield.fr · celfield.io · celfield.app</span>
    </div>
  </div>
</footer>
<!-- PIED:FIN -->'''


def carte_lien(p):
    return (f'<a class="lien" href="/{p["slug"]}/"><b>{e(p["court"])}</b>'
            f'<span>{e(p["accroche"])}</span><i>Lire la page →</i></a>')


def grille_solutions():
    cartes = '\n      '.join(carte_lien(p) for p in PAGES)
    return f'''<!-- SOLUTIONS:DEBUT (généré par outils/generer_pages.py) -->
<section id="solutions" class="band">
  <div class="wrap">
    <div class="eye">Solutions</div>
    <h2 class="h2">Par besoin, par métier</h2>
    <p class="lead" style="margin-bottom:40px">Prise de commande, mode hors ligne, lecture IA, catalogue des marques : chaque page détaille une partie de CelField et la façon dont elle s'applique à votre secteur.</p>
    <div class="liens">
      {cartes}
    </div>
  </div>
</section>
<!-- SOLUTIONS:FIN -->'''


def figure(nom, legende):
    w, h, alt = IMAGES[nom]
    return f'''<div class="app">
        <div class="app-bar"><i></i><i></i><i></i><div class="app-url">votre-structure.celfield.com</div></div>
        <img width="{w}" height="{h}" src="/assets/img/{nom}" alt="{e(alt)}" fetchpriority="high" style="display:block;width:100%;height:auto">
      </div>
      <p class="app-cap">{e(legende)}</p>'''


def donnees_structurees(p):
    fil = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Accueil", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": p['court'], "item": url_page(p)}]}
    page = {"@context": "https://schema.org", "@type": "WebPage", "name": p['titre'],
            "description": p['description'], "url": url_page(p), "inLanguage": "fr-FR",
            "isPartOf": {"@type": "WebSite", "name": "CelField", "url": SITE + "/"},
            "about": {"@type": "SoftwareApplication", "name": "CelField",
                      "applicationCategory": "BusinessApplication"},
            "primaryImageOfPage": f"{SITE}/assets/img/{p['image']}",
            "dateModified": AUJOURDHUI}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'<[^>]+>', '', r)}}
        for q, r in p['faq']]}
    return json.dumps([fil, page, faq], ensure_ascii=False)


def page_html(p):
    atouts = '\n          '.join(f'<li>{COCHE}<span>{a}</span></li>' for a in p['atouts'])
    faq = '\n      '.join(
        f'<details><summary>{e(q)}</summary><p>{r}</p></details>' for q, r in p['faq'])
    voisins = [P[s] for s in p['voir_aussi']]
    liens = '\n      '.join(carte_lien(v) for v in voisins)
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(p['titre'])}</title>
<meta name="description" content="{e(p['description'])}">
<link rel="canonical" href="{url_page(p)}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#4B6358">
<meta property="og:type" content="article">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="CelField">
<meta property="og:url" content="{url_page(p)}">
<meta property="og:title" content="{e(p['titre'])}">
<meta property="og:description" content="{e(p['description'])}">
<meta property="og:image" content="{SITE}/assets/img/partage-celfield.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{donnees_structurees(p)}</script>
<link rel="icon" type="image/png" sizes="128x128" href="/assets/img/icone-celfield.png">
<link rel="apple-touch-icon" href="/assets/img/icone-celfield.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&family=Geist+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css?v={CSS_V}">
</head>
<body>

{nav('/')}

<header class="hero hero-page">
  <div class="wrap">
    <ol class="fil" aria-label="Fil d'Ariane">
      <li><a href="/">Accueil</a></li>
      <li aria-current="page">{e(p['court'])}</li>
    </ol>
    <div class="hero-txt">
      <div class="hero-tag"><i></i> {e(p['etiquette'])}</div>
      <h1>{p['h1']}</h1>
      <p class="lead">{p['chapo']}</p>
      <div class="btns">
        <a class="btn btn-primary" href="/#demo">Demander une démo {FLECHE}</a>
        <a class="btn btn-ghost" href="/#tarifs">Voir les tarifs</a>
      </div>
    </div>
    <div style="max-width:980px">
      {figure(p['image'], p['legende'])}
    </div>
  </div>
</header>

<main>
<section>
  <div class="wrap">
    <div class="split">
      <div class="prose">
{p['corps']}
      </div>
      <aside class="aside" aria-label="En bref">
        <div class="t">En bref</div>
        <ul>
          {atouts}
        </ul>
        <a class="btn btn-dark" href="/#demo">Voir CelField en démo</a>
      </aside>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="eye">Questions fréquentes</div>
    <h2 class="h2">{e(p['faq_titre'])}</h2>
    <div class="faq" style="margin-top:30px">
      {faq}
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="eye">À lire aussi</div>
    <h2 class="h2">Les autres facettes de CelField</h2>
    <div class="liens" style="margin-top:30px">
      {liens}
    </div>
  </div>
</section>

<section class="dark">
  <div class="wrap">
    <div class="eye">Parlons-en</div>
    <h2 class="h2">Une démo de vingt minutes, sur un jeu de données proche du vôtre</h2>
    <p class="lead">Dites-nous ce que vous vendez et comment vos agents travaillent aujourd'hui : on vous montre l'application, et on répond aux questions concrètes — reprise de l'existant, nombre de postes, marques à connecter.</p>
    <div class="btns">
      <a class="btn btn-primary" href="/#demo">Demander une démo {FLECHE}</a>
      <a class="btn btn-ghost" href="/">Découvrir CelField</a>
    </div>
  </div>
</section>
</main>

{pied()}

</body>
</html>
'''


def remplacer_bloc(s, nom, nouveau):
    motif = re.compile(r'<!-- ' + nom + r':DEBUT.*?<!-- ' + nom + r':FIN -->', re.S)
    if not motif.search(s):
        raise SystemExit(f'balises {nom}:DEBUT / {nom}:FIN introuvables dans index.html')
    return motif.sub(lambda m: nouveau, s, count=1)


P = {p['slug']: p for p in PAGES}


def main():
    for p in PAGES:
        for s in p['voir_aussi']:
            assert s in P and s != p['slug'], (p['slug'], s)
        assert p['image'] in IMAGES, p['image']
        assert len(p['description']) <= 165, (p['slug'], len(p['description']))
        dossier = os.path.join(RACINE, p['slug'])
        os.makedirs(dossier, exist_ok=True)
        with open(os.path.join(dossier, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(page_html(p))
        print('écrit', p['slug'])

    idx = os.path.join(RACINE, 'index.html')
    s = open(idx, encoding='utf-8').read()
    s = remplacer_bloc(s, 'PIED', pied())
    s = remplacer_bloc(s, 'SOLUTIONS', grille_solutions())
    s = re.sub(r'/assets/site\.css\?v=\d+', f'/assets/site.css?v={CSS_V}', s)
    open(idx, 'w', encoding='utf-8').write(s)
    print('accueil mis à jour')

    urls = [(SITE + '/', '1.0')] + [(url_page(p), '0.8') for p in PAGES]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, prio in urls:
        sm.append(f'  <url><loc>{u}</loc><lastmod>{AUJOURDHUI}</lastmod><priority>{prio}</priority></url>')
    sm.append('</urlset>')
    open(os.path.join(RACINE, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(sm) + '\n')
    print('sitemap :', len(urls), 'adresses')


if __name__ == '__main__':
    main()
