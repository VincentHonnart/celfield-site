"""Contenu des pages thématiques de celfield.com — lu par generer_pages.py.

Règle : n'écrire que ce que l'application fait réellement (vérifié dans le dépôt
celfield-crm au 15/09/2026). Aucun témoignage, aucun chiffre client inventé.
Les tarifs reprennent ceux de la page d'accueil.

Champs :
  slug        adresse (/slug/)
  court       libellé court (liens, fil d'Ariane, pied)
  accroche    une phrase pour les cartes de liens
  titre       <title> — la requête visée d'abord, la marque ensuite
  description meta description, 165 caractères maximum
  etiquette   petit bandeau au-dessus du H1
  h1, chapo   titre et chapeau (HTML autorisé)
  image       capture affichée sous le chapeau
  corps       HTML de l'article (h2, h3, p, ul)
  atouts      liste « En bref »
  faq         [(question, réponse HTML)]
  voir_aussi  quatre slugs
"""

PAGES = [

# ─────────────────────────────────────────────────────────────────────────────
dict(
slug='logiciel-prise-de-commande-pharmacie',
court='Prise de commande en pharmacie',
accroche="Saisir la commande chez le pharmacien, l'envoyer avant de reprendre la route, savoir qu'elle est arrivée.",
titre='Logiciel de prise de commande en pharmacie pour agents commerciaux | CelField',
description="Logiciel de prise de commande pour agents commerciaux en pharmacie : catalogue à jour, remises et UG, bon PDF envoyé par email, suivi de remise, mode hors ligne.",
etiquette='Prise de commande · Officine',
h1="Le logiciel de prise de commande des agents qui vendent <em>en pharmacie</em>",
chapo="CelField remplace le carnet, le catalogue imprimé et la ressaisie du soir. La commande se prend chez le pharmacien, sur votre ordinateur portable ou votre tablette, avec les conditions du client déjà appliquées. Le bon part par email avant que vous ayez quitté l'officine — et vous savez s'il est bien arrivé.",
image='capture-prise-de-commande.webp',
legende='Prise de commande · catalogue, quantités et totaux (données de démonstration)',
corps='''
<h2>Une commande prise au comptoir, envoyée avant de reprendre la route</h2>
<p>Dans la plupart des réseaux, la commande prise en officine vit trois vies : notée sur papier ou en photo, ressaisie le soir dans un tableur, puis envoyée à la marque ou au dépositaire. Chaque étape coûte du temps, et chaque ressaisie ouvre la porte à une erreur de référence ou de quantité. <strong>CelField réduit la chaîne à une seule saisie</strong>, faite devant le client.</p>

<h3>Trouver le produit comme on le cherche en officine</h3>
<p>Le catalogue se parcourt par marque et par gamme, ou se filtre au nom ou au <strong>code EAN</strong>. Les nouveautés sont signalées, les produits en rupture aussi, avec leur date de retour quand la marque l'a indiquée : vous ne proposez pas ce qui ne pourra pas être livré.</p>

<h3>Les conditions du client, appliquées d'office</h3>
<p>Remises, <strong>unités gratuites (UG)</strong>, colisage : la commande reprend les remises issues des conditions générales de la marque et celles négociées avec la pharmacie. Le respect du PCB (colisage) s'active d'un geste et arrondit les quantités au multiple attendu ; on le désactive pour une opération du type 5+1. Le total HT se calcule au fur et à mesure, et le seuil de franco est signalé.</p>

<h3>Le bon de commande part au bon destinataire</h3>
<p>À la validation, CelField produit un <strong>bon de commande PDF</strong> à votre en-tête et l'envoie par email à la marque, au dépositaire ou à la pharmacie, sans quitter l'application. Une copie reste attachée à la fiche du client.</p>

<h3>Remis, pas seulement envoyé</h3>
<p>Un email envoyé n'est pas un email reçu. CelField suit la <strong>remise réelle</strong> de chaque bon auprès du serveur destinataire : remis, ou rejeté — et pourquoi. Une adresse erronée se voit dans la liste des commandes le jour même, pas trois semaines plus tard quand la pharmacie réclame sa livraison.</p>

<h2>Une commande qui connaît la pharmacie</h2>
<p>La commande s'ouvre depuis la fiche du client, où figurent son <strong>historique d'achats</strong>, son groupement et vos notes de visite. Dans l'écran de commande, un onglet signale les <a href="/catalogue-marques-laboratoires/">opérations commerciales</a> en cours ou à venir pour ce client et cette marque : vous ne découvrez pas une opération sell-in la semaine où elle se termine.</p>

<h2>Les marchés : une saisie, plusieurs livraisons</h2>
<p>Quand une pharmacie s'engage sur l'année, la commande se saisit une seule fois puis se <strong>répartit sur plusieurs dates de livraison</strong>. CelField vérifie que la répartition boucle — quantités et UG comprises — et génère une commande complète par échéance, chacune avec son bon, son envoi et son suivi. Le chiffre d'affaires de chaque livraison tombe dans le mois où elle est livrée.</p>

<h2>Pour qui ?</h2>
<ul>
<li><strong>Agents commerciaux multicartes</strong> qui représentent plusieurs marques auprès des officines — voir <a href="/crm-agent-commercial-multicarte/">le CRM de l'agent multicarte</a>.</li>
<li><strong>Équipes de vente des marques et des laboratoires</strong>, et les délégués qui prennent des commandes en pharmacie.</li>
<li><strong>Structures commerciales</strong> qui veulent une vue consolidée de leurs agents sans multiplier les tableurs.</li>
</ul>

<h2>Et quand le réseau manque ?</h2>
<p>L'arrière-boutique sans couverture n'arrête pas la commande : CelField garde une copie locale de vos données et <a href="/prise-de-commande-hors-ligne/">fonctionne hors ligne</a>. La commande est enregistrée sur l'appareil et part dès que la connexion revient. Et si la pharmacienne vous tend son propre bon de commande, <a href="/lecture-ia-bon-de-commande/">l'IA le lit pour vous</a>.</p>
''',
atouts=[
 'Recherche par nom, gamme ou code EAN',
 'Remises, UG et colisage (PCB) appliqués automatiquement',
 'Bon PDF envoyé par email à votre en-tête',
 'Suivi de remise : remis ou rejeté',
 'Marchés répartis sur plusieurs livraisons',
 'Fonctionne sans réseau',
],
faq_titre='La prise de commande en pharmacie avec CelField',
faq=[
 ("Faut-il installer un logiciel sur l'ordinateur ou la tablette ?",
  "Non. CelField s'ouvre dans le navigateur, sur un ordinateur portable ou une tablette. Il peut aussi être installé comme une application depuis le navigateur, sans passer par un magasin d'applications."),
 ("À qui le bon de commande est-il envoyé ?",
  "À l'adresse que vous choisissez : la marque, son dépositaire ou la pharmacie. Le bon part en PDF, à l'en-tête de votre structure, et une copie reste attachée à la fiche du client."),
 ("Comment savoir si le bon a bien été reçu ?",
  "CelField suit la remise de chaque email auprès du serveur destinataire. La liste des commandes indique si le bon a été remis ou rejeté, avec la raison du rejet."),
 ("Peut-on reprendre notre historique de commandes ?",
  "Oui. À la mise en route, vos pharmacies, vos groupements, votre catalogue et votre historique de commandes sont importés : chaque fiche client affiche son passé dès le premier jour."),
 ("Combien coûte CelField ?",
  "40 € HT par mois pour le premier poste, 15 € HT par mois par poste complémentaire, sans frais de mise en service. La lecture IA des bons de commande est une option, poste par poste. Le détail est sur <a href=\"/#tarifs\">la page des tarifs</a>."),
],
voir_aussi=['prise-de-commande-hors-ligne', 'lecture-ia-bon-de-commande', 'crm-agent-commercial-multicarte', 'catalogue-marques-laboratoires'],
),

# ─────────────────────────────────────────────────────────────────────────────
dict(
slug='prise-de-commande-hors-ligne',
court='Prise de commande hors ligne',
accroche="Consulter ses clients et saisir des commandes sans réseau, tout remonte au retour de la connexion.",
titre='Application de prise de commande hors ligne pour commerciaux terrain | CelField',
description="Prenez vos commandes sans réseau : fiches clients, catalogue et saisie disponibles hors ligne, envoi automatique au retour de la connexion, sans doublon.",
etiquette='Mode hors ligne · Zones blanches',
h1="Prendre les commandes <em>sans réseau</em>, en officine comme dans le train",
chapo="Arrière-boutique sans couverture, zone rurale, trajet en train : c'est souvent là que la commande se joue. CelField garde une copie locale de vos pharmacies et de votre catalogue, vous laisse saisir normalement, et envoie tout dès que la connexion revient.",
image='capture-fiche-pharmacie.webp',
legende='Fiche pharmacie · consultable avec ou sans connexion (données de démonstration)',
corps='''
<h2>Le réseau manque précisément là où se prennent les commandes</h2>
<p>Une officine de centre-bourg, une réserve en sous-sol, une route de campagne : les commerciaux terrain le savent, la couverture mobile n'est jamais garantie au moment où le client est prêt à commander. Une application qui exige une connexion transforme ces moments en <strong>« je vous l'envoie ce soir »</strong> — et en ressaisie.</p>
<p>CelField a été conçu pour que la perte de réseau ne change rien à la visite.</p>

<h2>Ce qui reste disponible sans connexion</h2>
<ul>
<li><strong>Vos pharmacies</strong> : coordonnées, groupement, notes, historique des commandes.</li>
<li><strong>Le catalogue</strong> : références, EAN, prix, conditions, nouveautés et ruptures.</li>
<li><strong>La saisie de commande</strong>, remises et UG comprises — y compris les <a href="/logiciel-prise-de-commande-pharmacie/">marchés répartis sur plusieurs livraisons</a>.</li>
<li><strong>Vos commandes en attente</strong>, listées avec leur libellé pour que vous reconnaissiez chacune.</li>
</ul>

<h2>Au retour du réseau : tout part, dans l'ordre, sans doublon</h2>
<p>Les commandes saisies hors ligne sont placées dans une <strong>file d'attente</strong> sur l'appareil. Dès que la connexion revient, elles sont transmises au serveur une par une. Le numéro de commande est attribué à ce moment-là, par le serveur : aucun numéro n'est fabriqué sur l'appareil, ce qui évite qu'un même numéro soit donné deux fois lorsque plusieurs agents travaillent en parallèle.</p>
<p>Un indicateur de connexion vous dit à tout moment si vous travaillez en ligne ou sur la copie locale.</p>

<h2>« Rester hors ligne » : pour les connexions qui vont et viennent</h2>
<p>Le pire réseau n'est pas l'absence de réseau, c'est celui qui coupe toutes les trente secondes. Un <strong>interrupteur</strong> permet de forcer le mode hors ligne le temps d'un trajet ou d'une visite : l'application cesse d'essayer de joindre le serveur et travaille sereinement sur la copie locale. Vous le relevez en arrivant.</p>

<h2>Verrouiller l'écran sans se déconnecter</h2>
<p>Se déconnecter sans réseau, c'est s'enfermer dehors : le mot de passe ne peut pas être vérifié tant que la connexion n'est pas revenue. Hors ligne, CelField propose donc de <strong>verrouiller la session</strong> : l'écran se couvre, les données restent protégées, et vous rouvrez avec un code, sans réseau.</p>

<h2>Rien à installer, rien à synchroniser à la main</h2>
<p>CelField fonctionne dans le navigateur de votre ordinateur portable ou de votre tablette, et peut être installé comme une application. La copie locale se tient à jour d'elle-même quand vous êtes connecté : il n'y a pas de bouton « synchroniser » à ne pas oublier avant de partir en tournée.</p>
''',
atouts=[
 'Fiches clients et historique consultables hors ligne',
 'Catalogue et prix disponibles sans réseau',
 'Commandes en file d’attente, envoyées au retour de la connexion',
 'Numéros attribués par le serveur : aucun doublon',
 'Interrupteur « Rester hors ligne »',
 'Verrouillage de session sans réseau',
],
faq_titre='Le mode hors ligne, en pratique',
faq=[
 ("Que se passe-t-il si je ferme l'application avant le retour du réseau ?",
  "Les commandes restent enregistrées sur l'appareil. Elles partent à la prochaine ouverture de CelField avec une connexion disponible."),
 ("Deux agents peuvent-ils se retrouver avec le même numéro de commande ?",
  "Non. Les numéros sont attribués par le serveur au moment où la commande y arrive, jamais sur l'appareil. Une commande saisie hors ligne reçoit son numéro à la reconnexion."),
 ("Les prix sont-ils à jour quand je travaille hors ligne ?",
  "Ce sont ceux de la dernière mise à jour reçue en ligne. La copie locale se rafraîchit d'elle-même dès que vous êtes connecté, sans action de votre part."),
 ("Mes données sont-elles protégées sur l'appareil ?",
  "La session peut être verrouillée par un code sans réseau. Et chaque agent ne voit que les pharmacies et le chiffre qui le concernent : les droits sont posés au niveau de la base de données."),
],
voir_aussi=['logiciel-prise-de-commande-pharmacie', 'lecture-ia-bon-de-commande', 'crm-agent-commercial-multicarte', 'parapharmacie'],
),

# ─────────────────────────────────────────────────────────────────────────────
dict(
slug='lecture-ia-bon-de-commande',
court='Lecture IA des bons de commande',
accroche="Déposez le bon de la pharmacie, en PDF ou en photo : l'IA remplit la commande, vous validez.",
titre='Lecture IA des bons de commande PDF et photos | CelField',
description="Déposez le bon de commande de la pharmacie en PDF ou en photo : l'IA extrait EAN, libellés et quantités et prépare la commande. Vous relisez et validez.",
etiquette='Intelligence artificielle · Saisie',
h1="Le bon de commande de la pharmacie, <em>saisi par l'IA</em> en quelques secondes",
chapo="La pharmacienne vous tend son bon de commande, ou vous l'envoie en PDF. Plutôt que de le recopier ligne à ligne, vous le déposez dans CelField : l'IA lit le document, reconnaît chaque produit et remplit la commande. Vous relisez, vous corrigez si besoin, vous validez.",
image='capture-lecture-ia.webp',
legende='Lecture IA · dépôt du bon de commande (données de démonstration)',
corps='''
<h2>La ressaisie, étape la plus longue et la plus risquée</h2>
<p>Beaucoup de pharmacies préparent leur commande elles-mêmes : un export de leur logiciel d'officine, un bon imprimé, une liste manuscrite. Recopier trente lignes de codes EAN à treize chiffres est long, et une seule erreur de chiffre change le produit livré. <strong>C'est cette étape que la lecture IA supprime.</strong></p>

<h2>Ce que l'IA lit</h2>
<ul>
<li><strong>Le code EAN</strong> de chaque ligne, débarrassé des espaces ;</li>
<li><strong>la désignation</strong> du produit telle qu'elle figure sur le document ;</li>
<li><strong>la quantité commandée</strong>, quel que soit l'intitulé de la colonne ;</li>
<li><strong>la date de livraison</strong> souhaitée et le <strong>numéro de commande</strong> de la pharmacie, quand ils sont présents.</li>
</ul>
<p>En-têtes, totaux, adresses et mentions légales sont ignorés : seules les lignes de produits sont retenues.</p>

<h2>PDF, bon imprimé ou photo</h2>
<p>Le document peut être un <strong>PDF</strong> de plusieurs pages, ou une <strong>photo</strong> du bon papier (JPEG, PNG ou WebP), jusqu'à 8 Mo. Les colonnes désalignées d'un export d'officine ne gênent pas la lecture : l'IA s'appuie à la fois sur le texte et sur la mise en page.</p>

<h2>Elle n'invente rien, et vous gardez la main</h2>
<p>Le modèle est cadré pour <strong>n'extraire que ce qui figure sur le document</strong>. Une ligne sans code EAN reste sans code EAN : la donnée absente n'est jamais devinée. La commande proposée s'affiche ensuite dans l'écran de saisie habituel, rapprochée de votre <a href="/catalogue-marques-laboratoires/">catalogue</a> : chaque ligne reste modifiable, et rien n'est enregistré ni envoyé sans votre validation.</p>

<h2>Une option, poste par poste</h2>
<p>La lecture IA s'ajoute aux postes qui en ont l'usage : <strong>10 € HT par mois</strong> sur le premier poste, <strong>5 € HT par mois</strong> par poste complémentaire. Sans elle, le reste de CelField fonctionne à l'identique — <a href="/logiciel-prise-de-commande-pharmacie/">la prise de commande</a>, le suivi des clients, le mode hors ligne. L'option se désactive sans rien toucher d'autre.</p>

<h2>Ce qui est transmis</h2>
<p>Seul le document que vous déposez est transmis au modèle d'intelligence artificielle, le temps de sa lecture. La commande qui en résulte est enregistrée dans la base de votre structure, comme toute autre commande.</p>
''',
atouts=[
 'PDF multipage ou photo du bon papier',
 'EAN, désignation, quantité, date de livraison',
 'Aucune donnée inventée : un champ absent reste vide',
 'Commande proposée, modifiable avant validation',
 'Option à 10 € puis 5 € HT par poste',
],
faq_titre='La lecture IA des bons de commande',
faq=[
 ("Quels formats de fichier sont acceptés ?",
  "Les PDF, et les photos au format JPEG, PNG, GIF ou WebP, jusqu'à 8 Mo. Le format HEIC, utilisé par défaut par certains iPhone, n'est pas accepté : il suffit de partager la photo en JPEG."),
 ("L'IA peut-elle se tromper ?",
  "Comme toute lecture automatique, elle peut mal lire une ligne peu lisible. C'est pourquoi la commande proposée n'est jamais enregistrée directement : vous la relisez et la corrigez dans l'écran de saisie avant de la valider."),
 ("Que se passe-t-il si un code EAN manque sur le bon ?",
  "La ligne est reprise avec sa désignation et sa quantité, sans code : l'IA ne complète jamais une donnée absente. Vous choisissez le produit dans le catalogue."),
 ("Peut-on activer l'IA pour un seul agent ?",
  "Oui. L'option se prend poste par poste : vous ne la payez que pour les agents qui s'en servent."),
],
voir_aussi=['logiciel-prise-de-commande-pharmacie', 'prise-de-commande-hors-ligne', 'catalogue-marques-laboratoires', 'complements-alimentaires'],
),

# ─────────────────────────────────────────────────────────────────────────────
dict(
slug='crm-agent-commercial-multicarte',
court='CRM pour agent multicarte',
accroche="Toutes vos marques, un seul portefeuille : clients, commandes, chiffre et commissions par marque.",
titre='CRM pour agent commercial multicarte en pharmacie et parapharmacie | CelField',
description="Le CRM de l'agent commercial multicarte : un portefeuille de pharmacies pour toutes vos marques, commandes par marque, CA et commissions suivis en temps réel.",
etiquette='CRM · Agents multicartes',
h1="Le CRM de l'agent multicarte : <em>toutes vos marques</em>, un seul portefeuille",
chapo="Un agent multicarte visite les mêmes pharmacies pour le compte de plusieurs marques. CelField réunit ces marques dans un seul outil : un portefeuille de clients, un catalogue par marque, un bon de commande par marque, et un chiffre d'affaires que l'on suit marque par marque.",
image='capture-tableau-de-bord.webp',
legende="Tableau de bord · chiffre d'affaires et commandes (données de démonstration)",
corps='''
<h2>Un CRM généraliste ne connaît ni les officines ni les marques</h2>
<p>Les CRM du marché savent gérer des « comptes » et des « opportunités ». L'agent qui vend en pharmacie a besoin d'autre chose : des <strong>officines rattachées à leur groupement</strong>, un <strong>catalogue par marque</strong> avec ses conditions, des commandes qui partent chez le bon fournisseur, et un chiffre qui se lit marque par marque. CelField est construit autour de ce métier.</p>

<h2>Un portefeuille, plusieurs marques</h2>
<p>Chaque pharmacie a une seule fiche, quelle que soit la marque pour laquelle vous la visitez. Elle rassemble ses coordonnées, son <strong>groupement</strong>, vos <strong>notes de visite</strong> et l'historique de ses commandes, toutes marques confondues ou filtré sur l'une d'elles.</p>
<ul>
<li>Filtrer le portefeuille par secteur, par groupement ou par marque ;</li>
<li>repérer les pharmacies qui n'ont rien commandé depuis trop longtemps — le seuil se règle ;</li>
<li>savoir, avant d'entrer, ce que le client a pris la dernière fois et chez quelle marque.</li>
</ul>

<h2>Une commande, un fournisseur</h2>
<p>La <a href="/logiciel-prise-de-commande-pharmacie/">prise de commande</a> se fait marque par marque, avec le catalogue, les remises, les packs et les opérations propres à chacune. Le bon part à l'adresse de la marque ou de son dépositaire. Vous ne mélangez pas deux fournisseurs sur un même bon.</p>

<h2>Le chiffre et les commissions, par marque</h2>
<p>Votre <strong>chiffre d'affaires du mois et de l'année</strong> se met à jour à chaque commande enregistrée, et se ventile par marque. Le rapport mensuel liste les commandes d'un mois avec leur CA et leurs <strong>commissions</strong>, filtrables par marque et par secteur. L'accès aux commissions est un droit : un profil qui ne doit pas les voir ne les reçoit pas, même dans un export.</p>

<h2>Seul ou en équipe</h2>
<p>CelField convient à l'agent indépendant comme à l'agence qui emploie plusieurs commerciaux. Chaque agent voit <strong>ses pharmacies et son chiffre</strong> ; un responsable voit son équipe. Les secteurs sont attribués par code : une pharmacie rejoint automatiquement le portefeuille de l'agent qui porte son secteur.</p>

<h2>Démarrer avec son passé</h2>
<p>Un changement d'outil ne doit pas effacer des années de relation client. À la mise en route, vos pharmacies, vos groupements, vos catalogues et votre <strong>historique de commandes</strong> sont importés. Les fiches affichent leur passé dès le premier jour, et le chiffre des mois précédents figure dans les rapports.</p>
''',
atouts=[
 'Une fiche par pharmacie, toutes marques confondues',
 'Catalogue, remises et opérations propres à chaque marque',
 'CA du mois et de l’année, par marque',
 'Rapport mensuel avec commissions',
 'Portefeuille par secteur, vue équipe pour le responsable',
 'Reprise de l’historique de commandes',
],
faq_titre="Le CRM de l'agent commercial multicarte",
faq=[
 ("Combien de marques peut-on gérer ?",
  "Il n'y a pas de limite fixée au nombre de marques : chacune a son catalogue, ses conditions et son adresse d'envoi des bons."),
 ("Le CRM convient-il à un agent indépendant seul ?",
  "Oui. Le premier poste comprend l'instance de votre structure et votre compte. Vous ajoutez des postes le jour où vous recrutez."),
 ("Les commissions sont-elles visibles par tous les utilisateurs ?",
  "Non. L'accès aux commissions est un droit attribué par profil. Un utilisateur sans ce droit ne les voit ni à l'écran, ni dans les rapports, ni dans les exports."),
 ("Nos données sont-elles partagées avec d'autres agences ?",
  "Non. Chaque structure dispose de sa propre base de données, isolée, hébergée dans l'Union européenne, et de sa propre adresse."),
],
voir_aussi=['logiciel-prise-de-commande-pharmacie', 'catalogue-marques-laboratoires', 'prise-de-commande-hors-ligne', 'cosmetique-beaute'],
),

# ─────────────────────────────────────────────────────────────────────────────
dict(
slug='catalogue-marques-laboratoires',
court='Catalogue alimenté par les marques',
accroche="Tarifs, ruptures, nouveautés et opérations publiés par les marques, sans ressaisie.",
titre='Catalogue produits alimenté par les marques et laboratoires | CelField',
description="Un catalogue tenu à jour par les marques : tarifs, EAN, ruptures avec date de retour, nouveautés, packs et opérations sell-in et sell-out, sans ressaisie.",
etiquette='Connectique marques · Catalogue',
h1="Un catalogue tenu à jour <em>par les marques</em>, pas par vos agents",
chapo="Le tarif qui a changé, la référence en rupture, le lancement du mois, l'opération sell-in de la rentrée : dans CelField, ces informations descendent des marques jusqu'à l'écran de l'agent. Personne ne retape un tarif, personne ne travaille sur une version périmée.",
image='capture-trade.webp',
legende='Opérations commerciales · calendrier sell-in et sell-out (données de démonstration)',
corps='''
<h2>Le catalogue périmé coûte cher</h2>
<p>Un catalogue imprimé ou un fichier envoyé par email est faux dès le premier changement de prix. L'agent propose un produit en rupture, applique une remise qui n'existe plus, ou découvre une opération trop tard. <strong>CelField relie le catalogue à sa source</strong> : la marque.</p>

<h2>Ce que la marque publie</h2>
<h3>Références et tarifs</h3>
<p>Références, <strong>codes EAN</strong>, prix, gammes et <strong>colisage (PCB)</strong>. Le prix affiché à l'écran est celui de la marque, identique pour toute l'équipe.</p>
<h3>Ruptures, avec leur date de retour</h3>
<p>Un produit indisponible est signalé dans le catalogue, avec la <strong>date de retour</strong> prévue quand elle est connue. L'agent ne le propose pas, ou prévient la pharmacie du délai.</p>
<h3>Nouveautés</h3>
<p>Les lancements sont mis en avant dans le catalogue le jour où la marque les ouvre.</p>
<h3>Packs et conditions générales de vente</h3>
<p>Les <strong>packs</strong> — lots de produits vendus ensemble à prix fixé — se commandent en une ligne. Les <strong>conditions générales de vente</strong> de chaque marque sont consultables sur sa fiche, et leurs remises s'appliquent aux commandes.</p>

<h2>Les opérations commerciales, au bon moment</h2>
<p>Les opérations <strong>sell-in</strong> et <strong>sell-out</strong> des marques s'affichent dans un calendrier, avec leur période, leurs conditions — remise, gratuité, objectif — et leur <strong>cible</strong> : toutes les pharmacies, un ou plusieurs groupements, ou une liste d'officines. Elles sont signalées dans l'écran de commande des pharmacies concernées : l'agent les a sous les yeux pendant la visite.</p>

<h2>Au-dessus du tarif, les accords du client</h2>
<p>Les conditions particulières négociées avec une pharmacie ou avec son groupement s'ajoutent au tarif de la marque et s'appliquent à la <a href="/logiciel-prise-de-commande-pharmacie/">prise de commande</a>. Le référentiel des <strong>groupements de pharmacies</strong> est commun, ce qui permet de cibler une opération sur un groupement sans maintenir sa propre liste.</p>

<h2>Pour les marques : un réseau à jour le jour même</h2>
<p>Pour une marque ou un laboratoire, c'est l'assurance que les agents qui la représentent travaillent sur les mêmes informations, au même moment. Une rupture déclarée le matin est visible dans les tournées de l'après-midi. Voir aussi CelField pour <a href="/parapharmacie/">la parapharmacie</a>, <a href="/cosmetique-beaute/">la cosmétique</a> et <a href="/complements-alimentaires/">les compléments alimentaires</a>.</p>
''',
atouts=[
 'Tarifs, EAN et colisage à la source',
 'Ruptures avec date de retour',
 'Nouveautés mises en avant',
 'Packs et CGV par marque',
 'Opérations sell-in et sell-out ciblées',
 'Référentiel commun des groupements',
],
faq_titre='Le catalogue alimenté par les marques',
faq=[
 ("Les agents peuvent-ils modifier le catalogue ?",
  "Le catalogue suit la marque. Les conditions particulières d'un client s'ajoutent au-dessus du tarif, sans modifier le catalogue commun."),
 ("Comment une opération commerciale est-elle ciblée ?",
  "Une opération s'adresse à toutes les pharmacies, à un ou plusieurs groupements, ou à une liste précise d'officines. Pendant sa période, elle est signalée dans l'écran de commande des pharmacies concernées."),
 ("Que se passe-t-il quand un produit est en rupture ?",
  "Il est signalé dans le catalogue, avec sa date de retour si la marque l'a indiquée. L'agent le voit avant de le proposer."),
 ("Une marque qui n'est pas encore connectée peut-elle être utilisée ?",
  "Oui. Son catalogue est importé à la mise en route et tenu à jour depuis l'application, en attendant qu'elle publie elle-même ses informations."),
],
voir_aussi=['crm-agent-commercial-multicarte', 'logiciel-prise-de-commande-pharmacie', 'parapharmacie', 'cosmetique-beaute'],
),

# ─────────────────────────────────────────────────────────────────────────────
dict(
slug='parapharmacie',
court='Parapharmacie',
accroche="Dermo-cosmétique, hygiène, solaires : un outil pour les gammes larges et les saisons courtes.",
titre='CRM et prise de commande pour commerciaux en parapharmacie | CelField',
description="CelField pour la parapharmacie : catalogues larges à jour, précommandes de saison, opérations par groupement, commande hors ligne et suivi du CA par marque.",
etiquette='Secteur · Parapharmacie',
h1="CelField pour les marques et agents de <em>parapharmacie</em>",
chapo="Des gammes larges, des références qui changent chaque saison, des opérations négociées avec les groupements : la parapharmacie en officine demande un outil qui suive le rythme des marques. CelField réunit le portefeuille, le catalogue et la commande au même endroit.",
image='capture-prise-de-commande.webp',
legende='Prise de commande · catalogue par gamme (données de démonstration)',
corps='''
<h2>Des catalogues larges, qui bougent</h2>
<p>Dermo-cosmétique, hygiène, soins bébé, solaires : un catalogue de parapharmacie compte vite plusieurs centaines de références, avec des lancements et des arrêts à chaque saison. Dans CelField, le <a href="/catalogue-marques-laboratoires/">catalogue est tenu à jour à la source</a> : nouveautés mises en avant, ruptures signalées avec leur date de retour, recherche par gamme ou par code EAN.</p>

<h2>Les précommandes de saison</h2>
<p>Les gammes saisonnières se vendent souvent des mois avant leur livraison. Une commande peut être marquée comme <strong>précommande</strong> et porter sa date de livraison ; son chiffre d'affaires est classé dans le mois où elle est livrée. Les engagements étalés sur l'année se saisissent en une fois et se <strong>répartissent sur plusieurs livraisons</strong>.</p>

<h2>Les groupements au cœur de la négociation</h2>
<p>En parapharmacie, beaucoup de conditions se négocient avec les groupements. Chaque pharmacie est rattachée à son groupement ; les opérations sell-in et sell-out peuvent cibler un ou plusieurs groupements, et sont signalées au moment de commander pour les officines concernées.</p>

<h2>Sur la route</h2>
<p>La commande se prend en officine, sur ordinateur portable ou tablette, <a href="/prise-de-commande-hors-ligne/">même sans réseau</a>. Le bon part par email à la marque ou au dépositaire, et son arrivée est suivie. Si la pharmacie a préparé sa propre liste, <a href="/lecture-ia-bon-de-commande/">l'IA la lit</a> et remplit la commande.</p>

<h2>Le chiffre par marque</h2>
<p>Pour l'agent multicarte comme pour l'équipe d'une marque, le <strong>CA du mois et de l'année</strong> se suit en temps réel, marque par marque, avec la liste des pharmacies qui n'ont pas commandé depuis longtemps.</p>
''',
atouts=[
 'Catalogues larges, nouveautés et ruptures à jour',
 'Précommandes datées',
 'Marchés répartis sur plusieurs livraisons',
 'Opérations ciblées par groupement',
 'Commande hors ligne en officine',
],
faq_titre='CelField en parapharmacie',
faq=[
 ("CelField gère-t-il les précommandes ?",
  "Oui. Une commande peut être marquée comme précommande et porter sa date de livraison ; son chiffre d'affaires est classé dans le mois de livraison."),
 ("Peut-on cibler une opération sur un groupement ?",
  "Oui. Une opération s'adresse à toutes les pharmacies, à un ou plusieurs groupements, ou à une liste d'officines."),
 ("CelField convient-il aussi aux parapharmacies hors officine ?",
  "CelField est conçu autour des officines et de leurs groupements. Pour un autre réseau de points de vente, parlons-en lors de la démo."),
],
voir_aussi=['logiciel-prise-de-commande-pharmacie', 'catalogue-marques-laboratoires', 'cosmetique-beaute', 'complements-alimentaires'],
),

# ─────────────────────────────────────────────────────────────────────────────
dict(
slug='cosmetique-beaute',
court='Cosmétique et beauté',
accroche="Lancements fréquents, coffrets et packs, opérations en magasin : la beauté en officine, suivie de près.",
titre='CRM et prise de commande pour commerciaux en cosmétique et beauté | CelField',
description="CelField pour les marques de cosmétique et de beauté vendues en officine : lancements, packs et coffrets, opérations sell-out, commande sur tablette et suivi du CA.",
etiquette='Secteur · Cosmétique & beauté',
h1="CelField pour la <em>cosmétique et la beauté</em> en officine",
chapo="Lancements réguliers, coffrets, mise en avant en magasin : les marques de beauté vivent au rythme des nouveautés et des opérations. CelField donne aux agents un catalogue à jour, des packs prêts à vendre et un calendrier des opérations, dans l'outil où ils prennent la commande.",
image='capture-trade.webp',
legende='Opérations commerciales · calendrier des marques (données de démonstration)',
corps='''
<h2>Le rythme des lancements</h2>
<p>Une marque de beauté peut lancer plusieurs références par trimestre. Dans CelField, les <strong>nouveautés sont mises en avant</strong> dans le catalogue dès leur ouverture, et les références arrêtées ou en rupture sont signalées. L'agent présente la bonne collection, au bon moment.</p>

<h2>Packs et coffrets</h2>
<p>Les <strong>packs</strong> — lots de produits vendus ensemble à prix fixé — se commandent comme une ligne unique, avec leur contenu consultable. Ils conviennent aux coffrets, aux implantations et aux offres de lancement.</p>

<h2>Les opérations sell-out</h2>
<p>Les animations en officine, les offres consommateur et les opérations de mise en avant s'affichent dans le <a href="/catalogue-marques-laboratoires/">calendrier des opérations</a>, avec leur période, leurs conditions et les pharmacies ciblées. L'agent les rappelle pendant la visite, et les unités gratuites se saisissent dans la commande.</p>

<h2>Une présentation soignée</h2>
<p>La commande se prend sur <strong>tablette ou ordinateur portable</strong>, devant la pharmacienne, dans une interface lisible. Le bon de commande part en PDF à l'en-tête de votre structure, et l'historique de la pharmacie aide à proposer ce qui manque en rayon.</p>

<h2>Le suivi</h2>
<p>Le chiffre d'affaires se suit par marque et par mois ; les pharmacies inactives sont repérées. Pour un agent qui représente plusieurs marques de beauté, voir <a href="/crm-agent-commercial-multicarte/">le CRM de l'agent multicarte</a>.</p>
''',
atouts=[
 'Nouveautés mises en avant dès leur ouverture',
 'Packs et coffrets commandés en une ligne',
 'Calendrier des opérations sell-out',
 'UG saisies dans la commande',
 'Bon de commande PDF à votre en-tête',
],
faq_titre='CelField en cosmétique et beauté',
faq=[
 ("Comment sont gérés les coffrets ?",
  "Comme des packs : un lot de produits à prix fixé, commandé en une ligne, dont le contenu reste consultable."),
 ("Peut-on suivre une opération de mise en avant ?",
  "Chaque opération a sa période, ses conditions et sa cible. Pendant toute sa durée, elle est signalée dans l'écran de commande des pharmacies concernées."),
 ("L'application fonctionne-t-elle sur tablette ?",
  "Oui, dans le navigateur de la tablette, avec ou sans réseau. Elle peut aussi être installée comme une application."),
],
voir_aussi=['catalogue-marques-laboratoires', 'crm-agent-commercial-multicarte', 'parapharmacie', 'lecture-ia-bon-de-commande'],
),

# ─────────────────────────────────────────────────────────────────────────────
dict(
slug='complements-alimentaires',
court='Compléments alimentaires',
accroche="Cures saisonnières, marchés annuels, gratuités : un outil pour les ventes qui se planifient.",
titre='CRM et prise de commande pour commerciaux en compléments alimentaires | CelField',
description="CelField pour les compléments alimentaires et le bien-être en pharmacie : marchés sur plusieurs livraisons, UG, opérations saisonnières et suivi du CA par mois.",
etiquette='Secteur · Compléments & bien-être',
h1="CelField pour les <em>compléments alimentaires</em> et le bien-être",
chapo="Cures d'hiver, préparation de l'été, engagements annuels : les ventes de compléments alimentaires en officine se planifient. CelField permet de saisir un marché en une fois, de le répartir sur l'année, et de suivre le chiffre mois par mois.",
image='capture-tableau-de-bord.webp',
legende="Tableau de bord · CA du mois et de l'année (données de démonstration)",
corps='''
<h2>Des ventes qui se planifient</h2>
<p>Immunité à l'automne, minceur et solaire au printemps : les compléments alimentaires suivent les saisons, et les pharmacies s'engagent souvent à l'avance. CelField permet de <strong>saisir un marché en une seule fois</strong> et de le répartir sur plusieurs dates de livraison. Chaque livraison devient une commande à part entière, avec son bon et son suivi.</p>

<h2>Unités gratuites et paliers</h2>
<p>Les <strong>unités gratuites</strong> se saisissent ligne par ligne, et se répartissent elles aussi sur les livraisons d'un marché : la répartition doit boucler, quantités payantes et UG comprises, avant que la commande puisse être validée. Le respect du colisage s'applique à chaque livraison.</p>

<h2>Les opérations saisonnières</h2>
<p>Les opérations sell-in de début de saison et les animations sell-out apparaissent dans le <a href="/catalogue-marques-laboratoires/">calendrier des opérations</a>, ciblées sur les pharmacies ou les groupements concernés.</p>

<h2>Le chiffre, livraison par livraison</h2>
<p>Le chiffre d'affaires d'un marché est classé dans le mois de chaque livraison : le tableau de bord montre un CA qui correspond à ce qui est réellement livré, mois après mois, et non un pic artificiel le jour de la signature.</p>

<h2>Sur le terrain</h2>
<p>La commande se prend en officine, <a href="/prise-de-commande-hors-ligne/">avec ou sans réseau</a>. Le bon de la pharmacie peut être <a href="/lecture-ia-bon-de-commande/">lu par l'IA</a>, et l'historique du client rappelle ce qu'il a commandé la saison précédente.</p>
''',
atouts=[
 'Marchés saisis une fois, livrés en plusieurs fois',
 'UG réparties sur les livraisons',
 'Colisage respecté à chaque livraison',
 'Opérations saisonnières ciblées',
 'CA classé au mois de livraison',
],
faq_titre='CelField pour les compléments alimentaires',
faq=[
 ("Combien de livraisons un marché peut-il compter ?",
  "Aujourd'hui, un marché se répartit sur trois dates de livraison au plus, chacune donnant lieu à une commande complète."),
 ("Les unités gratuites sont-elles réparties sur les livraisons ?",
  "Oui. Elles se répartissent comme les quantités payantes, et la commande ne peut être validée que si la répartition boucle exactement."),
 ("Comment le chiffre d'affaires d'un marché est-il compté ?",
  "Chaque livraison est une commande datée : son chiffre d'affaires est classé dans le mois où elle est livrée."),
],
voir_aussi=['logiciel-prise-de-commande-pharmacie', 'parapharmacie', 'lecture-ia-bon-de-commande', 'prise-de-commande-hors-ligne'],
),
]

# Colonnes du pied de page
GROUPES = [
    ('Fonctions', ['prise-de-commande-hors-ligne', 'lecture-ia-bon-de-commande',
                   'crm-agent-commercial-multicarte', 'catalogue-marques-laboratoires']),
    ('Secteurs', ['logiciel-prise-de-commande-pharmacie', 'parapharmacie',
                  'cosmetique-beaute', 'complements-alimentaires']),
]
