from gtts import gTTS

from playsound import playsound


text_val = ''' Welcome to my project. This Project is going to introduce me. So, Hello everyone. My name is Shruti vats. 
I am a sophomore at Chandigarh University and pursuing Bachelor's of Engineering in computer science. I like to code 
specially in python and c++ language. I am also into web development and android development and currently learning about them. 
I like changes and try to improve myself everyday. So that's all i want to say about me. Is there anything else you want to know about me? If yes press 1 and n for 2'''
language = 'en'
obj = gTTS(text=text_val, lang=language, slow=False)
obj.save("exam.mp3")
playsound("exam.mp3")
yn = int(input("Enter you choice : "))

ques = '''What would you like to know ?
    1. My date of birth
    2. From where i am 
    3. what is my age
    4. what is my nationality
    5. from where i did my schooling
    Question will be displayed at your screen please select question number accordingly'''
language = 'en'
obj1 = gTTS(text = ques, lang=language, slow=False)
obj1.save("question.mp3")

if yn == 1:
    playsound("question.mp3")
else:
    bye = ''' Thank you. I hope you like this.'''
    b = gTTS(text=bye,lang=language,slow=False)
    b.save("bye1.mp3")
    playsound("bye1.mp3")
    exit()

print('''*** do you want to know ?***
*  1. Date of Birth 
*  2. From where I am  
*  3. My age
*  4. My nationality
*  5. from where i did my schooling''')
choice = int(input("Enter question number(e.g 1 0r 2 0r 3 : "))
choice1= '''I was born on 5th March 2003'''
choice2 = '''I am from Munger,Bihar'''
choice3 = '''I am 18 year old'''
choice4 = '''I am from India'''
choice5 = '''I did my schooling from Kendriya Vidyalaya 3 BRD AFS Chandigarh '''
default = ''' I would suggest you to select from the given question chart.'''

ch1 = gTTS(text=choice1,lang=language,slow=False)
ch1.save("ch1.mp3")

ch2 = gTTS(text=choice2,lang=language,slow=False)
ch2.save("ch2.mp3")

ch3 = gTTS(text=choice3,lang=language,slow=False)
ch3.save("ch3.mp3")

ch4 = gTTS(text=choice4,lang=language,slow=False)
ch4.save("ch4.mp3")

ch5 = gTTS(text=choice5,lang=language,slow=False)
ch5.save("ch5.mp3")

ch6 = gTTS(text=default,lang=language,slow=False)
ch6.save("ch6.mp3")

if choice == 1:
    playsound("ch1.mp3")
elif choice ==2:
    playsound("ch2.mp3")
elif choice ==3:
    playsound("ch3.mp3")
elif choice ==4:
    playsound("ch4.mp3")
elif choice == 5:
    playsound("ch5.mp3")
else:
    playsound("ch6.mp3")

goodbye = '''Now i would like to take permission to end this project. Good bye . I hope you liked this. Thank you.'''

gb = gTTS(text=goodbye,lang=language,slow=False)
gb.save("bye.mp3")
playsound("bye.mp3")