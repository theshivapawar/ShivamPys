def list_names(first_names, last_names):
    return [f'{first_names[i]} {last_names[i]}' for i in range(len(first_names))]

first_names = ['Shiva', 'Satyam']
last_names = ['Pawar', 'Prajapati']
print(list_names(first_names, last_names))