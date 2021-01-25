#----------------------------------------------------------------------------------------
#   Software  que gera codigo aleatorio de mensagem
#   Data de Criacao: 01-2021
#   Autor: Athila Wender de Salles
#----------------------------------------------------------------------------------------


import PySimpleGUI as tela
import random

#----Area de tela e tema-----------------------------------------------------------------

tela.theme('DarkGrey')

informacao=[
        [tela.Radio('Mensagem a ser codificada', 'RADIO1', default=True,key='-COD-')],
        [tela.Radio('Codigo a ser traduzido','RADIO1',default=False,key='-MEM-')],
        [tela.Multiline(size=(50,15),key='-IN-')]
        ]

resultado=[
        [tela.Text('Resultado')],
        [tela.Text(' ')],
        [tela.Multiline(size=(50,15),key='-OUT-')]
        ]

layout =[
        [tela.Column(informacao),tela.VerticalSeparator(),tela.Column(resultado)],
        [tela.Button('Executar'), tela.Button('Limpar'), tela.Button('Sair')]
        ]

janela =  tela.Window('CripTest', layout, icon='virus.ico')


#----Inicio do Software------------------------------------------------------------------

while True:
    event,values = janela.read()

#   termina os eventos para sair

    if event == tela.WIN_CLOSED or event =='Sair':
        break

#   limpa a tela

    if event == 'Limpar':
        janela['-IN-'].update('')
        janela['-OUT-'].update('')

#   captura o texto da caixa de texto

    if event == 'Executar':
        ini= int(100*(random.random()))
        cod=''
        pos =0
        carac=''
        posi=0
        men = {"testo":values['-IN-']}
        men2 =men['testo']
        tam=len(men2)
        if int(ini) <100 and int(ini)>10:
            ini = '0'+str(ini)

        if int(ini)<10:
            ini = '00'+str(ini)


#   executa a codificacao do texto

        if values['-COD-'] == True:

            for c in men2:
                carac =str(ord(men2[pos]))
                carac =int(carac)+int(ini)
                if int(carac)<10:
                    carac = '00'+str(carac)
                if int(carac)<100 and int(carac)>10:
                    carac='0'+str(carac)
                cod=cod+str(carac)
                pos=pos+1
            cod =str(ini) + cod


#   executa a traducao do codigo

        if values['-MEM-']==True:
            for c in men2:
                carac = carac + men2[pos]
                if posi == 2:
                    if pos == 2:
                        ini = int(carac)
                    carac = int(carac)-int(ini)
                    if carac > 0:
                        cod = cod +(chr(int(carac)))
                    carac = ''
                    posi = -1
                posi = posi +1
                pos = pos +1
    

#   manda o resultado para tela   

        janela["-OUT-"].update(cod)

janela.close()

#----Fim do programa---------------------------------------------------------------------
