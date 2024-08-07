
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


    
    # Modul 3: Vstup počtu jader radioaktivních látek

    # Podmodul 3.1: Funkce pro zpracování zadaných dat
def get_valid_input(prompt):
    """
    Funkce pro získání platného kladného celého čísla od uživatele.
    Parametry:
    prompt (str): Zpráva pro požadavek na vstup.
    Vrací:
    int: Platné celé kladné číslo.
    """
    while True:                                                     # Nekonečný cyklus, který se nezastaví, dokud nebude dosaženo správné podmínky
        value = input(prompt)                                       # Vytvoří proměnné value, která je rovna zadané proměnné prompt
        if value.isdigit():                                         # Kontrola, zda vstup obsahuje pouze číslice
            value = int(value)                                      # Přiřadí proměnné value typ integer, pokud podmínka value.isdigit() je True
            if value > 0:                                           # Kontrola, zda zadané číslo je větší než nula
                return value                                        # Vrátí hodnotu, pokud podmínka value > 0 je True
            elif value == 0:                                        # Kontrola, zda zadané číslo je rovno nule
                return 0                                            # Vrátí 0, pokud podmínka value > 0 je False a podmínka value == 0 je True
        print("Zadejte celé kladné číslo.")                         # Zpráva o chybě zadání, pokud podmínka value.isdigit() je False

    # Podmodul 3.2: Vstup hodnot pro každý prvek
elements = ["N_U_238", "N_Th_234", "N_Pa_234", "N_U_234", "N_Th_230",       # Definuje seznam, ve kterém každá buňka obsahuje název proměnné pro zadaná data
            "N_Ra_226", "N_Rn_222", "N_Po_218", "N_Pb_214", "N_Bi_214", 
            "N_Po_214", "N_Pb_210", "N_Bi_210", "N_Po_210", "N_Pb_206"]

nuclei_counts = {}                          # Vytvoří slovník s názvem nuclei_counts
for element in elements:                                                                    # Podmínka cyklu, pro každý prvek ze seznamu elements
    nuclei_counts[element] = get_valid_input(f"Zadejte počet jader pro {element}: ")        # Přes funkci get_valid_input přidá zadanou hodnotu pod klíč, 
                                                                                            #   odpovídající názvu prvku
    


# Modul 4: Poločasy přeměny a výpočet rozpadových konstant radioaktivních prvků

    # Seznam prvků s jejich poločasy přeměny v letech a typy přeměny
elements = [                                    # Vytvoří nový seznam elements, kde každá položka obsahuje data
    ("U_238", 10000, "Alfa rozpad"),
    ("Th_234", 1500, "Beta-minus rozpad"),
    ("Pa_234", 3000, "Beta-minus rozpad"),
    ("U_234", 1200, "Alfa rozpad"),
    ("Th_230", 2200, "Alfa rozpad"),
    ("Ra_226", 4500, "Alfa rozpad"),
    ("Rn_222", 1600, "Alfa rozpad"),
    ("Po_218", 2700, "Alfa rozpad"),
    ("Pb_214", 5500, "Beta-minus rozpad"),
    ("Bi_214", 3400, "Beta-minus rozpad"),
    ("Po_214", 1200, "Alfa rozpad"),
    ("Pb_210", 3300, "Beta-minus rozpad"),
    ("Bi_210", 2400, "Beta-minus rozpad"),
    ("Po_210", 1100, "Alfa rozpad"),
    ("Pb_206", float('inf'), "Stabilní prvek")  # Olovo-206 je stabilní prvek
]
decay_constants = {}        # Slovník pro ukládání poločasů přeměny a rozpadových konstant                                

    # Podmodul 4.1: Výpočet rozpadových konstant
for element, hl, decay_type in elements:            # Podmínka cyklu, pro každý element, hl, decay_type pro každou položku v seznamu elements
    if hl > 0:                                      # Podmínka if, pokud hl > 0
        decay_constants[element] = np.log(2) / hl   # Výpočet rozpadové konstanty pod klíčem, pokud je podmínka pravdivá
    else:
        decay_constants[element] = 0

    # Podmodul 4.2: Výstup vypočítaných hodnot
