departamentos = {
     'Izabal':{
        '1': 'Puerto Barrios',
        '2': 'Morales',
        '3': 'Los Amates',
        '4': 'Livisntong'
        },
}
for d in departamentos.values():
    for k,v in d.items():
        result[k].append(v)

