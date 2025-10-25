from tkinter import *
from tkinter import ttk

import requests

def data_get():
    city = city_name.get()
    api_key = "fd38be88686c870af628dd4d017cfa27"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    data = requests.get(url).json()
    weather_label1.config(text=data["weather"][0]["main"])
    weatherd_label1.config(text=data["weather"][0]["description"])
    temp1.config(text=str(int(data["main"]["temp"]-273.15)))
    per1.config(text=data["main"]["pressure"])

window = Tk()

# title
window.title("Weather application")
window.config(bg="light blue")
window.geometry("500x500")

# label
name_label = Label(window,text="Live Weather Update App",
                  font=("Calibri",30,"bold") )
name_label.place(x=25,y=50,height=50,width=450)

# combobox
city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(window,text="Live Weather Update App",values=list_name,
                  font=("Calibri",15,"bold"),textvariable= city_name)
com.place(x=50,y=120,height=50,width=400)


# Weather climate
weather_label = Label(window,text="Weather climate",
                  font=("Calibri",15) )
weather_label.place(x=100,y=290,height=25,width=150)
weather_label1 = Label(window,text="  ",
                  font=("Calibri",15) )
weather_label1.place(x=260,y=290,height=25,width=150)

# Weather Discription
weatherd_label = Label(window,text="Weather Discription",
                  font=("Calibri",13) )
weatherd_label.place(x=100,y=325,height=25,width=150)
weatherd_label1 = Label(window,text="",
                  font=("Calibri",13) )
weatherd_label1.place(x=260,y=325,height=25,width=150)

# temperature
temp = Label(window,text="Temperature",
                  font=("Calibri",14) )
temp.place(x=100,y=360,height=25,width=150)
temp1 = Label(window,text="",
                  font=("Calibri",14) )
temp1.place(x=260,y=360,height=25,width=150)

# pressure
per = Label(window,text="Pressure",
                  font=("Calibri",14) )
per.place(x=100,y=395,height=25,width=150)
per1 = Label(window,text="",
                  font=("Calibri",14) )
per1.place(x=260,y=395,height=25,width=150)

#button
show_button = Button(window,text="Show",
                  font=("Calibri",15,"bold"),command=data_get)
show_button.place(x=200,y=190,height=50,width=100)

window.mainloop()