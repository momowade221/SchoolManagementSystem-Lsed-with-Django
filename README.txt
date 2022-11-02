I) COMPTES 
superuser: {USERNAME: momowade, PWD:momowade}
admin(site): {USERNAME: admin,PWD:admin}
prof(site): {USERNAME: seck,PWD:seck}
eleve(site): {USERNAME: diouf,PWD:diouf}

II) FONCTIONNALITES
L'application est un système d'information pour le Lycée Scientifique d'Excellence de Diourbzl
Trois types d'acteurs sont implémentés:
1)LES ADMINISTRATEURS(PROVISEUR, CENSEUR):
+ils peuvent créer, lire, modifier, supprimer les informations des élèves profs et élèves
+ils doivent approuver les comptes des profs et élèves une fois inscrits
+ils peuvent  faire des annonces à l'ensemble des élèves et profs
+ils peuvent prendre l'absence des profs et élèves
+ils peuvent gérer les frais de scolarité des élèves
+ils peuvent gérer les salaires des professuers
2) LES PROFESSEUERS
Après l'inscription et approbation des administrateurs,
+ils peuvent se connecter
+ils peuvent voir les  annonces faites par les administrateurs 
+ils peuvent faire des annonces aux élèves
+ils peuvent voir leur présences et absences
3) LES ELEVES
Après l'inscription et approbation des administrateurs,
+ils peuvent se connecter
+ils peuvent voir les annonces faites par les administrateurs et les profs
+ils peuvent voir leur présences et absences

III) API
+Les informations de l'API peuvent être accédées via l'authentification et le token