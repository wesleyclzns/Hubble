from random import choice

#Objetos estelares
planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno']

planetasAnoes = ['Plutão', 'Caronte', 'Éris', 'Disnomia', 'Ceres', 'Makemake', 'Haumea']

satelites = ['Lua', 'Fobos', 'Deimos']

satelitesJupiter = ['Métis', 'Adreasteia', 'Amalteia', 'Tebe', 'Io', 'Europa', 'Ganímedes', 'Calisto', 'Temisto', 'Leda', 'Himalia', 'Lisiteia', 'Elara', 'Dia', 'Carpo', 'S/2003 J 12', 'Euporia', 'S/2003 J 3', 'S/2003 J 18', '	S/2011 J 1', 'S/2010 J 2', 'Thelxinoe', 'Euante', 'Helique', 'Ortósia', 'S/2016 J 1', '	Iocasta', '	S/2003 J 16', 'Praxidique', 'Harpalique', 'Mneme', 'Hermipe', 'Tione', 'Ananke', 'Herse', 'Aitne', 'Cale', 'Taigete', 'S/2003 J 19', 'Caldene', 'S/2003 J 15', 'S/2003 J 10', 'S/2003 J 23', 'Erinome', 'Aoede', 'Calicore', 'Calique', 'Carme', 'Caliroe', 'Euridome', 'S/2011 J 2', 'Pasite', 'S/2010 J 1', 'Coré', 'Cilene', 'Euquelade', 'S/2017 J 1', 'S/2003 J 4', 'Pasife', 'Hegemone', 'Arque', 'Isonoe', 'S/2003 J 9', 'S/2003 J 5', 'Sinope', 'Esponde', 'Autonoe', 'Megaclite', 'S/2003 J 2']

satelitesSaturno = ['S/2019 S1', 'Pã', 'Defne', 'Atlas', 'Prometeu', 'Pandora', 'Epimeteu', 'Jano', 'Aegeon', 'Mimas', 'Methone', 'Anthe', 'Palene', 'Encélado', 'Tétis', 'Telesto', 'Calipso', 'Dione', 'Helene', 'Polideuces', 'Reia', 'Titã', 'Hipérion', 'Jepeto', 'Kiviuq', 'Ijiraq', 'Febe', 'Paaliaq', 'Skathi', 'Albiorix', 'S/2007 S 2', 'Bebhionn', 'Erriapo', 'Siarnaq', 'Skoll', 'Tavos', 'Tarqeq', 'Greip', 'S/2004 S 13', 'Hyrrokkin', 'Murdilfari', 'Jarnsaxa', 'S/2006 S 1', 'S/2007 S 3', 'Narvi', 'Bergelmir', 'S/2004 S 12', 'Bestla', 'Farbauti', 'Thymr', 'Aegir', 'S/2004 S7', 'S/2006 S 3', 'Kari', 'Fenrir', 'Surtur', 'Ymir', 'Loge', 'Fornjot']

satelitesNetuno = ['Cordélia', 'Ofélia', 'Bianca', 'Créssida', 'Desdémone', 'Julieta', 'Pórcia', 'Rosalinda', 'Cupido', 'Belinda', 'Perdita', 'Puck', 'Mab', 'Miranda', 'Ariel', 'Umbriel', 'TItânia', 'Oberon', 'Francisco', 'Caliban', 'Stephano', 'Thincolo', 'Sycorax', 'Margaret', 'Prospero', 'Setebos', 'Ferdinand']

asteroides = ['3753 Cruithne', 'Hungrias', 'Phocaeas', 'Nysas', 'Alindas', 'Hildas', 'Pallas', 'Maria', 'Koronis', 'Eos', 'Themis', 'Griquas', 'Cibeles', 'Thule', 'Vesta', '5335 Dâmocles', '1996 PW',  ]

cometas = ['2060 Quíron', '95/P Chiron']

NEO = ['2004 FH', '2004 FU'] 

estrelas = ['Westerlund 1', 'UY Scuti', 'WOH G64', 'RW Cephei', 'Westerlund 1-26', 'VX Sagittari', 'KY Cygni', 'KY Canis Majoris', 'AH Scorpii', 'VV Cephei A', 'Mu Cephei', 'HR 5171 A', 'BI Cygni', 'S Persei', 'RAFGL 2139', 'PZ Cassiopeiae', 'BC Cygni', 'RT Carinae', 'V396 Centauri', 'CK Carinae', 'V1749 Cygni', 'U Lacertae', 'KW Sagittarii', 'RS Persei', 'NR Vulpeculae', 'RW Cygni', 'GCIRS 7', 'HV 212', 'Betelgeuse', 'V602 Carinae', 'Tz Cassiopeiae', 'Antares A', 'IX Carinae', 'SU Persei', 'TV Geminorum', 'V355 Cepheus', 'V382 Carinae', 'V354 Cephei', '119 Tauri', 'S Pegasi', 'T Cephei', 'S Orions', 'W Hydrae', 'R Leporis', 'Rho Cessiopeiae', 'Mira', 'V838 Monocerotis', 'S Doradus', 'R Doradus', 'Pistol Star', 'Chi Cygni', 'Ras Algethi', 'Deneb', 'LBV 1806-20', 'Epsilon Aurigae', 'Wr 102ka', 'Gacrux', 'Rigel', 'Canopus', 'Albireo', 'Aldebra', 'Polaris', 'RMC 136a1', 'Arcturo', 'Alnitak', 'Cygnus X-1', 'Capella', 'VV Cephei B', 'WR 104']

objetosEstelares = [planetas, planetasAnoes, satelites, satelitesJupiter, satelitesNetuno, satelitesSaturno, asteroides, cometas, NEO, estrelas]

objetoEscolhido = choice(objetosEstelares)
nomeProjeto = choice(objetoEscolhido)
print(nomeProjeto)