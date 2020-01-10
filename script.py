from random import choice

#Objetos estelares
planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno']

planetasAnoes = ['Plutão', 'Caronte', 'Éris', 'Disnomia', 'Ceres', 'Makemake', 'Haumea']

satelites = ['Lua', 'Fobos', 'Deimos']

satelitesJupiter = ['Métis', 'Adreasteia', 'Amalteia', 'Tebe', 'Io', 'Europa', 'Ganímedes', 'Calisto', 'Temisto', 'Leda', 'Himalia', 'Lisiteia', 'Elara', 'Dia', 'Carpo', 'S/2003 J 12', 'Euporia', 'S/2003 J 3', 'S/2003 J 18', '	S/2011 J 1', 'S/2010 J 2', 'Thelxinoe', 'Euante', 'Helique', 'Ortósia', 'S/2016 J 1', '	Iocasta', '	S/2003 J 16', 'Praxidique', 'Harpalique', 'Mneme', 'Hermipe', 'Tione', 'Ananke', 'Herse', 'Aitne', 'Cale', 'Taigete', 'S/2003 J 19', 'Caldene', 'S/2003 J 15', 'S/2003 J 10', 'S/2003 J 23', 'Erinome', 'Aoede', 'Calicore', 'Calique', 'Carme', 'Caliroe', 'Euridome', 'S/2011 J 2', 'Pasite', 'S/2010 J 1', 'Coré', 'Cilene', 'Euquelade', 'S/2017 J 1', 'S/2003 J 4', 'Pasife', 'Hegemone', 'Arque', 'Isonoe', 'S/2003 J 9', 'S/2003 J 5', 'Sinope', 'Esponde', 'Autonoe', 'Megaclite', 'S/2003 J 2']

objetosEstelares = [planetas, planetasAnoes, satelites, satelitesJupiter]

objetoEscolhido = choice(objetosEstelares)
nomeProjeto = choice(objetoEscolhido)
print(nomeProjeto)