for element, hl, decay_type in elements:
    dc = decay_constants[element]                   # Přiřadí proměnné dc hodnotu ze slovníku podle klíče názvu prvku
    print(f"{element}: poločas přeměny = {hl} let, rozpadová konstanta = {dc:.5e} 1/rok ({decay_type})")       # Výstup do terminálu

    # Modul 5: Řešení systému diferenciálních rovnic prvního řádu metodou Eulera a výpočet počtu alfa a beta částic

    # Definice proměnných rozpadových konstant pro použití v modulu 5
decay_constants = {el: dc for el, dc in decay_constants.items()}        # Vytvoří kopii slovníku a vrátí páry (klíč, hodnota) pomocí slovníkového vyjádření 
                                                                        #   (dict comprehension). Slovník má stejné klíče a hodnoty, pouze dostupné pro výpočty dále.

    # Podmodul 5.1: Zadejte počáteční podmínky
alpha_particles = 0  # Počáteční počet alfa-částic
beta_particles = 0   # Počáteční počet beta-částic

    # Podmodul 5.2: Funkce pro získání platného celého kladného čísla od uživatele
def get_valid_input_2(prompt_2):
    """
    Funkce pro získání platného celého kladného čísla od uživatele.
    Parametry:
    prompt_2 (str): Zpráva pro požadavek na vstup.
    Vrací:
    int: Platné celé kladné číslo.
    """
    while True:                                             # Nekonečný cyklus, který se nezastaví, dokud nebude dosaženo správné podmínky 
        value_2 = input(prompt_2)                           # Vytvoří proměnné value_2, která je rovna zadané proměnné prompt_2
        if value_2.isdigit() and int(value_2) > 0:          # Smíšená podmínka, která kontroluje, zda zadaná hodnota obsahuje pouze číslice a zda je větší než nula
            return int(value_2)                             # Vrátí hodnotu typu integer, pokud je podmínka pravdivá
        else:
            print("Zadejte celé kladné číslo.")             # Zpráva o chybě zadání, pokud podmínka není splněna

    # Podmodul 5.3: Zadejte hodnotu času simulace a krok pro metodu Eulera
while True:                                                                     # Nekonečný cyklus, který se nezastaví, dokud nebude dosaženo správné podmínky
    T = get_valid_input_2("Čas simulace T v letech: ")                          # Vstup času simulace
    h = get_valid_input_2("Délka kroku h v letech pro metodu Eulera: ")         # Vstup délky kroku
    if T / h >= 10:                                                             # Kontrola, aby bylo množství kroků dostatečně velké
        print(f"T: {T}, h: {h}")                                                # Výstup zadaných hodnot, pokud je podmínka splněna
        break                                                                   # Ukončení cyklu 
    else:
        print("Zadejte hodnoty, jejichž poměr bude větší než 10.")              # Zpráva o chybě zadání, pokud podmínka není splněna

N = T / h                                                   # Výpočet počtu kroků pro metodu Eulera
steps = int(round(N))                                       # Zaokrouhlení počtu kroků na celé číslo
print(f"Počet kroků pro metodu Eulera N = {N}")             # Výstup počtu kroků

    # Podmodul 5.4: Vytvoření polí pro ukládání dat
time = np.zeros(steps + 1)                                          # Pole pro ukládání času
elements = ['U_238', 'Th_234', 'Pa_234', 'U_234', 'Th_230', 'Ra_226', 'Rn_222', 'Po_218', 'Pb_214', 'Bi_214', 'Po_214', 'Pb_210', 'Bi_210', 'Po_210', 'Pb_206']
                                                                    # Nový seznam elements
element_arrays = {el: np.zeros(steps + 1) for el in elements}       # Pole pro každý prvek je nastavena v novém slovníku element_arrays podle klíče
alpha_arr = np.zeros(steps + 1)                                     # Pole pro alfa-částice
beta_arr = np.zeros(steps + 1)                                      # Pole pro beta-částice

    # Podmodul 5.5: Inicializace polí počátečními podmínkami
    # Inicializace polí počátečními podmínkami
