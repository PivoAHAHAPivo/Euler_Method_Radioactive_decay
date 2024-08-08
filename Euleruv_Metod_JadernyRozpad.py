
# Modul 1: Instalace potřebných knihoven přes terminál:

    # Otevřete terminál a postupně zadejte následující příkazy
    # pip install numpy
    # pip install matplotlib
    # pip install mplcursors



# Modul 2: Připojení knihoven pro sestavení kódu

        # Připojení knihovny numpy
import numpy as np                              # Importuje modul numpy a přiřazuje mu přezdívku np (modul určený pro matematické funkce)
        # Připojení knihovny matplotlib
import matplotlib.pyplot as plt                 # Importuje podmodul pyplot z modulu matplotlib a přiřazuje mu přezdívku plt (podmodul určený pro vizualizaci 
                                                #   dat pomocí grafů a jejich vytváření)
        # Připojení knihovny math
import math                                     # Importuje modul math



# Modul 3: Zadávání a kontrola dat

# Podmodul 3.1: Funkce pro zadávání správných dat 

def input_elements(prompt):
    """
    Funkce pro požadování názvů prvků od uživatele, oddělených čárkami.
        Parametry:
    prompt (str): Zpráva pro požadování vstupu.
        Vrací:
    list: Seznam názvů prvků.
    """
    while True:                                                         # Nekonečný cyklus, skončí, když budou splněny podmínky cyklu
        try:                                                            # Blok try, ve kterém bude spuštěn kód
            data = input(prompt).split(',')                             # Požadujeme vstup a rozdělíme řetězce podle čárek
            data = [el.strip() for el in data if el.strip()]            # Odstraníme nadbytečné mezery a prázdné řádky pomocí list comprehension
            if not data:                                                # Zkontrolujeme, zda seznam není prázdný
                raise ValueError("Seznam nemůže být prázdný.")           # Generuje výjimku pomocí příkazu raise a dává jí název ValueError(), pokud je seznam prázdný
            return data                                                 # Vrátí seznam prvků, pokud seznam obsahuje alespoň jednu hodnotu
        except ValueError as e:                                         # Blok Except, ve kterém je výjimce přiřazen přezdívka e. Funguje, pokud v bloku try došlo k vyvolání výjimky.
            print(f"Chyba: {e}. Zkuste to znovu.")                      # Vytiskne zprávu o chybě a znovu požádá o vstup


def input_positive_floats(prompt, count):
    """
    Funkce pro požadování seznamu kladných čísel s plovoucí desetinnou čárkou od uživatele.
        Parametry:
    prompt (str): Zpráva pro požadování vstupu.
    count (int): Očekávaný počet hodnot.
        Vrací:
    list: Seznam kladných čísel s plovoucí desetinnou čárkou.
    """
    while True:
        try:
            data = list(map(float, input(prompt).split(',')))                                           # Převede vstup na seznam (list()) čísel s plovoucí desetinnou čárkou (map(float,))
            if len(data) != count:                                                                      # Zkontroluje počet zadaných hodnot
                raise ValueError(f"Mělo by být zadáno {count} hodnot.")
            if any(x < 0 and x != float('inf') for x in data):                                          # Zkontroluje, zda jsou všechny hodnoty kladné nebo nekonečné any() - funkce
                                                                                                        #   vrací hodnotu True, pokud alespoň jeden prvek je pravdivý,
                                                                                                        #   vrací False, pokud jsou všechny hodnoty nepravdivé.
                raise ValueError("Všechny hodnoty musí být kladná čísla nebo nekonečné.")               # Pokud je podmínka True
            return data                                                                                 # Pokud je podmínka False
        except ValueError as e:
            print(f"Chyba: {e}. Zkuste to znovu.")                                                    


