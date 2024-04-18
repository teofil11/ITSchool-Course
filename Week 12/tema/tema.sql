INSERT INTO masini VALUES(null, 'Audi', 2017, 'motorina', 'alb', 43000);
INSERT INTO masini VALUES(null, 'BMW', 2019, 'benzina', 'gri', 30000);        
INSERT INTO masini VALUES(null, 'Mercedes', 2022, 'electric', 'negru', 10000);
INSERT INTO masini VALUES(null, 'Dacia', 2007, 'benzina', 'albastru', 310000);
INSERT INTO masini VALUES(null, 'Skoda', 2009, 'motorina', 'alb', 245000);    
INSERT INTO masini VALUES(null, 'Ford', 2010, 'benzina', 'albastru', 210000); 
INSERT INTO service VALUES(null, 'Bucuresti', 'Service1');
INSERT INTO service VALUES(null, 'Cluj Napoca', 'Service2');
INSERT INTO service VALUES(null, 'Bucuresti', 'Service3');
INSERT INTO service VALUES(null, 'Timisoara', 'Service4');
INSERT INTO reparatii VALUES(null, 1, 3, 'revizie');
INSERT INTO reparatii VALUES(null, 4, 2, 'reparatie motor');
INSERT INTO reparatii VALUES(null, 2, 4, 'revizie');
INSERT INTO reparatii VALUES(null, 6, 1, 'reparatie motor');
INSERT INTO reparatii VALUES(null, 5, 3, 'reparatie turbina');

#Selectati toate masinile 
select * from tema.masini
 
#Selectati toate masinile fabricate dupa anul 2010
select * from tema.masini where an_fabricatie> 2010

#Selectati toate masinile pe benzina
select * from tema.masini where combustibil = 'benzina'

#Selectati toate masinile care nu am inca 20 000 km 
select * from tema.masini where nr_km < 20000 

#Selectati toate masinile care au culoarea albastra 
select * from tema.masini where culoare = 'albastru'

#Selectati toate Service-urile 
select * from tema.service

#Selectati toate interventiile service 
select tip_interventie from tema.reparatii

#Selectati toate interventiile service impreuna cu orasul si numele service-ului 
select reparatii.*, service.oras, service.nume
from reparatii
join service on reparatii.id_service = service.id 

#Selectati toate interventiile service impreuna cu detaliile masinii 
select reparatii.* , masini.marca, masini.an_fabricatie, masini.combustibil, masini.culoare, masini.nr_km
from reparatii
join masini on reparatii.id_masina = masini.id

#Selectati toate interventiile de tip revizie pentru masinile sub 100.000 de km 
select reparatii.*, masini.marca, masini.an_fabricatie, masini.combustibil, masini.culoare, masini.nr_km
from reparatii
join masini on reparatii.id_masina = masini.id
where reparatii.tip_interventie = 'revizie' and masini.nr_km < 100000

#Updatati toate masinile care au peste 100 000 de km, scazand 2 ani din anul fabricatiei 
update masini set an_fabricatie = an_fabricatie - 2 where nr_km > 100000

#Updatati toate interventiile de tip revizie pentru masinile care au sub 100.000 de km si redenumiti interventia in lucrare_garantie
update reparatii set tip_interventie = 'lucrare garantie'
where tip_interventie = 'revizie'
and id_masina in (select id from masini where nr_km < 100000)

#Updatati toate service-urile sa aiba locatia Bucuresti 
update service set oras = 'Bucuresti'

#Stergeti masinile fabricate inainte de 2010 
delete from masini where an_fabricatie < 2010

#Stergeti masinile de culoare rosie 
delete from masini where culoare = 'rosu'

#Stergeti toate intrarile din tabela de masini
truncate masini