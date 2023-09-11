"""
 ┌─────────────────────────────┬────────┬─────┬┬─────────────────────────────┬────────┬─────┐
 │            Talent           │ Poziom │Cecha││            Talent           │ Poziom │Cecha│
 ╞═════════════════════════════╪════════╪═════╪╪═════════════════════════════╪════════╪═════╡
 │ Atletyka                    │ 1 / 2  │ Int ││ Atletyka                    │ 1 / 2  │ Int │
 ├─────────────────────────────┼────────┼─────┼┼─────────────────────────────┼────────┼─────┤
 │ Broń Biała (Podstawowa)     │ 1 / 1  │ Int ││ Atletyka                    │ 1 / 1  │ Int │
 ├─────────────────────────────┼────────┼─────┼┼─────────────────────────────┼────────┼─────┤
"""

# Zmienna = [nazwa, cecha, poziom, maksimum]
tal_aptek = ['Aptekarz', 'Int', 0, None]
arcy = ['Arcydzieło', '', 0, 99]
artyler = ['Artylerzysta', 'Zr', 0, None]
at_wyprz = ['Atak Wyprzedzający', 'I', 0, None]
atrak = ['Atrakcyjny', 'Ogd', 0, None]
b_silny = ['Bardzo Silny', '', 0, 1]
b_szyb = ['Bardzo Szybki', '', 0, 1]
bers_szar = ['Berserkerska Szarża', 'S', 0, None]
bicz = ['Biczownik', 'Wt', 0, None]
bit_fur = ['Bitewna Furia', 'SW', 0, None]
bit_rel = ['Bitewny Reﬂeks', 'I', 0, None]
bl_krew = ['Błękitna Krew', '', 0, 1]
blogos = ['Błogosławieństwo (Boska Tradycja)', '', 0, 1]
blys_strz = ['Błyskawiczny Strzał', 'Zw', 0, None]
blysk = ['Błyskotliwość', '', 0, 1]
cel_strz = ['Celny Strzał', 'US', 0, None]
charyz = ['Charyzmatyczny', '', 0, 1]
chirurg = ['Chirurgia', 'Int', 0, None]
chodu = ['Chodu!', 'Zw', 0, None]
cien = ['Cień', 'Zw', 0, None]
cios_mierz = ['Cios Mierzony', 'I', 0, None]
cios_p_pasa = ['Cios Poniżej Pasa', 'WW', 0, None]
czarow = ['Czarownica!', 'SW', 0, None]
czl_guma = ['Człowiek Guma', 'Zw', 0, None]
czujny = ['Czujny', '', 0, 1]
czyst_dusz = ['Czysta Dusza', 'SW', 0, None]
czyt_z_warg = ['Czytanie z Ruchu Warg', 'I', 0, None]
czyt = ['Czytanie/Pisanie', '', 0, 1]
defraud = ['Defraudant', 'Int', 0, None]
przygot = ['Dobrze Przygotowany', 'I', 0, None]
wedr = ['Doświadczony Wędrowiec (Wybrany Teren)', 'Zw', 0, None]
dw_bron = ['Dwie Bronie', 'Zw', 0, None]
etykie = ['Etykieta (Grupa Społeczna)', 'Ogd', 0, None]
finta = ['Finta', 'WW', 0, None]
gadan = ['Gadanina', 'Ogd', 0, None]
gen_aryt = ['Geniusz Arytmetyczny', 'Int', 0, None]
glad_sl = ['Gładkie Słówka', 'Ogd', 0, None]
grozny = ['Groźny', 'S', 0, None]
hulaka = ['Hulaka', 'Wt', 0, None]
inspir = ['Inspirujący', 'Ogd', 0, None]
intryg = ['Intrygant', 'Int', 0, None]
inwok = ['Inwokacja (Boska Tradycja)', '', 0, 1]
krasomow = ['Krasomówstwo', 'Ogd', 0, None]
krzepki = ['Krzepki', 'Wt', 0, None]
lapowka = ['Łapówkarz', 'Ogd', 0, None]
mag_bit = ['Mag Bitewny', '', 0, 1]
mag_chaos = ['Magia Chaosu (Tradycja)', '', 0, 99]  # Zastępczo 99; Liczba dost. czarów w wybranej trad. magii Chaosu.
mag_prost = ['Magia Prosta', '', 0, 1]
mag_taj = ['Magia Tajemna (Tradycja)', '', 0, 1]
majetny = ['Majętny', '', 0, 99]
maly = ['Mały', '', 0, 1]
mist_charak = ['Mistrz Charakteryzacji', 'Ogd', 0, None]
mist_rzem = ['Mistrz Rzemiosła (Rzemiosło)', 'Zr', 0, None]
mist_walk = ['Mistrz Walki', 'Zw', 0, None]
moc_plec = ['Mocne Plecy', 'S', 0, None]
mord_atk = ['Morderczy Atak', 'I', 0, None]
mol = ['Mól Książkowy', 'Int', 0, None]
mowca = ['Mówca', 'Ogd', 0, None]
musztra = ['Musztra', 'WW', 0, None]
czt_lapy = ['Na Cztery Łapy', 'Zw', 0, None]
naciag = ['Naciągacz', 'Ogd', 0, None]
naslad = ['Naśladowca', 'I', 0, None]
nieg_uwg = ['Niegodny Uwagi', 'Ogd', 0, None]
nienaw = ['Nienawiść (Grupa)', 'SW', 0, None]
nieublag = ['Nieubłagany', 'Wt', 0, None]
nieug = ['Nieugięty', 'S', 0, None]
nieust = ['Nieustępliwy', 'Zw', 0, None]
nieustr = ['Nieustraszony (typ wroga)', 'SW', 0, None]
niewzr = ['Niewzruszony', 'SW', 0, None]
niezw_odp = ['Niezwykle Odporny', '', 0, 1]
nos_klop = ['Nos do Kłopotów', 'I', 0, None]
numizm = ['Numizmatyka', 'I', 0, None]
obiez = ['Obieżyświat', 'Int', 0, None]
obur = ['Oburęczność', '', 0, 2]
odp_mag = ['Odporność na Magię', 'Wt', 0, None]
odp_psych = ['Odporność Psychiczna', 'SW', 0, None]
odp_zagr = ['Odporny na (Zagrożenie)', 'Wt', 0, None]
odw_szans = ['Odwrócenie Szans', 'WW', 0, None]
oglusz = ['Ogłuszenie', 'WW', 0, None]
oko_low = ['Oko Łowcy', 'I', 0, None]
perc_mag = ['Percepcja Magiczna', 'I', 0, None]
pierw_pom = ['Pierwsza Pomoc', 'Int', 0, None]
pilot = ['Pilot', 'I', 0, None]
pilot_rzecz = ['Pilot Rzeczny', 'I', 0, None]
poligl = ['Poliglota', 'Int', 0, None]
pomocny = ['Pomocny', 'Ogd', 0, None]
poryw_gorl = ['Porywająca Gorliwość', 'Ogd', 0, None]
posl_zwierz = ['Posłuch u Zwierząt', 'SW', 0, None]
prec_ink = ['Precyzyjne Inkantowanie', 'I', 0, None]
prst_ocz = ['Prosto Między Oczy', '', 0, 1]
przek = ['Przekonujący', 'Ogd', 0, None]
przest = ['Przestępca', '', 0, 99]
prz_miks = ['Przyrządzanie Mikstur', 'Int', 0, None]
riposta = ['Riposta', 'Zw', 0, None]
rozbr = ['Rozbrojenie', 'I', 0, None]
rozp_art = ['Rozpoznanie Artefaktu', 'I', 0, None]
rozpr_mag = ['Rozproszenie Uwagi', 'Zw', 0, None]
ruch_dlo = ['Ruchliwe dłonie', 'Zr', 0, None]
rybak = ['Rybak', 'I', 0, None]
sekr_toz = ['Sekretna Tożsamość', 'Int', 0, None]
sil_nog = ['Silne Nogi', 'S', 0, None]
sil_cios = ['Silny Cios', 'S', 0, None]
skr_dyst = ['Skrócenie Dystansu', 'Zr', 0, None]
slch_abs = ['Słuch Absolutny', 'I', 0, None]
snajp = ['Snajper', '', 0, 4]
sprez = ['Sprężynka', '', 0, 1]
strasz = ['Straszny', 'S', 0, None]
strz_przeb = ['Strzał Przebijający', 'I', 0, None]
sztrz_dzies = ['Strzał w Dziesiątkę', '', 0, 1]
strz_wyb = ['Strzelec Wyborowy', '', 0, 1]
szal_boj = ['Szał Bojowy', '', 0, 1]
szczesc = ['Szczęście', 'Ogd', 0, None]
szczor_tun = ['Szczur Tunelowy', 'Zw', 0, None]
szost_zm = ['Szósty Zmysł', 'I', 0, None]
szuler = ['Szuler', 'Int', 0, None]
szuler_kosc = ['Szuler Kościany', 'Int', 0, None]
szyb_ref = ['Szybki Reﬂeks', '', 0, 1]
szyb_czyt = ['Szybkie Czytanie', 'Int', 0, None]
szyb_przel = ['Szybkie Przeładowanie', 'Zr', 0, None]
szyb_bieg = ['Szybkobiegacz', 'S', 0, None]
szycha = ['Szycha', '', 0, 1]
sw_plyw = ['Świetny Pływak', 'S', 0, None]
sw_nienaw = ['Święta Nienawiść', 'Ogd', 0, None]
sw_wizje = ['Święte Wizje', 'I', 0, None]
tal_art = ['Talent Artystyczny', 'Zr', 0, None]
tarcz = ['Tarczownik', 'S', 0, None]
towarz = ['Towarzyski', 'Ogd', 0, None]
trag = ['Tragarz', 'S', 0, None]
trap = ['Traper', 'I', 0, None]
tward = ['Twardziel', 'Wt', 0, None]
ulicz = ['Ulicznik', 'I', 0, None]
ur_siod = ['Urodzony w Siodle', 'Zw', 0, None]
ur_woj = ['Urodzony Wojownik', '', 0, 1]
ur_zegl = ['Urodzony Żeglarz', 'Wt', 0, None]
wal_ser = ['Waleczne Serce', 'SW', 0, None]
wal_cias = ['Walka w Ciasnocie', 'Zw', 0, None]
widz_ciem = ['Widzenie w Ciemności', 'I', 0, None]
wiez_pam = ['Wieża Pamięci', 'Int', 0, None]
wilk_mor = ['Wilk Morski', 'Zw', 0, None]
wlad_post = ['Władcza Postura', 'Ogd', 0, None]
wlocz = ['Włóczykij', 'Zr', 0, None]
wodniak = ['Wodniak', 'Zw', 0, None]
woltyz = ['Woltyżerka', 'Zw', 0], None
wodz = ['Wódz', 'Ogd', 0, None]
wroz_los = ['Wróżba Losu', '', 0, 1]
wstrz = ['Wstrzemięźliwy', 'Wt', 0, None]
wsciek_atk = ['Wściekły Atak', 'Zw', 0, None]
wtarg_wlam = ['Wtargnięcie z Włamaniem', 'S', 0, None]
wyb_wspin = ['Wyborny Wspinacz', 'S', 0, None]
wycz_kier = ['Wyczucie Kierunku', 'I', 0, None]
wycz_zmys = ['Wyczulony Zmysł', 'I', 0, None]
wykr_mag = ['Wykrywanie Magii', 'I', 0, None]
wytrw = ['Wytrwały', 'Wt', 0, None]
wytw = ['Wytwórca', 'Zr', 0, None]
zbat = ['Z Bata', 'Zr', 0, None]
zabojca = ['Zabójca', '', 0, 1]
zbic_bron = ['Zbicie Broni', 'WW', 0, None]
zej_lin = ['Zejście z Linii', 'Zw', 0, None]
zim_krew = ['Zimna krew', '', 0, 1]
zl_racz = ['Złota Rączka', 'Zr', 0, None]
zm_bit = ['Zmysł Bitewny', 'I', 0, None]
zm_mag = ['Zmysł Magii', 'I', 0, None]
znaw = ['Znawca (Wiedza)', 'Int', 0, None]
zrecz = ['Zręczny', '', 0, 1]
zel_szcz = ['Żelazna Szczęka', 'Wt', 0, None]
zel_wola = ['Żelazna Wola', 'SW', 0, None]
zyl_hand = ['Żyłka Handlowa', 'Ogd', 0, None]


'''
TABELA LOSOWYCH TALENTÓW
Rzut Talent Rzut Talent
01-03 Atrakcyjny 50-52 Silne Nogi
04-06 Bardzo Silny 53-55 Słuch Absolutny
07-08 Błękitna Krew 56-58 Strzelec Wyborowy
09-11 Błyskotliwość 59-62 Szczęście
12-14 Charyzmatyczny 63-66 Szósty Zmysł
15-17 Chodu! 67-69 Szybki Reﬂeks
18-20 Czujny 70-72 Talent Artystyczny
21-24 Czysta Dusza 73-75 Tragarz
25-27 Czytanie/Pisanie 76-79 Twardziel
28-31 Geniusz Arytmetyczny 80-82 Urodzony Wojownik
32-34 Naśladowca 83-85 Widzenie w Ciemności
35-37 Niezwykle Odporny 86-88 Wyczucie Kierunku
38-40 Oburęczność 89-91 Wyczulony Zmysł
(Dowolny)
41-43 Odporny na (Dowolne
Zagrożenie) 92-94 Wytwórca (Dowolny)
44-46 Poliglota 95-97 Zimna Krew
47-49 Posłuch u Zwierząt 98-100 Zręczny'''