def input_non_negative_integers(prompt, count):
    """
    Funkce pro požadování seznamu nezáporných celých čísel od uživatele.
        Parametry:
    prompt (str): Zpráva pro požadování vstupu.
    count (int): Očekávaný počet hodnot.
        Vrací:
    list: Seznam nezáporných celých čísel.
    """
    while True:
        try:
            data = list(map(int, input(prompt).split(',')))                                         # Převede vstup na seznam celých čísel
            if len(data) != count:                                                                  # Zkontroluje počet zadaných hodnot
                raise ValueError(f"Mělo by být zadáno {count} hodnot.")
            if any(x < 0 for x in data):                                                            # Zkontroluje, zda jsou všechny hodnoty nezáporné
                raise ValueError("Všechny hodnoty musí být nezáporná celá čísla.")
            return data                                                                             # Vrátí seznam hodnot
        except ValueError as e:
            print(f"Chyba: {e}. Zkuste to znovu.")                                                # Vytiskne zprávu o chybě a znovu požádá o vstup


def input_positive_float(prompt):
    """
    Funkce pro požadování kladného čísla s plovoucí desetinnou čárkou od uživatele.
        Parametry:
    prompt (str): Zpráva pro požadování vstupu.
        Vrací:
    float: Kladné číslo s plovoucí desetinnou čárkou.
    """
    while True:
        try:
            data = float(input(prompt))                                                             # Převede vstup na číslo s plovoucí desetinnou čárkou
            if data <= 0 and data == float('inf'):                                                  # Zkontroluje, zda je hodnota kladná, ale ne nekonečná
                raise ValueError("Hodnota musí být kladné číslo nebo nekonečná.")
            return data                                                                             # Vrátí hodnotu
        except ValueError as e:
            print(f"Chyba: {e}. Zkuste to znovu.")                                                # Vytiskne zprávu o chybě a znovu požádá o vstup


# Podmodul 3.2: Funkce pro vytvoření a filtrování slovníku

def create_element_dict(names, half_lives, initial_amounts):
    """
    Funkce pro vytvoření slovníku prvků s jejich parametry.
    Parametry:
    names (list): Seznam názvů prvků.
    half_lives (list): Seznam period poločasu rozpadu pro každý prvek.
    initial_amounts (list): Seznam počátečních množství jader pro každý prvek.
    Vrací:
    dict: Slovník prvků s parametry 'half_life' a 'initial_amount'.
    """
    element_dict = {}                                                       # Vytvoříme prázdný slovník pro uchování prvků
    for i in range(len(names)):                                             # Procházíme všechny prvky v seznamu names, přes podmínku pro i v rozsahu délky seznamu range(len(names))
        element_dict[names[i]] = {                                          # Pro každý klíč ve slovníku se vytváří vnořený slovník 
            'half_life': half_lives[i],                                     # Přidáme období poločasu rozpadu (hodnota) s názvem 'half_life'
            'initial_amount': initial_amounts[i]                            # Přidáme počáteční množství jader (hodnota) s názvem 'initial_amount'
        }
    return element_dict                                                     # Vrátí vyplněný slovník

def filter_elements(element_dict):
    """
    Funkce pro filtrování prvků, přičemž se zohledňuje jejich období poločasu rozpadu.
    Parametry:
    element_dict (dict): Slovník prvků s jejich parametry.
    Vrací:
    dict: Filtrováný slovník prvků.
    """
    filtered_dict = {}                                                              # Vytvoříme prázdný slovník pro uchování filtrováných prvků
    last_amount = 0                                                                 # Proměnná pro uchování množství jader od prvků s nulovým obdobím poločasu rozpadu
    for el, params in element_dict.items():                                         # Procházíme všechny prvky slovníku, kde přípona .items() vrací páry: 
                                                                                    #   klíč (el), hodnota (params).
        half_life = params['half_life']                                             # Přiřadí proměnné half_life hodnotu z vnořeného seznamu s názvem 'half_life'
        if half_life == 0:                                                          # Pokud je období poločasu rozpadu rovno 0
            last_amount += params['initial_amount']                                 # Přidá množství jader (hodnota) k proměnné last_amount
        elif half_life == float('inf'):                                              # Pokud je období poločasu rozpadu nekonečné
            filtered_dict[el] = params                                               # Přidá prvek do filtrováného slovníku
        else:                                                                         # Pokud není období poločasu rozpadu rovno 0 nebo nekonečné
            params['initial_amount'] += last_amount                                  # Přidá proměnné last_amount k počátečnímu množství jader
            filtered_dict[el] = params                                                # Přidá prvek do filtrováného slovníku
            last_amount = 0                                                           # Nastaví proměnné last_amount na 0
    return filtered_dict                                                             # Vrátí slovník s filtrovánými prvky


