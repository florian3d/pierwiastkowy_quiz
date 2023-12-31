import random, tkinter, tkinter.font, tkinter.messagebox

class Element:
    def __init__(self, e) -> None:
        self.name = e['name']
        self.number = e['number']
        self.symbol = e['symbol']

periodic_table_full = [{'name': 'wodór', 'symbol': 'H', 'number': '1'}, {'name': 'hel', 'symbol': 'He', 'number': '2'}, {'name': 'lit', 'symbol': 'Li', 'number': '3'}, {'name': 'beryl', 'symbol': 'Be', 'number': '4'}, {'name': 'bor', 'symbol': 'B', 'number': '5'}, {'name': 'węgiel', 'symbol': 'C', 'number': '6'}, {'name': 'azot', 'symbol': 'N', 'number': '7'}, {'name': 'tlen', 'symbol': 'O', 'number': '8'}, {'name': 'fluor', 'symbol': 'F', 'number': '9'}, {'name': 'neon', 'symbol': 'Ne', 'number': '10'}, {'name': 'sód', 'symbol': 'Na', 'number': '11'}, {'name': 'magnez', 'symbol': 'Mg', 'number': '12'}, {'name': 'glin', 'symbol': 'Al', 'number': '13'}, {'name': 'krzem', 'symbol': 'Si', 'number': '14'}, {'name': 'fosfor', 'symbol': 'P', 'number': '15'}, {'name': 'siarka', 'symbol': 'S', 'number': '16'}, {'name': 'chlor', 'symbol': 'Cl', 'number': '17'}, {'name': 'argon', 'symbol': 'Ar', 'number': '18'}, {'name': 'potas', 'symbol': 'K', 'number': '19'}, {'name': 'wapń', 'symbol': 'Ca', 'number': '20'}, {'name': 'skand', 'symbol': 'Sc', 'number': '21'}, {'name': 'tytan', 'symbol': 'Ti', 'number': '22'}, {'name': 'wanad', 'symbol': 'V', 'number': '23'}, {'name': 'chrom', 'symbol': 'Cr', 'number': '24'}, {'name': 'mangan', 'symbol': 'Mn', 'number': '25'}, {'name': 'żelazo', 'symbol': 'Fe', 'number': '26'}, {'name': 'kobalt', 'symbol': 'Co', 'number': '27'}, {'name': 'nikiel', 'symbol': 'Ni', 'number': '28'}, {'name': 'miedź', 'symbol': 'Cu', 'number': '29'}, {'name': 'cynk', 'symbol': 'Zn', 'number': '30'}, {'name': 'gal', 'symbol': 'Ga', 'number': '31'}, {'name': 'german', 'symbol': 'Ge', 'number': '32'}, {'name': 'arsen', 'symbol': 'As', 'number': '33'}, {'name': 'selen', 'symbol': 'Se', 'number': '34'}, {'name': 'brom', 'symbol': 'Br', 'number': '35'}, {'name': 'krypton', 'symbol': 'Kr', 'number': '36'}, {'name': 'rubid', 'symbol': 'Rb', 'number': '37'}, {'name': 'stront', 'symbol': 'Sr', 'number': '38'}, {'name': 'itr', 'symbol': 'Y', 'number': '39'}, {'name': 'cyrkon', 'symbol': 'Zr', 'number': '40'}, {'name': 'niob', 'symbol': 'Nb', 'number': '41'}, {'name': 'molibden', 'symbol': 'Mo', 'number': '42'}, {'name': 'technet', 'symbol': 'Tc', 'number': '43'}, {'name': 'ruten', 'symbol': 'Ru', 'number': '44'}, {'name': 'rod', 'symbol': 'Rh', 'number': '45'}, {'name': 'pallad', 'symbol': 'Pd', 'number': '46'}, {'name': 'srebro', 'symbol': 'Ag', 'number': '47'}, {'name': 'kadm', 'symbol': 'Cd', 'number': '48'}, {'name': 'ind', 'symbol': 'In', 'number': '49'}, {'name': 'cyna', 'symbol': 'Sn', 'number': '50'}, {'name': 'antymon', 'symbol': 'Sb', 'number': '51'}, {'name': 'tellur', 'symbol': 'Te', 'number': '52'}, {'name': 'jod', 'symbol': 'I', 'number': '53'}, {'name': 'ksenon', 'symbol': 'Xe', 'number': '54'}, {'name': 'cez', 'symbol': 'Cs', 'number': '55'}, {'name': 'bar', 'symbol': 'Ba', 'number': '56'}, {'name': 'lantan', 'symbol': 'La', 'number': '57'}, {'name': 'cer', 'symbol': 'Ce', 'number': '58'}, {'name': 'prazeodym', 'symbol': 'Pr', 'number': '59'}, {'name': 'neodym', 'symbol': 'Nd', 'number': '60'}, {'name': 'promet', 'symbol': 'Pm', 'number': '61'}, {'name': 'samar', 'symbol': 'Sm', 'number': '62'}, {'name': 'europ', 'symbol': 'Eu', 'number': '63'}, {'name': 'gadolin', 'symbol': 'Gd', 'number': '64'}, {'name': 'terb', 'symbol': 'Tb', 'number': '65'}, {'name': 'dysproz', 'symbol': 'Dy', 'number': '66'}, {'name': 'holm', 'symbol': 'Ho', 'number': '67'}, {'name': 'erb', 'symbol': 'Er', 'number': '68'}, {'name': 'tul', 'symbol': 'Tm', 'number': '69'}, {'name': 'iterb', 'symbol': 'Yb', 'number': '70'}, {'name': 'lutet', 'symbol': 'Lu', 'number': '71'}, {'name': 'hafn', 'symbol': 'Hf', 'number': '72'}, {'name': 'tantal', 'symbol': 'Ta', 'number': '73'}, {'name': 'wolfram', 'symbol': 'W', 'number': '74'}, {'name': 'ren', 'symbol': 'Re', 'number': '75'}, {'name': 'osm', 'symbol': 'Os', 'number': '76'}, {'name': 'iryd', 'symbol': 'Ir', 'number': '77'}, {'name': 'platyna', 'symbol': 'Pt', 'number': '78'}, {'name': 'złoto', 'symbol': 'Au', 'number': '79'}, {'name': 'rtęć', 'symbol': 'Hg', 'number': '80'}, {'name': 'tal', 'symbol': 'Tl', 'number': '81'}, {'name': 'ołów', 'symbol': 'Pb', 'number': '82'}, {'name': 'bizmut', 'symbol': 'Bi', 'number': '83'}, {'name': 'polon', 'symbol': 'Po', 'number': '84'}, {'name': 'astat', 'symbol': 'At', 'number': '85'}, {'name': 'radon', 'symbol': 'Rn', 'number': '86'}, {'name': 'frans', 'symbol': 'Fr', 'number': '87'}, {'name': 'rad', 'symbol': 'Ra', 'number': '88'}, {'name': 'aktyn', 'symbol': 'Ac', 'number': '89'}, {'name': 'tor', 'symbol': 'Th', 'number': '90'}, {'name': 'protaktyn', 'symbol': 'Pa', 'number': '91'}, {'name': 'uran', 'symbol': 'U', 'number': '92'}, {'name': 'neptun', 'symbol': 'Np', 'number': '93'}, {'name': 'pluton', 'symbol': 'Pu', 'number': '94'}, {'name': 'ameryk', 'symbol': 'Am', 'number': '95'}, {'name': 'kiur', 'symbol': 'Cm', 'number': '96'}, {'name': 'berkel', 'symbol': 'Bk', 'number': '97'}, {'name': 'kaliforn', 'symbol': 'Cf', 'number': '98'}, {'name': 'einstein', 'symbol': 'Es', 'number': '99'}, {'name': 'ferm', 'symbol': 'Fm', 'number': '100'}, {'name': 'mendelew', 'symbol': 'Md', 'number': '101'}, {'name': 'nobel', 'symbol': 'No', 'number': '102'}, {'name': 'lorens', 'symbol': 'Lr', 'number': '103'}, {'name': 'rutherford', 'symbol': 'Rf', 'number': '104'}, {'name': 'dubn', 'symbol': 'Db', 'number': '105'}, {'name': 'seaborg', 'symbol': 'Sg', 'number': '106'}, {'name': 'bohr', 'symbol': 'Bh', 'number': '107'}, {'name': 'has', 'symbol': 'Hs', 'number': '108'}, {'name': 'meitner', 'symbol': 'Mt', 'number': '109'}, {'name': 'darmsztadt', 'symbol': 'Ds', 'number': '110'}, {'name': 'roentgen', 'symbol': 'Rg', 'number': '111'}, {'name': 'kopernik', 'symbol': 'Cn', 'number': '112'}, {'name': 'nihon', 'symbol': 'Nh', 'number': '113'}, {'name': 'flerow', 'symbol': 'Fl', 'number': '114'}, {'name': 'moskow', 'symbol': 'Mc', 'number': '115'}, {'name': 'liwermor', 'symbol': 'Lv', 'number': '116'}, {'name': 'tenes', 'symbol': 'Ts', 'number': '117'}, {'name': 'oganeson', 'symbol': 'Og', 'number': '118'}]
elements = [Element(e) for e in periodic_table_full]
gen, _r_, ans = [], 0, None
correct = 0
iterations = 25
loop = 1
title = 'Pierwiastkowy quiz'
font_family = 'Consolas'
answer_time = 3
timeout_answer = answer_time
game_time = iterations*5
timeout_game = game_time
answer_timer_enabled = False
game_timer_enabled = False
gtid = -1

