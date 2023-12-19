from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image,ImageTk

root=Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False,False)


def getWeather():
    city=textfield.get()
    # geolocator=Nominatim(user_agent="geoapiExercises")
    geolocator=Nominatim(user_agent="my_geocoder")
    try:

        location=geolocator.geocode(city)
    except:
        print("location not found")
        return

    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    timezone.config(text=result)

    long_lat.config(text=f"{round(location.latitude,1)}°N,{round(location.longitude,1)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")

    clock.config(text=current_time)

    api="https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&appid=beb2576a33e1c7cb025701e9aa96605a"

    json_data=requests.get(api).json()

    #current_data

    temp=json_data['main']['temp']
    humidity=json_data['main']['humidity']
    pressure=json_data['main']['pressure']
    wind=json_data['wind']['speed']
    description=json_data['weather'][0]['description']

    t.config(text=(temp,"K"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=description)


    api_key="beb2576a33e1c7cb025701e9aa96605a"
    # api_daily="https://api.openweathermap.org/data/2.5/forecast/daily?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&cnt=7&appid="
    # api_daily=f"https://api.openweathermap.org/data/2.5/forecast?lat={location.latitude}&lon={location.longitude}&appid={api_key}"
    # api_daily=f"https://https://api.openweathermap.org/data/3.0/onecall?lat={location.latitude}&lon={location.longitude}&appid={api_key}"
    api_daily=f"https://api.openweathermap.org/data/3.0/onecall?lat={location.latitude}&lon={location.longitude}&appid={api_key}"
    json_data1=requests.get(api_daily).json()
    # print(dict(json_data1))

    # firstcell

    firstdayimage=json_data1['daily'][0]['weather'][0]['icon']
    # print(firstdayimage)
    photo1=ImageTk.PhotoImage(file=f"Images/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1

    tempday1=json_data1['daily'][0]['temp']['day']
    tempnight1=json_data1['daily'][0]['temp']['night']

    day1temp.config(text=f"Day:{tempday1}\n Night:{tempnight1}")



    # secondcell

    seconddayimage = json_data1['daily'][1]['weather'][0]['icon']
    # print(seconddayimage)

    img=(Image.open(f"Images/{seconddayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2

    tempday2 = json_data1['daily'][1]['temp']['day']
    tempnight2 = json_data1['daily'][1]['temp']['night']

    day2temp.config(text=f"Day:{tempday2}\n Night:{tempnight2}")


    # thirdcell

    thirddayimage = json_data1['daily'][2]['weather'][0]['icon']
    # print(thirddayimage)

    img = (Image.open(f"Images/{thirddayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image = photo3

    tempday3 = json_data1['daily'][2]['temp']['day']
    tempnight3 = json_data1['daily'][2]['temp']['night']

    day3temp.config(text=f"Day:{tempday3}\n Night:{tempnight3}")

    # fourthcell

    fourthdayimage = json_data1['daily'][3]['weather'][0]['icon']
    # print(fourthdayimage)

    img = (Image.open(f"Images/{fourthdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image = photo4

    tempday4 = json_data1['daily'][3]['temp']['day']
    tempnight4 = json_data1['daily'][3]['temp']['night']

    day4temp.config(text=f"Day:{tempday4}\n Night:{tempnight4}")

    # fifthcell

    fifthdayimage = json_data1['daily'][4]['weather'][0]['icon']
    # print(fifthdayimage)

    img = (Image.open(f"Images/{fifthdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image = photo5

    tempday5 = json_data1['daily'][4]['temp']['day']
    tempnight5 = json_data1['daily'][4]['temp']['night']
    day5temp.config(text=f"Day:{tempday5}\n Night:{tempnight5}")

    # sixthcell

    sixthdayimage = json_data1['daily'][5]['weather'][0]['icon']
    # print(sixthdayimage)

    img = (Image.open(f"Images/{sixthdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image = photo6

    tempday6 = json_data1['daily'][5]['temp']['day']
    tempnight6 = json_data1['daily'][5]['temp']['night']
    day6temp.config(text=f"Day:{tempday6}\n Night:{tempnight6}")


    # seventhcell

    seventhdayimage = json_data1['daily'][6]['weather'][0]['icon']
    # print(seventhdayimage)

    img = (Image.open(f"Images/{seventhdayimage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image = photo7

    tempday7 = json_data1['daily'][6]['temp']['day']
    tempnight7 = json_data1['daily'][6]['temp']['night']
    day7temp.config(text=f"Day:{tempday7}\n Night:{tempnight7}")

    #days
    first=datetime.now()
    day1.config(text=first.strftime("%A"))

    second=first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first + timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))


#Icon

image_icon=PhotoImage(file="Images/logo.png")
root.iconphoto(False,image_icon)

Round_box=PhotoImage(file="Images/Rounded+Rectangle+1.png")
Label(root,image=Round_box,bg="#57adff").place(x=30,y=110)

#labels

label1 = Label(root,text="Temperature",font=("Helvetica",11),fg="white",bg="#203243")
label1.place(x=50,y=120)

label2 = Label(root,text="Humidity",font=("Helvetica",11),fg="white",bg="#203243")
label2.place(x=50,y=140)

label3 = Label(root,text="Pressure",font=("Helvetica",11),fg="white",bg="#203243")
label3.place(x=50,y=160)

label4 = Label(root,text="Wind Speed",font=("Helvetica",11),fg="white",bg="#203243")
label4.place(x=50,y=180)

label5 = Label(root,text="Description",font=("Helvetica",11),fg="white",bg="#203243")
label5.place(x=50,y=200)

#searchbox

Search_image=PhotoImage(file="Images/Rounded+Rectangle+3.png")
myimage=Label(image=Search_image,bg="#57adff")
myimage.place(x=270,y=120)

weat_image=PhotoImage(file="Images/Layer+7.png")
weather_image=Label(root,image=weat_image,bg="#203243")
weather_image.place(x=290,y=127)

textfield=Entry(root,justify="center",width=15,font=("popins",25,"bold"),bg="#203243",border=0,fg='white')
textfield.place(x=370,y=130)
textfield.focus()

Search_icon = PhotoImage(file="Images/Layer+6.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor='hand2',bg="#203243",command=getWeather)
myimage_icon.place(x=645,y=125)

#bottom_boxes

frame=Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

firstbox=PhotoImage(file="Images/Rounded+Rectangle+2.png")
secondbox=PhotoImage(file="Images/Rounded+Rectangle+2+copy.png")

Label(frame,image=firstbox,bg="#212120").place(x=30,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=300,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=400,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=500,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=600,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=700,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=800,y=30)


#Clock
clock=Label(root,font=('Helvetica',30,'bold'),fg='white',bg="#57adff")
clock.place(x=30,y=20)

#timezone
timezone=Label(root,font=('Helvetica',20),fg="white",bg="#57adff")
timezone.place(x=700,y=20)

long_lat=Label(root,font=('Helvetica',20),fg="white",bg="#57adff")
long_lat.place(x=700,y=50)

t=Label(root,font=('Helvetica',11),fg='white',bg="#203243")
t.place(x=150,y=120)

h=Label(root,font=('Helvetica',11),fg='white',bg="#203243")
h.place(x=150,y=140)

p=Label(root,font=('Helvetica',11),fg='white',bg="#203243")
p.place(x=150,y=160)

w=Label(root,font=('Helvetica',11),fg='white',bg="#203243")
w.place(x=150,y=180)

d=Label(root,font=('Helvetica',11),fg='white',bg="#203243")
d.place(x=150,y=200)

#first cell

firstframe=Frame(root,width=230,height=132,bg='#282829')
firstframe.place(x=35,y=315)

day1 = Label(firstframe,font="arial 15",bg="#282829",fg="#fff")
day1.place(x=100,y=5)

firstimage = Label(firstframe,bg="#282829")
firstimage.place(x=1,y=15)

day1temp = Label(firstframe,bg="#282829", fg="#57adff", font="arial 15 bold")
day1temp.place(x=100,y=50)


#second cell
secondframe=Frame(root,width=70,height=115,bg='#282829')
secondframe.place(x=305,y=325)

day2 = Label(secondframe,bg="#282829",fg="#fff")
day2.place(x=10,y=5)

secondimage = Label(secondframe,bg="#282829")
secondimage.place(x=7,y=20)

day2temp=Label(secondframe,bg="#282829",fg="#57adff")
day2temp.place(x=2,y=70)


#third cell
thirdframe=Frame(root,width=70,height=115,bg='#282829')
thirdframe.place(x=405,y=325)


day3 = Label(thirdframe,bg="#282829",fg="#fff")
day3.place(x=10,y=5)


thirdimage = Label(thirdframe,bg="#282829")
thirdimage.place(x=7,y=20)

day3temp=Label(thirdframe,bg="#282829", fg="#57adff")
day3temp.place(x=2,y=70)

#fourth cell

fourthframe=Frame(root,width=70,height=115,bg='#282829')
fourthframe.place(x=505,y=325)

day4 = Label(fourthframe,bg="#282829",fg="#fff")
day4.place(x=10,y=5)

fourthimage = Label(fourthframe,bg="#282829")
fourthimage.place(x=7,y=20)

day4temp=Label(fourthframe,bg="#282829", fg="#57adff")
day4temp.place(x=2,y=70)

#fifth cell

fifthframe=Frame(root,width=70,height=115,bg='#282829')
fifthframe.place(x=605,y=325)

day5 = Label(fifthframe,bg="#282829",fg="#fff")
day5.place(x=10,y=5)

fifthimage = Label(fifthframe,bg="#282829")
fifthimage.place(x=7,y=20)

day5temp=Label(fifthframe,bg="#282829", fg="#57adff")
day5temp.place(x=2,y=70)
#sixth cell

sixthframe=Frame(root,width=70,height=115,bg='#282829')
sixthframe.place(x=705,y=325)

day6 = Label(sixthframe, bg="#282829",fg="#fff")
day6.place(x=10,y=5)

sixthimage = Label(sixthframe,bg="#282829")
sixthimage.place(x=7,y=20)

day6temp=Label(sixthframe,bg="#282829", fg="#57adff")
day6temp.place(x=2,y=70)


#seventh cell
seventhframe=Frame(root, width=70,height=115,bg='#282829')
seventhframe.place(x=805,y=325)

day7 = Label(seventhframe,bg="#282829",fg="#fff")
day7.place(x=10,y=5)

seventhimage = Label(seventhframe,bg="#282829")
seventhimage.place(x=7,y=20)

day7temp=Label(seventhframe,bg="#282829", fg="#57adff")
day7temp.place(x=2,y=70)

mainloop()