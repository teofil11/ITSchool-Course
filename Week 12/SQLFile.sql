#selectati toate persoanele din tabela persoane
SELECT * FROM `curs`.`persoane`;
#selectati nume si prenume din tabela persoane
SELECT nume, prenume FROM curs.persoane;
#selectati persoanele care au id-ul mai mare ca 1 
SELECT * FROM curs.persoane WHERE id>2;
#selectati toate calsele 
SELECT * FROM curs.clase;
#am ore dupa ora 6 iarna si am nevoie de cat mai multa lumina. Care e numarul maxim de geamuri 
SELECT MAX(numar_geamuri) from curs.clase;
#selectati clasele care au mai mult de 40 de geamuri
SELECT * FROM curs.clase WHERE NUMAR_GEAMURI>40;
#selectati toate persoanele si clasele din care acestea fac parte cu toate detaliile lor 
SELECT * FROM PERSOANE,
              PERSOANA_CLASA,
              CLASE
		WHERE PERSOANE.ID=PERSOANA_CLASA.ID_PERSOANA
         AND  CLASE.ID=PERSOANA_CLASA.ID_CLASA;
         
#inserati 2 persoane in tabelul persoane 
INSERT INTO PERSOANE VALUES(null,'Hagi','Gica','brunet');
INSERT INTO PERSOANE VALUES(null,'Marin','Cosmin','blond');

#selectam persoane 
select * from persoane;

#update pentru toate intrarile a.i. toti cei cu parul brunet sa fie notati cu parul negru 
SET SQL_SAFE_UPDATES = 0;
UPDATE PERSOANE SET CULOARE_PAR='negru' where CULOARE_PAR='Brunet';
UPDATE PERSOANE SET CULOARE_PAR='galben' WHERE CULOARE_PAR='Saten' OR CULOARE_PAR='BLOND';

#faceti update a.i. toate persoanele cu numele Badea sau Olteanu cu culoarea parului negru sa aiba porecla par-negru
UPDATE PERSOANE SET PORECLA='par-negru' WHERE CULOARE_PAR='negru' and (nume='Badea' OR nume='Olteanu');

#cate persoane au fiecare tip de culoare a parului 
SELECT CULOARE_PAR,COUNT(*) FROM PERSOANE GROUP BY CULOARE_PAR;

#stergeti toate persoanele care au parul galben 
DELETE FROM PERSOANE WHERE CULOARE_PAR='galben';

#stergeti toate persoanele care nu au porecla 
delete  FROM PERSOANE WHERE PORECLA='fara';

#golesc toata tabela 
delete from PERSOANE WHERE 1=1;
truncate PERSOANE;

#sintaxa generata din python 
INSERT INTO PERSOANE VALUES(null,'Hagi','Gica','Brunet','fara');
INSERT INTO PERSOANE VALUES(null,'Ionut','Popescu','Saten','fara');
INSERT INTO PERSOANE VALUES(null,'Mihai','Vancica','Blond','fara');
INSERT INTO PERSOANE VALUES(null,'Mihai','Viteazul','Necunoscut','fara');
INSERT INTO PERSOANE VALUES(null,'Stelica','Ion','Blond','fara');