time[0] = 0                             # Počáteční podmínka 0. Cyklus pro každou buňku pole, kde další buňka má hodnotu předchozí plus krok h.
for i in range(steps):
    time[i + 1] = time[i] + h

for el in elements:                                         # Cyklus pro každý prvek v seznamu elements. Kde se kontroluje přítomnost prvku podle klíče a 
    key = f"N_{el}"                                         #   vytvoří pole, kde první buňka má zadanou hodnotu.
    if key in nuclei_counts:
        element_arrays[el][0] = nuclei_counts[key]

alpha_arr[0] = alpha_particles                              # Vytvoří pole pro alfa-částice a přiřadí počáteční hodnotu do první buňky
beta_arr[0] = beta_particles

    # Podmodul 5.6: Metoda Eulera pro výpočet dat a aktualizaci hodnot
for i in range(steps):                                                          # Cyklus pro každé i v rozsahu steps, protože první buňka je vyhrazena pro počáteční hodnotu
    current_values = {el: element_arrays[el][i] for el in elements}             # Pomocí slovníku, kde hodnoty jsou pole dat. Aktuální hodnoty pro každý prvek (klíč).

    rates = {       # Výpočet rychlostí rozpadu pro každý prvek pomocí seznamu rates
        'U_238': -decay_constants["U_238"] * current_values['U_238'],
        'Th_234': decay_constants["U_238"] * current_values['U_238'] - decay_constants["Th_234"] * current_values['Th_234'],
        'Pa_234': decay_constants["Th_234"] * current_values['Th_234'] - decay_constants["Pa_234"] * current_values['Pa_234'],
        'U_234': decay_constants["Pa_234"] * current_values['Pa_234'] - decay_constants["U_234"] * current_values['U_234'],
        'Th_230': decay_constants["U_234"] * current_values['U_234'] - decay_constants["Th_230"] * current_values['Th_230'],
        'Ra_226': decay_constants["Th_230"] * current_values['Th_230'] - decay_constants["Ra_226"] * current_values['Ra_226'],
        'Rn_222': decay_constants["Ra_226"] * current_values['Ra_226'] - decay_constants["Rn_222"] * current_values['Rn_222'],
        'Po_218': decay_constants["Rn_222"] * current_values['Rn_222'] - decay_constants["Po_218"] * current_values['Po_218'],
        'Pb_214': decay_constants["Po_218"] * current_values['Po_218'] - decay_constants["Pb_214"] * current_values['Pb_214'],
        'Bi_214': decay_constants["Pb_214"] * current_values['Pb_214'] - decay_constants["Bi_214"] * current_values['Bi_214'],
        'Po_214': decay_constants["Bi_214"] * current_values['Bi_214'] - decay_constants["Po_214"] * current_values['Po_214'],
        'Pb_210': decay_constants["Po_214"] * current_values['Po_214'] - decay_constants["Pb_210"] * current_values['Pb_210'],
        'Bi_210': decay_constants["Pb_210"] * current_values['Pb_210'] - decay_constants["Bi_210"] * current_values['Bi_210'],
        'Po_210': decay_constants["Bi_210"] * current_values['Bi_210'] - decay_constants["Po_210"] * current_values['Po_210'],
        'Pb_206': decay_constants["Po_210"] * current_values['Po_210'] - decay_constants["Pb_206"] * current_values['Pb_206']
    }

    for el in elements:                                                          # Cyklus pro každý prvek v seznamu elements.
        element_arrays[el][i + 1] = (element_arrays[el][i] + rates[el] * h)      # Aktualizace polí pro každý prvek na základě počáteční hodnoty plus změna rychlosti vynásobená krokem

    alpha_arr[i + 1] = alpha_arr[i] + h * (
        decay_constants["U_238"] * current_values['U_238'] + 
        decay_constants["U_234"] * current_values['U_234'] +
        decay_constants["Th_230"] * current_values['Th_230'] +
        decay_constants["Ra_226"] * current_values['Ra_226'] +
        decay_constants["Rn_222"] * current_values['Rn_222'] +
        decay_constants["Po_218"] * current_values['Po_218'] +
        decay_constants["Po_214"] * current_values['Po_214'] +
        decay_constants["Po_210"] * current_values['Po_210']
    )    # Aktualizace počtu alfa-částic
    beta_arr[i + 1] = beta_arr[i] + h * (
        decay_constants["Th_234"] * current_values['Th_234'] +
        decay_constants["Pa_234"] * current_values['Pa_234'] +
        decay_constants["Pb_214"] * current_values['Pb_214'] +
        decay_constants["Bi_214"] * current_values['Bi_214'] +
        decay_constants["Pb_210"] * current_values['Pb_210'] +
        decay_constants["Bi_210"] * current_values['Bi_210']
    )    # Aktualizace počtu beta-částic

    # Podmodul 5.7: Výstup konečných dat
