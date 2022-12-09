


# import module

import PySimpleGUI as sg

# valja tema
sg.theme('DarkAmber')

# skapa en layout
layout = [
            [sg.Text('Enter somenting:'), sg.Input(k='-IN-')],
            [sg.Text('Out output vill go here', size=(30, 1), k='-OUT-')],
            [sg.Button('OK'), sg.Button('Exit')]
]

# Skapa fönster 
window = sg.Window('Title', layout)

# Event-loop

while True:
    event, values = window.read()

    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    window['-OUT-'].update(values['-IN-'])

# Stänga fönster
window.close()
exit()