def reset():
    global loop, correct, timeout_game
    loop = 1
    correct = 0
    timeout_game = game_time

def set_values():
    global answer_timer_enabled, game_timer_enabled
    lbl_symbol['text'] = ans.symbol
    lbl_symbol_number['text'] = ans.number
    for i, b in enumerate(buttons):
        b['text'] = gen[i].name
        b['state'] = 'normal'
        b['fg'] = 'blue'
        labels[i]['text'] = ''
        labels[i]['fg'] = 'green'
    answer.set(-1)
    answer_timer_enabled = False
    lbl_timer_answer['text'] = str(0)
    lbl_timer_game['text'] = str(timeout_game)

def start_game():
    global game_timer_enabled, gtid
    reset()
    randomize()
    tkinter.messagebox.showinfo(title, f'Zaczynamy, masz {iterations} prób.')
    set_values()
    game_timer_enabled = True
    window.after_cancel(gtid)
    gtid = window.after(1000, game_timer)

def answer_timer():
    global timeout_answer
    if timeout_answer > 0 and answer_timer_enabled:
        timeout_answer -= 1
        lbl_timer_answer['text'] = str(timeout_answer)
        window.after(1000, answer_timer)

def game_timer():
    global timeout_game, game_timer_enabled, gtid
    if game_timer_enabled:
        timeout_game -= 1
        lbl_timer_game['text'] = str(timeout_game)
        if timeout_game < 1:
            game_timer_enabled = False
            game_over()
    window.after_cancel(gtid)
    gtid = window.after(1000, game_timer)

