 
import keyboard, time

message = input('inserisci messaggio : ')
number = input('inserisci quantita : ')
delay = float(input('inserisci delay : '))

print('clicca nella casella di testo e quando sei pronto premi Enter')
keyboard.wait('enter')

for i in range(int(number)):
    keyboard.write(message)
    keyboard.press('enter')
    time.sleep(delay)