print("Konečné množství jader prvků po čase T:")
for el in elements:
    print(f"{el}: {element_arrays[el][-1]:.2f}")                # Výstup poslední hodnoty pro každý prvek.

print(f"Konečný počet alfa-částic: {alpha_arr[-1]:.2f}")       # Výstup konečného počtu alfa- a beta-částic
print(f"Konečný počet beta-částic: {beta_arr[-1]:.2f}")



# Modul 6: Zavedení zobrazení grafů

    # Podmodul 6.1: Zavedení funkce pro nalezení maxima grafu
def find_maxima(y, t):                              # Definuje funkci find_maxima s argumenty y, t
    """
    Funkce pro nalezení lokálního maxima grafu funkce
    Parametry:
    y[i](float): hodnota v buňce pole aktuálních hodnot počtu jader každé látky
    t[i](float): hodnota v buňce pole aktuálního času
    Vrátí: 
    maxima[(t[i], y[i])](list): seznam s dvojicí hodnot
    """ 
    maxima = []                                     # Vytváří pole s názvem maxima
    for i in range(1, len(y) - 1):                  # Smyčka for pro každý i v rozsahu od 1 do předposledního, aby nedošlo k překročení hranic pole
        if y[i - 1] < y[i] > y[i + 1]:              # Podmínka if, která určuje lokální maximum na grafu
            maxima.append((t[i], y[i]))             # Přidává do seznamu maxima dvojici (t[i], y[i]), kde t[i] je čas a y[i] je počet jader, pokud podmínka
                                                    #   if y[i - 1] < y[i] > y[i + 1]: je pravdivá
    return maxima                                   # Vrací proměnnou se hodnotou maxima a ukončuje smyčku

    # Zavedení funkcí pro zobrazení grafu  
def plot_graph(ax, x, y, label, title, color = 'blue'):
    """
    Funkce pro vykreslení grafu na jednom plátně
    Parametry:
    ax: představuje oblast, kde bude graf vykreslen. Objekt os na kterém bude graf vykreslen z knihovny Matplotlib.
    x: pole hodnot na ose x představující čas
    y: pole hodnot na ose y představující počet atomů
    label: štítek pro graf používaný v legendě
    title: název grafu
    color: barva čáry grafu, ve výchozím nastavení modrá
    Vrátí:
    plt.draw(): aktualizuje a zobrazuje graf
    """
    ax.clear()                                                  # Vyčistí osy před vykreslením nového grafu
    ax.plot(x, y, label = label, color = color)                 # Vykresluje graf podle dat z polí x a y s štítkem label
    ax.set_xlabel('Čas (roky)')                                # Nastavuje popis osy x s názvem Čas (roky)
    ax.set_ylabel('Počet atomů')                               # Nastavuje popis osy y s názvem Počet atomů
    ax.set_title(title)                                        # Nastavuje název pro každý graf
    ax.legend()                                                # Zobrazuje legendu na grafu
    ax.axhline(np.mean(y), color='r', linestyle='--', label='Průměrná hodnota')
                                                                # Nastavuje průměrnou čáru. Přidává horizontální čáru na úrovni průměrné hodnoty y, červené barvy s 
                                                                #   přerušovanou čárou a štítkem Průměrná hodnota.
    ax.legend()                                                # Aktualizuje legendu a přidává štítek průměrné čáry
    maxima = find_maxima(y, x)                                 # Zavádí proměnnou maxima a přiřazuje jí hodnotu funkce find_maxima(y, x)
    for t, value in maxima:                                    # Smyčka for pro hodnoty t, value v proměnné maxima (hrubě porovnává hodnoty)
        ax.plot(t, value, 'ro')                                # Zobrazuje na grafu jako červené tečky všechna lokální maxima
    plt.draw()                                                 # Zobrazuje graf na obrazovce
                    # Proměnná ax je potřebná pro propojení všech funkcí, aby přepínání grafů fungovalo správně a bylo spojeno s osami grafu. Jedno plátno, jiné osy.

    # Zavedení funkce pro zobrazení několika grafů
