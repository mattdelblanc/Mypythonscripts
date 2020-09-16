data = {'gk': ['David De Gea', 'Sergio Romero', 'Dean Henderson'], 'mid': ['Bruno Fernandes', 'Paul Pogba', 'Nemanja Matic', 'Fred', 'Scott Mactiminay'], 'def': ['Harry Maguire', 'Victor Lindelof', 'Aaron Wan Bissaka', 'Luke Shaw', 'Eric Bailey', 'Phil Jones'], 'fwd': ['Anthony Martial', 'Marcus Rashford', 'Mason Greenwood', 'Odion Ighalo'], 'mgr': ['Ole Gunner Solskjær', 'Micheal Carrick'], 'ceo': ['Ed Woodword'], 'own': ['Glazers']}

for item in data.items():
    print(item[0])
    for players in item[1]:
        print(players)