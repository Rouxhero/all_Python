INSERT INTO TP5.categorie (numCategRec,nomCat) VALUES (3,'Pizza');
 
INSERT INTO TP5.Ustensile (nomUst) VALUES
('saladier'),
('top 3 des batteries de casseroles'),
('mixeur'),
('four'),
('grille'),
('louche'),
('pinceau'),
('dénoyauteur');

INSERT INTO TP5.Produit (nomProd) VALUES
('fleur de sel'),
('farine'),
('huile d olive'),
('levure'),
('eau'),
('thym'),
('tomates pelées'),
('double concentré de tomates'),
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
(1,2,'préparation de la pâte:'),
(2,2,'émiettez la levure puis, diluer dans la moitié de l eau tiède. laissez reposer 10 minutes.'),
(3,2,'dans un grand saladier, déposez la farine et le sel puis mélangez.'),
(4,2,'ajoutez dans le saladier: l huile, la levure diluée et le reste d eau tiède.'),
(5,2,'mélangez bien les ingrédients à l aide d une grosse cuillère par exemple.'),
(6,2,'farinez un large plan de travail puis déposez la pâte.'),
(7,2,'pétrissez la pâte durant 10 minutes de manière énergique puis, frappez-là fort sur le plan de travail plusieurs fois.'),
(8,2,'le résultat: la pâte doit être lisse, non collante et de petites bulles d air doivent apparaître dans la pâte.'),
(9,2,'laissez reposer une heure (4 heures serait le mieux) dans un saladier recouvert d un linge humide et chaud afin que la pâte ne croûte pas et qu elle gonfle.'),
(10,2,'préparation de la sauce napolitaine façon gusteau:'),
(11,2,'dans une casserole, faites revenir les oignons émincés finement dans de l huile d olive.'),
(12,2,'une fois que les oignons ont bien sué, ajoutez les tomates préalablement écrasées à la main dans un saladier.'),
(13,2,'ajoutez les gousses d ail écrasées, le thym, le laurier, le double concentré de tomates. salez et poivrez.'),
(14,2,'laissez mijoter à feux doux jusqu à ce que le mélange épaississe puis, à feux très doux, ajoutez le basilic frais bien nettoyé et ciselé.'),
(15,2,'ajoutez le sucre (une pierre de sucre pour ma part).'),
(16,2,'laissez encore mijoter doucement quelques minutes pour que le basilic se diffuse sans la sauce.'),
(17,2,'passez la préparation au mixeur à soupe, légèrement afin de ne pas rendre la préparation trop liquide. réservez.'),
(18,2,'préparation des garnitures:'),
(19,2,'coupez la mozzarella en fines tranches puis égouttez-là entre plusieurs feuilles d essuie-tout (ceci afin qu elle ne rejette pas trop d eau lors de la cuisson).'),
(20,2,'nettoyez les feuilles de basilic frais.'),
(21,2,'rappez le parmigiano reggiano.'),
(22,2,'préchauffez votre four électrique au thermostat 9 (270°c), 30 minutes avant de commencer à dresser vos pizzas. la chaleur doit être statique et non tournante, une chaleur en bas et gril en haut.'),
(23,2,'disposez une grille à l étage le plus bas de votre four.'),
(24,2,'préparation finale:'),
(25,2,'farinez un large plan de travail, y déposer la pâte qui a doublé de volume durant l heure de repos.'),
(26,2,'écrasez la pâte pour enlever l excédent d air.'),
(27,2,'voici la démarche à suivre précisément: d abord vous devez délimiter les bords avec le bout des doigts tout en étirant la pâte de façon à créer les bords de la pizza afin d avoir une croûte bien marquée comme on peut le voir sur la photo. ensuite, étirez la pâte selon la méthode 12h/12h10  '),
(28,2,'c est un coup de main à prendre mais vous n êtes pas obliger de faire voler la pizza si vous n y arrivez pas.'),
(29,2,'déposez votre pâte sur une plaque à pizza.'),
(30,2,'déposez une louche de sauce napolitaine façon gusteau puis, étalez-là à l aide de la louche. répartir la mozarella et le parmesan.'),
(31,2,'à l aide d un pinceau culinaire, badigeonnez rapidement d huile d olive les bords de la pizza afin qu ils dorent (en effet les fours de notre cuisine ne permettent pas d obtenir une croûte bien brunie comme les fours à pizzaïolo car nos four ne sont pas assez chauds).'),
(32,2,'enfournez pour environ 8 à 10 minutes sans ouvrir.'),
(33,2,'à la sortie du four, disposez quelques feuilles de basilic.'),
(34,2,'la pâte doit être fine et croustillante au milieu et plus épaisse et moelleuse sur les bords (la pizza italienne se différencie donc de la pizza américaine qui est épaisse partout comme on peut le retrouver avec les pizzas de fast-food).'),
(35,2,'buon appetito !');