def plot_combined_graph(ax, x, y_dict, title):
    """
    Funkce pro vykreslení grafů na jednom plátně
    Parametry:
    ax: představuje oblast, kde bude graf vykreslen. Objekt os na kterém bude graf vykreslen z knihovny Matplotlib.
    x: pole hodnot na ose x představující čas
    y_dict: slovník s klíči a hodnotami pro zpracování
    title: název grafu
    Vrátí:
    plt.draw(): aktualizuje a zobrazuje grafy
    """
    ax.clear()                                          # Vyčistí osy před vykreslením nového grafu
    for label, (y, color) in y_dict.items():            # Smyčka for pro každý label, (y, color) ze slovníku y_dict. y_dict.items() vrací páry (klíč, hodnota) ze slovníku y_dict.
                                                        #   Kde label je klíč a (y, color) je hodnota.
        ax.plot(x, y, label=label, color=color)         # Vykresluje grafy podle dat z polí x a y s štítky label a barvami color
    ax.set_xlabel('Čas (roky)')                        # Nastavuje popis osy x s názvem Čas (roky)
    ax.set_ylabel('Počet atomů')                       # Nastavuje popis osy y s názvem Počet atomů
    ax.set_title(title)                                # Nastavuje název pro graf
    ax.legend()                                        # Zobrazuje legendu na grafu
    plt.draw()                                         # Aktualizuje plátno