# Podmodul 3.3: Zadávání dat

# Získání dat od uživatele:

# Vytvoří proměnné element_names a přiřadí jí seznam názvů prvků, který byl ověřen funkcí input_elements
element_names = input_elements("Zadejte názvy prvků (oddělené čárkami): ")

# Vytvoří proměnné half_lives a přiřadí jí seznam období poločasu rozpadu, který byl ověřen funkcí input_positive_floats
half_lives = input_positive_floats("Zadejte období poločasu rozpadu (oddělená čárkami): ", len(element_names))

# Vytvoří proměnné initial_amounts a přiřadí jí seznam počátečních množství jader, který byl ověřen funkcí input_non_negative_integers
initial_amounts = input_non_negative_integers("Zadejte počáteční množství jader (oddělené čárkami): ", len(element_names))

# Vytvoří proměnné time_experiment a přiřadí jí hodnotu, která byla ověřena funkcí input_positive_float
time_experiment = input_positive_float("Zadejte dobu experimentu (v letech): ")

# Vytvoří proměnné time_step a přiřadí jí hodnotu, která byla ověřena funkcí input_positive_float
time_step = input_positive_float("Zadejte krok (v letech): ")

# Vytvoří slovník prvků pomocí funkce create_element_dict a přiřadí ho proměnné element_dict
element_dict = create_element_dict(element_names, half_lives, initial_amounts)

# Filtrování slovníku pomocí funkce filter_elements a přiřazení výsledku proměnné filtered_dict
filtered_dict = filter_elements(element_dict)
# Tyto operace byly provedeny pro zjednodušení a správnou funkčnost programu. Všechny následující funkce a operace jsou určeny pro filtrováný slovník prvků.

print(filtered_dict)

# Modul 4: Výpočet dat metodou Euler

# Podmodul 4.1: Funkce pro výpočet systému diferenciálních rovnic metodou Euler

def calculate_decay_constants(filtered_dict):
    """
    Funkce pro výpočet rozpadových konstant pro každý prvek.
    Parametry:
    filtered_dict (dict): Slovník prvků s jejich parametry.
    Vrátí:
    dict: Slovník s rozpadovými konstantami pro každý prvek.
    """
    decay_constants = {}                                        # Vytvoříme prázdný slovník pro ukládání rozpadových konstant
    for element, params in filtered_dict.items():               
        half_life = params['half_life']                         
        if half_life == float('inf'):                           # Pokud je prvek stabilní (období poločasu rozpadu je nekonečné)
            decay_constants[element] = 0                        # Rozpadová konstanta je 0
        else:                                                   # Pokud má prvek reálnou hodnotu období rozpadu
            decay_constants[element] = np.log(2) / half_life    # Vypočítáme rozpadovou konstantu podle vzorce
    return decay_constants                                      # Vrátíme slovník s rozpadovými konstantami, kde klíč je název prvku a hodnota je rozpadová konstanta.
                                                                #   Vrátit slovník decay_constants je třeba pro další krok

