INSERT INTO TP5.categorie (numCategRec,nomCat) VALUES (3,'Pizza');
 
INSERT INTO TP5.Ustensile (nomUst) VALUES
('saladier'),
('top 3 des batteries de casseroles'),
('mixeur'),
('four'),
('grille'),
('louche'),
('pinceau'),
('d�noyauteur');

INSERT INTO TP5.Produit (nomProd) VALUES
('fleur de sel'),
('farine'),
('huile d olive'),
('levure'),
('eau'),
('thym'),
('tomates pel�es'),
('double concentr� de tomates'),
('oignon'),
('ail'),
('basilic frais'),
('feuille de laurier'),
('poivre'),
('sirop de sucre de canne'),
('mozzarella di buffala'),
('parmesan');

INSERT INTO TP5.Recette(nomRec, nbProd, temps,numCategRec) VALUES
('margherita', 19, '5:00:00', 3);

INSERT INTO TP5.Utiliser(numUst,numRecette)VALUES 
(2,2),
(3,2),
(4,2),
(5,2),
(6,2),
(7,2),
(8,2),
(8,2);

INSERT INTO TP5.Etape(numEtape,numRecette,description)VALUES
(1,2,'pr�paration de la p�te:'),
(2,2,'�miettez la levure puis, diluer dans la moiti� de l eau ti�de. laissez reposer 10 minutes.'),
(3,2,'dans un grand saladier, d�posez la farine et le sel puis m�langez.'),
(4,2,'ajoutez dans le saladier: l huile, la levure dilu�e et le reste d eau ti�de.'),
(5,2,'m�langez bien les ingr�dients � l aide d une grosse cuill�re par exemple.'),
(6,2,'farinez un large plan de travail puis d�posez la p�te.'),
(7,2,'p�trissez la p�te durant 10 minutes de mani�re �nergique puis, frappez-l� fort sur le plan de travail plusieurs fois.'),
(8,2,'le r�sultat: la p�te doit �tre lisse, non collante et de petites bulles d air doivent appara�tre dans la p�te.'),
(9,2,'laissez reposer une heure (4 heures serait le mieux) dans un saladier recouvert d un linge humide et chaud afin que la p�te ne cro�te pas et qu elle gonfle.'),
(10,2,'pr�paration de la sauce napolitaine fa�on gusteau:'),
(11,2,'dans une casserole, faites revenir les oignons �minc�s finement dans de l huile d olive.'),
(12,2,'une fois que les oignons ont bien su�, ajoutez les tomates pr�alablement �cras�es � la main dans un saladier.'),
(13,2,'ajoutez les gousses d ail �cras�es, le thym, le laurier, le double concentr� de tomates. salez et poivrez.'),
(14,2,'laissez mijoter � feux doux jusqu � ce que le m�lange �paississe puis, � feux tr�s doux, ajoutez le basilic frais bien nettoy� et cisel�.'),
(15,2,'ajoutez le sucre (une pierre de sucre pour ma part).'),
(16,2,'laissez encore mijoter doucement quelques minutes pour que le basilic se diffuse sans la sauce.'),
(17,2,'passez la pr�paration au mixeur � soupe, l�g�rement afin de ne pas rendre la pr�paration trop liquide. r�servez.'),
(18,2,'pr�paration des garnitures:'),
(19,2,'coupez la mozzarella en fines tranches puis �gouttez-l� entre plusieurs feuilles d essuie-tout (ceci afin qu elle ne rejette pas trop d eau lors de la cuisson).'),
(20,2,'nettoyez les feuilles de basilic frais.'),
(21,2,'rappez le parmigiano reggiano.'),
(22,2,'pr�chauffez votre four �lectrique au thermostat 9 (270�c), 30 minutes avant de commencer � dresser vos pizzas. la chaleur doit �tre statique et non tournante, une chaleur en bas et gril en haut.'),
(23,2,'disposez une grille � l �tage le plus bas de votre four.'),
(24,2,'pr�paration finale:'),
(25,2,'farinez un large plan de travail, y d�poser la p�te qui a doubl� de volume durant l heure de repos.'),
(26,2,'�crasez la p�te pour enlever l exc�dent d air.'),
(27,2,'voici la d�marche � suivre pr�cis�ment: d abord vous devez d�limiter les bords avec le bout des doigts tout en �tirant la p�te de fa�on � cr�er les bords de la pizza afin d avoir une cro�te bien marqu�e comme on peut le voir sur la photo. ensuite, �tirez la p�te selon la m�thode 12h/12h10  '),
(28,2,'c est un coup de main � prendre mais vous n �tes pas obliger de faire voler la pizza si vous n y arrivez pas.'),
(29,2,'d�posez votre p�te sur une plaque � pizza.'),
(30,2,'d�posez une louche de sauce napolitaine fa�on gusteau puis, �talez-l� � l aide de la louche. r�partir la mozarella et le parmesan.'),
(31,2,'� l aide d un pinceau culinaire, badigeonnez rapidement d huile d olive les bords de la pizza afin qu ils dorent (en effet les fours de notre cuisine ne permettent pas d obtenir une cro�te bien brunie comme les fours � pizza�olo car nos four ne sont pas assez chauds).'),
(32,2,'enfournez pour environ 8 � 10 minutes sans ouvrir.'),
(33,2,'� la sortie du four, disposez quelques feuilles de basilic.'),
(34,2,'la p�te doit �tre fine et croustillante au milieu et plus �paisse et moelleuse sur les bords (la pizza italienne se diff�rencie donc de la pizza am�ricaine qui est �paisse partout comme on peut le retrouver avec les pizzas de fast-food).'),
(35,2,'buon appetito !');

