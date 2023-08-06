import PySimpleGUI as sg



sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2')],
            [sg.Button('Iniciar'), sg.Button('Cancel')] 
]

# Create the Window
window = sg.Window('Texto da janela', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Iniciar':
        print('Alguma coisa')

window.close()