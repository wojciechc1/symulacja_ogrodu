Projekt zaliczeniowy -- Wojciech Cieciura

Tresc zadania
W dużym kwadratowym ogrodzie żyje gromadka kotów i sporo myszy. Od rana koty uganiają się za myszami
i wydeptują ścieżki. Czasem kot i mysz mogą spotkać się w jednym miejscu. Jak kończy się taka sytuacja? To
zależy (opis możliwych scenariuszy poniżej). Wieczorem na trawie widać ścieżki wydeptane przez zwierzęta.
Na początku symulacji umieszczamy koty i myszy w ogródku. Lista położeń początkowych (czyli położeń
kocich pudełek/mysich norek) wszystkich kotów i myszy wczytywana jest z plików, których opis znajduje
się nieco dalej. Na jej podstawie należy stworzyć wszystkie obiekty reprezentujące zwierzęta.
W ciągu dnia zarówno koty, jak i myszy poruszają się po ogrodzie, każdy na swój sposób:
 
 Myszy są małe, więc robią małe kroczki. W jednym momencie mogą co najwyżej zmienić swoją pozycję
(x, y) o 1 (lub nie zmienić wcale) w każdym kierunku. Wyjątek stanowi ucieczka, wtedy mysz nabiera
supermocy i teleportuje się do swojego schronienia, niezależnie jak to daleko.
 
 Koty Przeciętniaki oraz Koty Leniuchy poruszają się w losowym kierunku zmieniając położenie o co
najwyżej 10, zarówno w kierunku x, jak i y.

 Kociaki poruszają się w losowym kierunku, zmieniają swoją pozycję (każdą współrzędną) o co najwyżej
5, ale nigdy nie oddalają się od swojego domu o odległość większą niż 100. Jeśli nowe położenie
sprawiłoby, że kociak oddali się od domu o ponad 100, to zamiast tego wraca do poprzedniego położenia.

Uwaga: Każdy zwierzak pamięta wszystkie swoje położenia.
Jeśli mysz znajdzie się w odległości mniejszej niż 4 od kota, to następuje ich spotkanie. Spotkanie kota i
myszy może przebiegać różnie:

 Koty Przeciętniaki, których jest najwięcej, po prostu zawsze trącają mysz łapką, ona teleportuje się
do swojego domku, a kot jest zadowolony.

 Kociaki są bardzo młode i praktycznie zawsze boją się myszy, a gdy ją spotkają, natychmiast tele-
portują się do swojego pudła. Mysz nadal normalnie spaceruje sobie po ogródku. Jednak jeżeli jakimś
cudem spotkają mysz w pobliżu swojego pudełka (w promieniu 50), wtedy stają się odważne i potrafią
przestraszyć gryzonia na tyle, że tym razem to on teleportuje się natychmiast do swojej kryjówki.
 
 Koty Leniuchy są względnie niegroźne. Gdy spotkają mysz, nawet w swoim mieszkanku, często zupełnie
się nią nie przejmują i po spotkaniu każde z nich idzie w swoją stronę jak gdyby nic się nie stało.
Czasem jednak kot trąca mysz łapką, ta ucieka (teleportuje się) do kryjówki, a kot jest zadowolony, że
pogonił gryzonia. To, czy kot jest akurat zainteresowany myszą, jest losowe. Zależy jednak od liczby
przegonionych już myszy. Im jest ich więcej, tym kotu jednak bardziej się chce. Prawdopodobieństwo
zainteresowania wynosi 1 / ( 1+e^(-0.1 * n) ) , gdzie n to liczba dotychczas przegonionych myszy.

Cały dzień trwa kilkaset iteracji, a cała symulacja to jeden dzień. Po zakończeniu symulacji chcemy zobaczyć
wszystkie ścieżki wydeptane w trawie przez koty i myszy.
Pliki z danymi. Za pomocą dowolnego programu (lub ręcznie) należy stworzyć pliki tekstowy, który w
każdej linijce zawiera dwie liczby oddzielone spacją - położenia początkowe x i y jednego zwierzaka. Dane
dla każdego typu zwierząt powinny znaleźć się w osobnym pliku (3 typy kotów + myszy → w sumie 4 pliki).
Położenia powinny być liczbami całkowitymi nieujemnymi, żaden zwierzak nie powinien też znajdować poza
ogrodem. Należy stworzyć po kilka zwierząt każdego typu.
Po zakończeniu symulacji chcemy zobaczyć ścieżki wydeptane przez wszystkie zwierzęta. Jako że każde
zwierzę pamięta wszystkie swoje położenia, wystarczy narysować wykres przedstawiający kolejno połączone
punkty. Można to zrobić używając Matplotlib i polecenia plot.

