import random as r
import math
import matplotlib.pyplot as plt

garten_size = 100
# rozmiar ogrodu / prefer min 100
iterations = 200
# liczba iteracji symulacji
paths = ['animals_data/mouses.txt', 'animals_data/lazy_cats.txt', 
         'animals_data/normal_cats.txt', 'animals_data/baby_cats.txt']
# sciezki plikow z danymi 

class Animal:
    def __init__(self, x, y, name): 
        self.positions = [(x, y)]
        self.name = name

    def add_position(self, x, y):
        self.positions.append((x, y))

    def current_position(self):
        return self.positions[-1]

class Mouse(Animal):
    '''
    poruszanie sie: move()
    ---------------------------------------------------------
    zmieniaja pozycje X i/lub Y o 1 lub zostaja w miejscu.
    wyjatkiem jest ucieczka. wtedy mysz sie teleportuje do schronienia.
    jezeli znajdzie sie w odleglosci mniejszej niz 4 od kota, to nastepuje ich spotkanie
    '''
    def move(self):
      while(True):
        move = [self.positions[-1][0] + r.randint(-1, 1),
                self.positions[-1][1] + r.randint(-1, 1)]
        # this array has two numbers. X value and Y value. 
        # created by adding random int value <-1; 1> to the previous position 
         
        if (move[0] <= garten_size and move[0] >= 0 and move[1] <= garten_size and move[1] >= 0): 
            return move
        
class LazyCat(Animal):
    '''
    poruszanie sie: move()
    ---------------------------------------------------------
    poruszaja sie maks o 10 w X i/lub Y

    gdy dochodzi do spotkania: spotkanie()
    ---------------------------------------------------------
    gdy spotkaja mysz nic sobie nie robia, ale czasem traca mysz lapa, a ona tepa sie do kryjowki.
    to czy kot jest zainteresowany mysza jest losowe, a prawdopodobienstwo tego wynosi
    1 / ( 1+e^(-0.1n) ) , gdzie n to liczba dotychczas przegonionych myszy.
    '''
    def __init__(self, x, y, nazwa):
            super().__init__(x, y, nazwa)
            self.mouses_counter = 0 #licznik przegonionych myszy

    def move(self):
        while(True):
            move = [self.positions[-1][0] + r.randint(-10, 10),
                self.positions[-1][1] + r.randint(-10, 10)]
            if (move[0] <= garten_size and move[0] >= 0 and move[1] <= garten_size and move[1] >= 0): 
                return move
    
    def confrontation(self):
        rand = r.random()
        chance = 1 / (1 + (math.exp(-0.1 * self.mouses_counter)))
        # rand - losowa liczba float z zakresu <0; 1>. chance - liczba z zakresu <0.5; 1) obliczana ze wzoru wyzej.
        # jesli liczba ra jest mniejsza lub rowna liczbie chance to wtedy kot jest zainteresowany mysza
        if(rand <= chance):   
            self.mouses_counter =+ 1
            return True
        return False

class NormalCat(Animal):
    '''
    poruszanie sie: move()
    ---------------------------------------------------------
    poruszaja sie maks o 10 w X i/lub Y

    gdy dochodzi do spotkania: spotkanie()
    ---------------------------------------------------------
    traca mysz lapa. ta teleportuje sie do domu
    '''
    def move(self):
        while(True):
            move = [self.positions[-1][0] + r.randint(-10, 10),
                self.positions[-1][1] + r.randint(-10, 10)]
            if (move[0] <= garten_size and move[0] >= 0 and move[1] <= garten_size and move[1] >= 0): break

        return move
    
    def confrontation(self):
        return True

class BabyCat(Animal):
    '''
    poruszanie sie: move()
    ---------------------------------------------------------
    male koty poruszaja sie max o 5 w X i/lub Y. 
    i nie oddalaja sie od domu o wiecej niz 100.

    gdy dochodzi do spotkania: spotkanie()
    ---------------------------------------------------------
    koty sie boja i sie teleportuja do domu. 
    ale jesli mysz jest blisko ich pudelka (do 50) 
    to wtedy mysz sie teleportuje do domu
    '''
    def move(self):
        while(True):
            move = [self.positions[-1][0] + r.randint(-5, 5),
                self.positions[-1][1] + r.randint(-5, 5)]
            if (move[0] <= garten_size and move[0] >= 0 and move[1] <= garten_size and move[1] >= 0): 
                return move
    
    def confrontation(self):
        distance_from_home = math.sqrt((self.current_position()[0] - self.positions[0][0]) ** 2 +
                                        (self.current_position()[1] - self.positions[0][1]) ** 2)
       
        if distance_from_home < 50:
            return True
        
        self.add_position(self.positions[0][0], self.positions[0][1])
        return False
    
def get_animals(file_path, type):
    animals = []
    file = open(file_path, "r")

    for line in file:
        cords_text = line.split(" ")
        x = int(cords_text[0])
        y = int(cords_text[1])
        if(type == 'mouse'):
            animals.append(Mouse(x, y, 'mouse'))
        elif(type == 'lazycat'):
            animals.append(LazyCat(x, y, 'cat'))
        elif(type == 'normalcat'):
            animals.append(NormalCat(x, y, 'cat'))
        elif(type == 'babycat'):
            animals.append(BabyCat(x, y, 'cat'))

    file.close()
    return animals

animals = get_animals(paths[0], 'mouse') + get_animals(paths[1], 'lazycat') + get_animals(paths[2], 'normalcat') + get_animals(paths[3], 'babycat')

def drow(ax, animals):
    for animal in animals:
        marker = 'r' if animal.name == 'cat' else 'b'
        cords_x, cords_y = zip(*animal.positions)
        home_xy = animal.positions[0][0], animal.positions[0][1]
        ax.plot(home_xy[0], home_xy[1], 'o:'+marker)
        ax.plot(cords_x, cords_y, marker)
        
    plt.show()

def simulation(animals, iterations):
    for _ in range(iterations):
        for animal in animals:
            move = animal.move()
            animal.add_position(move[0], move[1])

            # ten kod sprawdza: dla kazdej myszy czy w poblizu jest kot
            if(animal.name == 'mouse'):
                for enemy in animals:
                    if(enemy.name == 'cat'):
                        distance = math.sqrt((animal.current_position()[0] - enemy.current_position()[0]) ** 2 +
                                        (animal.current_position()[1] - enemy.current_position()[1]) ** 2)
                        if distance < 4:
                            if enemy.confrontation():
                                animal.add_position(animal.positions[0][0], animal.positions[0][1])
       
simulation(animals, iterations)
drow(plt, animals)