def euler_method_divided(filtered_dict, time_experiment, time_step):
    """
    Funkce pro výpočet rozpadu prvků metodou Euler.
    Parametry:
    filtered_dict (dict): Slovník prvků s jejich parametry.
    time_experiment (float): Celkový čas experimentu.
    time_step (float): Krok času pro metodu Euler.
    Vrátí:
    dict: Slovník s poli množství jader pro každý prvek na každém časovém kroku.
    """
    decay_constants = calculate_decay_constants(filtered_dict)                                      # Přiřadíme slovníku jméno decay_constants, spočítáme a uložíme hodnoty 
                                                                                                    #   pomocí funkce calculate_decay_constants
    elements = list(filtered_dict.keys())                                                           # Přiřadíme seznamu názvů prvků, získaných klíči slovníku (.keys()), jméno elements
                                                                                                    #   a převedeme je na seznam pomocí funkce list()
    num_elements = len(elements)                                                                    # Počet prvků je rovný délce seznamu prvků
    num_steps = math.ceil(time_experiment / time_step) + 1                                          # Počet časových kroků. Spočítá se zaokrouhlením času experimentu 
                                                                                                    #   děleného krokem času plus jedna. Přidaný krok je potřeba pro počáteční hodnoty.
    element_arrays = {el: np.zeros(num_steps) for el in elements}                                   # Vytvoříme slovník, kde pole pro uchovávání množství jader na každém kroku
                                                                                                    #   jsou hodnoty s klíči. Pole obsahují nuly (np.zeros())
                                                                                                    #   s počtem buněk num_steps 
    for el in elements:                                                     # Inicializujeme počáteční množství jader.
        element_arrays[el][0] = filtered_dict[el]['initial_amount']         # Přiřadíme první buňce každého pole ze slovníku polí počáteční hodnotu jader z 
                                                                            #   filtrovaného slovníku parametrů pro každý prvek
    for i in range(num_steps - 1):                                                  # Procházíme každý časový krok. Kroků je o jeden méně, protože vypočítané hodnoty budou
                                                                                    #   přiřazovány do polí, první buňka je již obsazena počátečními hodnotami.
        current_values = {el: element_arrays[el][i] for el in elements}             # Vytvoříme slovník, kde hodnoty každého klíče jsou hodnoty z pole element_arrays na pozici i
        first_element = elements[0]                                                 # Přiřadíme proměnné first_element první prvek ze seznamu elements
        rates = {first_element: -decay_constants[first_element] * current_values[first_element]}        # Vytvoříme slovník pro rychlosti rozpadu.
                                                                                                        #   Vypočítáme rychlost změny pro první prvek.
        for j in range(1, num_elements - 1):                                # Procházíme všechny prvky kromě prvního a posledního
            el = elements[j]                                                # Přiřadíme proměnné el j-tý prvek ze seznamu elements
            prev_element = elements[j - 1]                                  # Přiřadíme proměnné prev_element (j-1)-ý prvek ze seznamu elements
            
            rates[el] = decay_constants[prev_element] * current_values[prev_element] - decay_constants[el] * current_values[el]  # Vypočítáme rychlost změny pro aktuální prvek.
                                                                                                                                 # Uložíme rychlost rozpadu do slovníku.
        last_element = elements[-1]                                                         # Přiřadíme proměnné last_element poslední prvek ze seznamu elements
        rates[last_element] = decay_constants[elements[-2]] * current_values[elements[-2]]  # Vypočítáme rychlost změny pro poslední prvek
        
        for el in elements:                                                                         # Aktualizujeme množství jader pro všechny prvky na dalším kroku
            element_arrays[el][i + 1] = current_values[el] + time_step * rates.get(el, 0)           
                        # element_arrays[el][i + 1] — množství jader prvku el na následujícím časovém kroku (krok i + 1) v poli element_arrays.
                        # current_values[el] — aktuální množství jader prvku el na současném kroku i.
                        # time_step — časový krok, na který se přechází.
                        # rates.get(el, 0) — rychlost změny množství jader prvku el. Metoda .get(el, 0) se používá pro získání hodnoty ze slovníku rates s klíčem el.
    
    return element_arrays       # Vrátíme slovník s poli množství jader pro každý prvek


# Podmodul 4.2: Řešení metodou Euler

element_arrays_whole = euler_method_divided(filtered_dict, time_experiment, time_step)      # Přiřadí proměnné element_arrays_whole slovník, kde hodnoty jsou pole dat.
    # Příprava dat pro grafy
num_steps = math.ceil(time_experiment / time_step) + 1                                      # Přiřadí proměnné num_steps hodnotu zaokrouhlených kroků plus jedna
times = np.arange(0, num_steps * time_step, time_step)                                      # Přiřadí proměnné times pole, kde začátek je 0, konec num_steps * time_step,
                                                                                            #   a kde každá buňka má hodnotu o time_step větší než předchozí
