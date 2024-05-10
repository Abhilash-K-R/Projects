
import requests
print("\t\tWelcome to the weather forecaster !\n\n")
print("just enter the city you want the weather report for and click on the button ! its that simple! \n\n")
city_name = input("Enter the name of the city : ")
print("\n\n")
def Gen_report(city):
    url = "https://wttr.in/{}".format(city)
    try:
        data = requests.get(url)
        weather_report = data.text
    except:
        weather_report = "Error Occurred"
    print(weather_report)

Gen_report(city_name)



import requests
print("\t\tWelcome to the weather forecaster !\n\n")
print("just enter the city you want the weather report for and click on the button ! its that simple! \n\n")
city_name = input("Enter the name of the city : ")
print("\n\n")
def Gen_report(city):
    url = "https://wttr.in/{}".format(city)
    try:
        data = requests.get(url)
        weather_report = data.text
    except:
        weather_report = "Error Occurred"
    print(weather_report)

Gen_report(city_name)
