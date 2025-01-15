--# Sample Data for endangered Species

CREATE TABLE endangered_species(
common_namevarchar2(200),
scientific_namevarchar2(200),
conservation_statusvarchar2(100)
);

BEGIN 
 /* https://www.worldwildlife.org/species/directory?direction=desc&sort=extinction_status */
INSERT INTO endangered_species
VALUES ('African forest elephant',null,'Critically Endangered');
INSERT INTO endangered_species
VALUES ('Amur Leopard','Panthera pardus orientalis','Critically Endangered');
INSERT INTO endangered_species
VALUES ('Black Rhino','Diceros bicornis''Critically Endangered');
INSERT INTO endangered_species
VALUES ('Bornean Orangutan','Pongo pygmaeus','Critically Endangered');
INSERT INTO endangered_species
VALUES ('Cross River Gorilla','Gorilla gorilla diehli','Critically Endangered');
INSERT INTO endangered_species
VALUES ('Eastern Lowland Gorilla','Gorilla beringei graueri','Critically Endangered');
INSERT INTO endangered_species
VALUES ('Hawksbill Turtle','Eretmochelys imbricata','Critically Endangered');
INSERT INTO endangered_species
VALUES ('Javan Rhino','Rhinoceros sondaicus','Critically Endangered');
INSERT INTO endangered_species
VALUES ('Orangutan','Pongo abelii, Pongo pygmaeus','Critically Endangered');
INSERT INTO endangered_species
VALUES ('Saola','Pseudoryx nghetinhensis','Critically Endangered');
INSERT INTO endangered_species
VALUES ('Sumatran Elephant','Elephas maximus sumatranus','Critically Endangered');
INSERT INTO endangered_species
VALUES ('Sumatran Orangutan','Pongo abelii','Critically Endangered');
INSERT INTO endangered_species
VALUES ('Sumatran Rhino','Dicerorhinus sumatrensis','Critically Endangered');
INSERT INTO endangered_species
VALUES ('Sunda Tiger','Panthera tigris sondaica','Critically Endangered');
INSERT INTO endangered_species
VALUES ('Vaquita','Phocoena sinus','Critically Endangered');
INSERT INTO endangered_species
VALUES ('Western Lowland Gorilla','Gorilla gorilla gorilla','Critically Endangered');
INSERT INTO endangered_species
VALUES ('Yangtze Finless Porpoise','Neophocaena asiaeorientalis ssp. asiaeorientalis','Critically Endangered');
INSERT INTO endangered_species
VALUES ('African savanna elephant','Loxodonta africana africana','Endangered');
INSERT INTO endangered_species
VALUES ('African Wild Dog','Lycaon pictus','Endangered');
INSERT INTO endangered_species
VALUES ('Asian Elephant','Elephas maximus indicus','Endangered');
INSERT INTO endangered_species
VALUES ('Black-footed Ferret','Mustela nigripes','Endangered');
INSERT INTO endangered_species
VALUES ('Blue Whale','Balaenoptera musculus','Endangered');
INSERT INTO endangered_species
VALUES ('Bluefin Tuna','Thunnus Thynnus','Endangered');
INSERT INTO endangered_species
VALUES ('Bonobo','Pan paniscus','Endangered');
INSERT INTO endangered_species
VALUES ('Bornean Elephant','Elephas maximus borneensis','Endangered');
INSERT INTO endangered_species
VALUES ('Chimpanzee','Pan troglodytes','Endangered');
INSERT INTO endangered_species
VALUES ('Fin Whale','Balaenoptera physalus','Endangered');
INSERT INTO endangered_species
VALUES ('Galápagos Penguin','Spheniscus mendiculus','Endangered');
INSERT INTO endangered_species
VALUES ('Ganges River Dolphin','Platanista gangetica gangetica','Endangered');
INSERT INTO endangered_species
VALUES ('Green Turtle','Chelonia mydas','Endangered');
INSERT INTO endangered_species
VALUES ('Hector\'s Dolphin','Cephalorhynchus hectori','Endangered');
INSERT INTO endangered_species
VALUES ('Humphead Wrasse','Cheilinus undulatus','Endangered');
INSERT INTO endangered_species
VALUES ('Indian Elephant','Elephas maximus indicus','Endangered');
INSERT INTO endangered_species
VALUES ('Indus River Dolphin','Platanista minor','Endangered');
INSERT INTO endangered_species
VALUES ('Irrawaddy Dolphin','Orcaella brevirostris','Endangered');
INSERT INTO endangered_species
VALUES ('Monarch Butterfly','Danaus plexippus','Endangered');
INSERT INTO endangered_species
VALUES ('Mountain Gorilla','Gorilla beringei beringei','Endangered');
INSERT INTO endangered_species
VALUES ('North Atlantic Right Whale','Eubalaena glacialis','Endangered');
INSERT INTO endangered_species
VALUES ('Red Panda','Ailurus fulgens','Endangered');
INSERT INTO endangered_species
VALUES ('Sea Lions','Zalophus wollebaeki','Endangered');
INSERT INTO endangered_species
VALUES ('Sea Turtle','Cheloniidae and Dermochelyidae families','Endangered');
INSERT INTO endangered_species
VALUES ('Sei Whale','Balaenoptera borealis','Endangered');
INSERT INTO endangered_species
VALUES ('Sri Lankan Elephant','Elephas maximus maximus','Endangered');
INSERT INTO endangered_species
VALUES ('Tiger','Panthera tigris','Endangered');
INSERT INTO endangered_species
VALUES ('Whale','Balaenoptera, Balaena, Eschrichtius, and Eubalaen','Endangered');
INSERT INTO endangered_species
VALUES ('Whale Shark','Rhincodon typus','Endangered');
INSERT INTO endangered_species
VALUES ('Bigeye Tuna','Thunnus obesus','Vulnerable');
INSERT INTO endangered_species
VALUES ('Black Spider Monkey','Ateles paniscus','Vulnerable');
INSERT INTO endangered_species
VALUES ('Dugong','Dugong dugon','Vulnerable');
INSERT INTO endangered_species
VALUES ('Giant Panda','Ailuropoda melanoleuca','Vulnerable');
INSERT INTO endangered_species
VALUES ('Giant Tortoise','','Vulnerable');
INSERT INTO endangered_species
VALUES ('Great White Shark','Carcharodon carcharias','Vulnerable');
INSERT INTO endangered_species
VALUES ('Greater One-Horned Rhino','Rhinoceros unicornis','Vulnerable');
INSERT INTO endangered_species
VALUES ('Hippopotamus','Hippopotamus amphibius','Vulnerable');
INSERT INTO endangered_species
VALUES ('Leatherback Turtle','Dermochelys coriacea','Vulnerable');
INSERT INTO endangered_species
VALUES ('Lion','Panthera Leo','Vulnerable');
INSERT INTO endangered_species
VALUES ('Loggerhead Turtle','Caretta caretta','Vulnerable');
INSERT INTO endangered_species
VALUES ('Marine Iguana','Amblyrhynchus cristatus','Vulnerable');
INSERT INTO endangered_species
VALUES ('Olive Ridley Turtle','Lepidochelys olivacea','Vulnerable');
INSERT INTO endangered_species
VALUES ('Polar Bear','Ursus maritimus','Vulnerable');
INSERT INTO endangered_species
VALUES ('Snow Leopard','Panthera uncia','Vulnerable');
INSERT INTO endangered_species
VALUES ('Southern rockhopper penguin','Eudyptes chrysocome','Vulnerable');
INSERT INTO endangered_species
VALUES ('Albacore Tuna','Thunnus alalunga','Near Threatened');
INSERT INTO endangered_species
VALUES ('Beluga','Delphinapterus leucas','Near Threatened');
INSERT INTO endangered_species
VALUES ('Greater Sage-Grouse','Centrocercus urophasianus','Near Threatened');
INSERT INTO endangered_species
VALUES ('Jaguar','Panthera onca','Near Threatened');
INSERT INTO endangered_species
VALUES ('Mountain Plover','Charadrius montanus','Near Threatened');
INSERT INTO endangered_species
VALUES ('Plains Bison','Bison bison bison','Near Threatened');
INSERT INTO endangered_species
VALUES ('White Rhino','Ceratotherium simum','Near Threatened');
INSERT INTO endangered_species
VALUES ('Yellowfin Tuna','Thunnus albacares','Near Threatened');
INSERT INTO endangered_species
VALUES ('Arctic Fox','Vulpes lagopus','Least Concern');
INSERT INTO endangered_species
VALUES ('Arctic Wolf','Canis lupus arctos','Least Concern');
INSERT INTO endangered_species
VALUES ('Bowhead Whale','Balaena mysticetus','Least Concern');
INSERT INTO endangered_species
VALUES ('Brown Bear','Ursus arctos','Least Concern');
INSERT INTO endangered_species
VALUES ('Common Bottlenose Dolphin','Tursiops truncates','Least Concern');
INSERT INTO endangered_species
VALUES ('Gray Whale','Eschrichtius robustus','Least Concern');
INSERT INTO endangered_species
VALUES ('Macaw','Ara ararauna','Least Concern');
INSERT INTO endangered_species
VALUES ('Narwhal','Monodon monoceros','Least Concern');
INSERT INTO endangered_species
VALUES ('Pronghorn','Antilocarpa americana','Least Concern');
INSERT INTO endangered_species
VALUES ('Skipjack Tuna','Katsuwonus pelamis','Least Concern');
INSERT INTO endangered_species
VALUES ('Swift Fox','Vulpes velox','Least Concern');
INSERT INTO endangered_species
VALUES ('Tree Kangaroo','Dendrolagus sp.','Least Concern');
INSERT INTO endangered_species
VALUES ('African Elephant','Loxodonta africana',null);
INSERT INTO endangered_species
VALUES ('Amazon River Dolphin','Scientific Name Inia geoffrensis ',null);
INSERT INTO endangered_species
VALUES ('Continental Tiger','Panthera tigris tigris', null);
INSERT INTO endangered_species
VALUES ('Dolphins and Porpoises', null, null);
INSERT INTO endangered_species
VALUES ('Elephant ', null, null);
INSERT INTO endangered_species
VALUES ('Gorilla','Gorilla gorilla and Gorilla beringei' null);
INSERT INTO endangered_species
VALUES ('Pacific Salmon ', null, null);
INSERT INTO endangered_species
VALUES ('Pangolin ', null, null);
INSERT INTO endangered_species
VALUES ('Penguin','Spheniscidae', null);
INSERT INTO endangered_species
VALUES ('Poison Dart Frog','Dendrobates species', null);
INSERT INTO endangered_species
VALUES ('Rhino', null, null);
INSERT INTO endangered_species
VALUES ('Seals', null, null);
INSERT INTO endangered_species
VALUES ('Shark', null, null);
INSERT INTO endangered_species
VALUES ('Sloth', null, null);
INSERT INTO endangered_species
VALUES ('Tuna','Thunnus and Katsuwonus species', null);
commit;
END;
