current_amounts = {el: element_arrays_whole[el] for el in filtered_dict}                    # Přiřadí proměnné current_amount slovník, kde klíč je název prvku,
                                                                                            #   a hodnota jsou pole spočítaných dat. Tento krok je potřebný pro zobrazení hodnot a klíčů.



# Modul 5: Zobrazení grafů 

# Podmodul 5.1: Funkce pro zobrazení grafů

def find_maxima(y, t):
    """
    Funkce pro nalezení maxim v datech.
    Parametry:
    y (list): Seznam hodnot (počet atomů).
    t (list): Seznam času.
    Vrací:
    list: Seznam dvojic (čas, hodnota) pro všechna maxima.
    """
    maxima = []                                         # Vytvoříme prázdný seznam pro uchování maxim
    for i in range(1, len(y) - 1):                      # Projdeme všechny hodnoty, kromě první a poslední
        if y[i - 1] < y[i] > y[i + 1]:                  # Zkontrolujeme podmínku maxima
            maxima.append((t[i], y[i]))                 # Přidáme maximum do seznamu
    return maxima                                       # Vrátíme seznam maxim

def plot_graph(ax, x, y, label, title, color='blue'):
    """
    Funkce pro zobrazení grafu jednoho prvku.
    Parametry:
    ax (matplotlib.axes.Axes): Osa pro vykreslení grafu.
    x (list): Seznam hodnot času.
    y (list): Seznam hodnot počtu atomů.
    label (str): Štítek pro graf.
    title (str): Název grafu.
    color (str, optional): Barva grafu. Defaultně 'blue'.
    """
    ax.clear()                                              # Vyčistíme osu před vykreslením grafu
    ax.plot(x, y, label=label, color=color)                 # Vykreslíme graf
    ax.set_xlabel('Čas (roky)')                             # Nastavíme popis osy X
    ax.set_ylabel('Počet atomů')                            # Nastavíme popis osy Y
    ax.set_title(title)                                     # Nastavíme název grafu
    ax.legend()                                             # Přidáme legendu
    ax.axhline(np.mean(y), color='r', linestyle='--', label='Průměrná hodnota')  # Přidáme vodorovnou čáru průměrné hodnoty
    ax.legend()                                             # Aktualizujeme legendu
    maxima = find_maxima(y, x)                              # Najdeme maxima
    for t, value in maxima:                                 # Projdeme všechna maxima
        ax.plot(t, value, 'ro')                             # Zobrazíme maxima červenými body
    plt.draw()                                              # Aktualizujeme graf

def plot_combined_graph(ax, x, y_dict, title):
    """
    Funkce pro zobrazení kombinovaného grafu pro všechny prvky.
    Parametry:
    ax (matplotlib.axes.Axes): Osa pro vykreslení grafu.
    x (list): Seznam hodnot času.
    y_dict (dict): Slovník s daty pro každý prvek (hodnoty a barva).
    title (str): Název grafu.
    """
    ax.clear()                                              # Vyčistíme osu před vykreslením grafu
    for label, (y, color) in y_dict.items():                # Projdeme všechny prvky ve slovníku
        ax.plot(x, y, label=label, color=color)             # Vykreslíme graf pro každý prvek
    ax.set_xlabel('Čas (roky)')                             # Nastavíme popis osy X
    ax.set_ylabel('Počet atomů')                            # Nastavíme popis osy Y
    ax.set_title(title)                                     # Nastavíme název grafu
    ax.legend()                                             # Přidáme legendu
    plt.draw()                                              # Aktualizujeme graf

def create_single_element_plot(ax, times, current_amounts, element, color):
    """
    Funkce pro vytvoření grafu jednoho prvku.
    Parametry:
    ax (matplotlib.axes.Axes): Osa pro vykreslení grafu.
    times (list): Seznam hodnot času.
    current_amounts (dict): Slovník s počtem atomů pro každý prvek.
    element (str): Název prvku pro vykreslení grafu.
    color (str): Barva grafu.
    """
    title = f'Změna počtu atomů {element}'                                # Vytvoříme název grafu
    plot_graph(ax, times, current_amounts[element], element, title, color)          # Vykreslíme graf pro jeden prvek