figs = [                                                                                                        # Zavedení seznamu grafů        
    lambda ax: plot_graph(ax, time, element_arrays['U_238'], 'U-238', 'Rozpad U-238', color='blue'),
    lambda ax: plot_graph(ax, time, element_arrays['Th_234'], 'Th-234', 'Rozpad Th-234', color='green'),
    lambda ax: plot_graph(ax, time, element_arrays['Pa_234'], 'Pa-234', 'Rozpad Pa-234', color='orange'),
    lambda ax: plot_graph(ax, time, element_arrays['U_234'], 'U-234', 'Rozpad U-234', color='purple'),
    lambda ax: plot_graph(ax, time, element_arrays['Th_230'], 'Th-230', 'Rozpad Th-230', color='cyan'),
    lambda ax: plot_graph(ax, time, element_arrays['Ra_226'], 'Ra-226', 'Rozpad Ra-226', color='magenta'),
    lambda ax: plot_graph(ax, time, element_arrays['Rn_222'], 'Rn-222', 'Rozpad Rn-222', color='yellow'),
    lambda ax: plot_graph(ax, time, element_arrays['Po_218'], 'Po-218', 'Rozpad Po-218', color='brown'),
    lambda ax: plot_graph(ax, time, element_arrays['Pb_214'], 'Pb-214', 'Rozpad Pb-214', color='pink'),
    lambda ax: plot_graph(ax, time, element_arrays['Bi_214'], 'Bi-214', 'Rozpad Bi-214', color='gray'),
    lambda ax: plot_graph(ax, time, element_arrays['Po_214'], 'Po-214', 'Rozpad Po-214', color='black'),
    lambda ax: plot_graph(ax, time, element_arrays['Pb_210'], 'Pb-210', 'Rozpad Pb-210', color='red'),
    lambda ax: plot_graph(ax, time, element_arrays['Bi_210'], 'Bi-210', 'Rozpad Bi-210', color='darkblue'),
    lambda ax: plot_graph(ax, time, element_arrays['Po_210'], 'Po-210', 'Rozpad Po-210', color='darkgreen'),
    lambda ax: plot_graph(ax, time, element_arrays['Pb_206'], 'Pb-206', 'Rozpad Pb-206', color='darkorange'),
    lambda ax: plot_graph(ax, time, alpha_arr, 'Alfa částice', 'Počet alfa částic', color='purple'),
    lambda ax: plot_graph(ax, time, beta_arr, 'Beta částice', 'Počet beta částic', color='cyan'),
    lambda ax: plot_combined_graph(ax, time, {
        'U-238': (element_arrays['U_238'], 'blue'),
        'Th-234': (element_arrays['Th_234'], 'green'),
        'Pa-234': (element_arrays['Pa_234'], 'orange'),
        'U-234': (element_arrays['U_234'], 'purple'),
        'Th-230': (element_arrays['Th_230'], 'cyan'),
        'Ra-226': (element_arrays['Ra_226'], 'magenta'),
        'Rn-222': (element_arrays['Rn_222'], 'yellow'),
        'Po-218': (element_arrays['Po_218'], 'brown'),
        'Pb-214': (element_arrays['Pb_214'], 'pink'),
        'Bi-214': (element_arrays['Bi_214'], 'gray'),
        'Po-214': (element_arrays['Po_214'], 'black'),
        'Pb-210': (element_arrays['Pb_210'], 'red'),
        'Bi-210': (element_arrays['Bi_210'], 'darkblue'),
        'Po-210': (element_arrays['Po_210'], 'darkgreen'),
        'Pb-206': (element_arrays['Pb_206'], 'darkorange'),
        'Alfa částice': (alpha_arr, 'purple'),
        'Beta částice': (beta_arr, 'cyan'),
    }, 'Všechny prvky')
]



# Modul 7: Interaktivní funkce grafů

    # Podmodul 7.1: Funkce pro změnu zobrazeného grafu
def on_click(event):
    """
    Funkce pro přepínání grafů dvojitým kliknutím myši
    Parametry:
    event: událost kliknutí myši, která přenáší informace o místě kliknutí
    """
    global current_plot                                  # Odkazuje na proměnnou current_plot, která mění aktuální graf
    if event.dblclick:                                  # Podmínka if kontroluje, zda došlo k dvojitému kliknutí
        current_plot = (current_plot + 1) % len(figs)   # Mění hodnotu proměnné current_plot na 1 a počítá zbytek po dělení délkou seznamu figs
        figs[current_plot](ax)                         # Volá aktuální funkci grafu ze seznamu figs pro vykreslení
        plt.draw()                                      # Aktualizuje graf s novým grafem

def on_key(event):
    """
    Funkce pro zavření grafu při stisknutí klávesy mezerníku
    Parametry:
    event: událost stisknutí klávesy, která přenáší informace o stisknuté klávese
    """
    if event.key == ' ':                                        # Podmínka if kontroluje, zda byla stisknuta klávesa mezerníku (key == ' ')
        plt.close()                                             # Příkaz k zavření grafu


current_plot = 0                                                # Inicializace proměnné current_plot s hodnotou 0
fig, ax = plt.subplots()                                        # Vytvoří figurku a osy pro graf
fig.canvas.mpl_connect('button_press_event', on_click)          # Spojuje událost kliknutí myši s funkcí on_click
fig.canvas.mpl_connect('key_press_event', on_key)               # Spojuje událost kliknutí Space s funkcí on_key
fig.suptitle('Rozpad radioaktivních prvků')                     # Nastavuje název pro celou figurku
fig.tight_layout()                                              # Automaticky nastavuje parametry grafu pro lepší vizualizaci
figs[current_plot](ax)                                          # Volá aktuální funkci grafu
plt.show()                                                      # Zobrazuje graf