def evaluate_game():
    global loop, game_timer_enabled
    loop += 1
    if loop > iterations:
        game_over()
    else:
        randomize()
        set_values()
        lbl_loop['text'] = f'próba {loop} z {iterations}'
        game_timer_enabled = True

def game_over():
    again = tkinter.messagebox.askquestion(title, 'Koniec gry.\nUdało ci się odgadnąć {round((correct/iterations)*100, 2)}% pierwiastków\nChcesz zagrać jeszcze raz?')
    if again == 'yes':
        start_game()    
    else:
        window.destroy()
    
def chosen():
    global correct, answer_timer_enabled, timeout_answer, game_timer_enabled
    _ch = answer.get()
    if _r_ == _ch:
        correct += 1
        lbl_points['text'] = f'punktacja: {correct}'
    for i, b in enumerate(buttons):
        b['state'] = 'disabled'
        if answer.get() == i and i != _r_:
            labels[i]['text'] = 'ŹLE'
            labels[i]['fg'] = 'red'
        if i == _r_:
            labels[i]['text'] = 'DOBRZE'
    answer_timer_enabled = True
    game_timer_enabled = False
    timeout_answer = answer_time
    lbl_timer_answer['text'] = str(timeout_answer)
    window.after(1000, answer_timer)
    window.after(timeout_answer*1000, evaluate_game)
    