def create_combined_plot(ax, times, current_amounts, colors, element_names):
    """
    Funkce pro vytvoření kombinovaného grafu pro všechny prvky.
    Parametry:
    ax (matplotlib.axes.Axes): Osa pro vykreslení grafu.
    times (list): Seznam hodnot času.
    current_amounts (dict): Slovník s počtem atomů pro každý prvek.
    colors (list): Seznam barev pro každý prvek.
    element_names (list): Seznam názvů prvků.
    """
    y_dict = {element: (current_amounts[element], color) for element, color in zip(filtered_dict, colors[:len(element_names)])}     # Vytvoříme slovník dat pro každý prvek
    plot_combined_graph(ax, times, y_dict, 'Změna počtu atomů všech prvků')                                            # Vykreslíme kombinovaný graf pro všechny prvky


# Podmodul 5.2: Příprava figury pro zobrazení grafů

colors = ['blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'red', 'yellow', 'black', 'violet']  # Barvy pro grafy
fig, ax = plt.subplots()  # Vytvoříme figuru a osu pro vykreslení grafů

def create_plot_functions(times, current_amounts, element_names, colors):
    """
    Vytvoří seznam funkcí pro zobrazení grafů.
    Parametry:
    times (list): Seznam hodnot času.
    current_amounts (dict): Slovník s počtem atomů pro každý prvek.
    element_names (list): Seznam názvů prvků.
    colors (list): Seznam barev pro grafy prvků.
    Vrací:
    list: Seznam funkcí pro zobrazení grafů.
    """
    plot_functions = []  # Vytvoříme prázdný seznam pro uchování funkcí
    
    for element, color in zip(filtered_dict, colors[:len(element_names)]):      # Vytvoříme funkci pro každý prvek a přidáme ji do seznamu funkcí
        def single_element_plot(ax=ax, times=times, current_amounts=current_amounts, element=element, color=color):
            create_single_element_plot(ax, times, current_amounts, element, color)
        plot_functions.append(single_element_plot)                              # Přidáme funkci zobrazení jednoho prvku do seznamu
    
    def combined_plot(ax=ax, times=times, current_amounts=current_amounts, element_names=element_names, colors=colors): # Vytvoříme funkci pro kombinovaný graf všech prvků
        create_combined_plot(ax, times, current_amounts, colors, element_names)
    plot_functions.append(combined_plot)                                        # Přidáme funkci kombinovaného grafu do seznamu
    return plot_functions                                                       # Vrátíme seznam funkcí

plot_functions = create_plot_functions(times, current_amounts, element_names, colors)   # Získáme seznam funkcí pro zobrazení grafů

def on_click(event):
    """
    Zpracovává dvojité kliknutí myši pro přepnutí grafů.
    Parametry:
    event (matplotlib.backend_bases.Event): Událost kliknutí myši.
    """
    global current_index
    if event.dblclick:                                                  # Zkontrolujeme, zda bylo dvojité kliknutí
        current_index = (current_index + 1) % len(plot_functions)       # Přepneme na další graf
        plot_functions[current_index](ax)                               # Zobrazíme vybraný graf

def on_key(event):
    """
    Zpracovává stisknutí mezerníku pro zavření grafu.
    Parametry:
    event (matplotlib.backend_bases.Event): Událost stisknutí klávesy.
    """
    if event.key == ' ':    # Zkontrolujeme, zda byla stisknuta mezerník
        plt.close()         # Zavřeme graf

fig.canvas.mpl_connect('button_press_event', on_click)  # Připojíme obsluhu kliknutí myši
fig.canvas.mpl_connect('key_press_event', on_key)  # Připojíme obsluhu stisknutí kláves

current_index = 0                   # Začínáme s prvním grafem
plot_functions[current_index](ax)   # Zobrazíme první graf
plt.show()                          # Ukážeme graf

