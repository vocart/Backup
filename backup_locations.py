# list of locations to backup with their backup directories for copy_replace()
locations_copy_replace = {
	'C:/Users/Lech/Desktop/Programowanie': '//192.168.20.20/kopia pulpit/Programowanie',
	
	'H:/muza/GRAJEK': '//192.168.20.20/muzyka/GRAJEK',
	'H:/muza/REDMI': '//192.168.20.20/muzyka/REDMI',
	
	'H:/MOJE/Różne/RESZTA': '//192.168.20.20/kopia pulpit/Różne/RESZTA',
	}


# list of files to copy for copy_new_version()
locations_copy_new_version = (	
	'H:/MOJE/figurki - aukcje, kasa.xls', 
	'H:/MOJE/obiektywy.xls',
	'H:/MOJE/figurki - spis 2020.xls',
	'H:/MOJE/waga.xls'
	)


# list of locations to update (checks folders inside if they changed and updates only different)
locations_update = {
	'H:/MOJE/Warhammer i gry': '//192.168.20.20/kopia pulpit/Warhammer i gry',
	'H:/MOJE/Zdjęcia': '//192.168.20.20/zdjęcia/zdjęcia archiwalne',
	'H:/MOJE/Muzyka/mp3': '//192.168.20.20/muzyka/mp3',

	'H:/MOJE/Różne/DOM': '//192.168.20.20/kopia pulpit/Różne/DOM',
	'H:/MOJE/Różne/PRACA/': '//192.168.20.20/kopia pulpit/Różne/PRACA/',
	'H:/MOJE/Różne/PROGRAMY': '//192.168.20.20/kopia pulpit/Różne/PROGRAMY',
	'H:/MOJE/Różne/ROZRYWKA': '//192.168.20.20/kopia pulpit/Różne/ROZRYWKA',

	'E:/fotki pulpit/1. SELEKCJA ZDJĘĆ': '//192.168.20.20/zdjęcia/Zdjęcia z pulpitu/1. SELEKCJA ZDJĘĆ',
	'C:/Zdjęcia do obróbki': '//192.168.20.20/zdjęcia/Zdjęcia z pulpitu/2. Zdjęcia do obróbki',
	'E:/fotki pulpit/3. SELEKCJA RAW': '//192.168.20.20/zdjęcia/Zdjęcia z pulpitu/3. SELEKCJA RAW',
	'E:/fotki pulpit/4. GOTOWE': '//192.168.20.20/zdjęcia/Zdjęcia z pulpitu/4. GOTOWE'
	}