def randomize():
    global gen, _r_, ans
    rnd = []
    _l = len(elements)-1
    while len(set(rnd)) != 4:
        rnd = [random.randint(0, _l) for _ in range(4)]
    gen = [elements[i] for i in rnd]
    _r_ = random.randint(0, 3)
    ans = gen[_r_]

def quit_app(event):
    window.destroy()

window = tkinter.Tk()
window.geometry("360x520")
window.resizable(False, False)
window.title(title)
window.bind('Q', quit_app)

font_element = tkinter.font.Font(window, size=80, family=font_family)
font_element_small = tkinter.font.Font(window, size=16, family=font_family)
font_button = tkinter.font.Font(window, size=18, family=font_family)
font_timer = tkinter.font.Font(window, size=12, family=font_family)
font_info = tkinter.font.Font(window, size=20, family=font_family)
font_correct = tkinter.font.Font(window, size=14, family=font_family)


lbl_symbol = tkinter.Label(window, padx=4, pady=4, font=font_element, text='#')
lbl_symbol_number = tkinter.Label(window, padx=4, pady=4, font=font_element_small, text='#')

answer = tkinter.IntVar()
buttons = [tkinter.Radiobutton(window, text='________', variable=answer, value=i, command=chosen, font=font_button, fg='blue', state='disabled') for i in range(4)]
labels = [tkinter.Label(window, justify='center', padx=5, pady=5, font=font_correct, text='', fg='green') for i in range(4)]
lbl_points = tkinter.Label(window, justify='center', padx=10, pady=15, font=font_info, text='punktacja: 0', fg='red')
lbl_loop = tkinter.Label(window, justify='center', padx=10, pady=0, font=font_info, text=f'próba 1 z {iterations}')
lbl_timer_answer = tkinter.Label(window, justify='center', padx=10, pady=0, font=font_timer, text=f'{timeout_answer}')
lbl_timer_game = tkinter.Label(window, justify='center', padx=10, pady=0, font=font_timer, text=f'{timeout_game}')

lbl_symbol.grid(row=0, column=0, padx=5, pady=5, sticky='ne')
lbl_symbol_number.grid(row=0, column=1, padx=5, pady=5, sticky='nw')
for i, b in enumerate(buttons):
    b.grid(row=i+1, column=0, padx=20, pady=5, sticky='nsw')
    labels[i].grid(row=i+1, column=1, padx=5, pady=5, sticky='nsw')
lbl_points.grid(row=5, column=0, padx=5, pady=5, sticky='nsw')
lbl_loop.grid(row=6, column=0, padx=5, pady=5, sticky='nsw')
lbl_timer_game.grid(row=7, column=0, padx=5, pady=5, sticky='nsw')
lbl_timer_answer.grid(row=7, column=1, padx=5, pady=5, sticky='nsw')

for i in range(8):
    window.rowconfigure(i, weight=0)
for i in range(2):
    window.columnconfigure(i, weight=0)

answer.set(-1)
window.after(0, start_game)
window.mainloop()
