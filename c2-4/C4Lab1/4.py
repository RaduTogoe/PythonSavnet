angajat1 = {
'nume': 'Ana-Maria Popescu',
'departament': 'IT',
'ID': 3409,
'Salar': 4560,
}
angajat2 = {
'nume': 'Marian Muntean',
'departament': 'IT',
'ID': 2235,
'Salar': 4556,
}
angajat3 = {
'nume': 'Maria Manea',
'departament': 'HR',
'ID': 1908,
'Salar': 6755,
}

angajat4 = {
'nume': 'Oana Popa',
'departament': 'HR',
'ID': 1977,
'Salar': 5400,
}
angajat5 = {
'nume': 'David Codru',
'departament': 'Management',
'ID': 1988,
'Salar': 12900,
}

lista_dict = [angajat1, angajat2, angajat3, angajat4, angajat5]

def salariu_greater_5000():
    for i in lista_dict:
        if i['Salar'] > 5000:
            print(f"Nume: {i['nume']}, ID: {i['ID']}, Departament: {i['departament']}")

def where_manager():
    nume = []
    for i in lista_dict:
        if i['departament'] != 'Management':
            nume.append(i['nume'])
    print(nume)

def medie_hr():
    salarii_hr = []
    for i in lista_dict:
        if i['departament'] == 'HR':
            salarii_hr.append(i['Salar'])
    s = sum([i for i in salarii_hr])
    print(s / len(salarii_hr))


salariu_greater_5000()
where_manager()
medie_hr()