# This code is an example for a tutorial on Ubuntu Unity/Gnome AppIndicators:
# http://candidtim.github.io/appindicator/2014/09/13/ubuntu-appindicator-step-by-step.html

import os
import signal
import json
import gi
from datetime import datetime

from urllib.request import Request, urlopen
from urllib.error import URLError

gi.require_version("Gtk", "3.0")
gi.require_version('Notify', '0.7')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify


APPINDICATOR_ID = 'myappindicator'

def getFormattedDateTime(datestr):
  p_datestr_format = ''.join(datestr.rsplit(":", 1))
  date_object = datetime.strptime(p_datestr_format, '%Y-%m-%dT%H:%M:%S%z')
  return date_object.strftime("%H:%M %A, %d %B %Y ")





def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('icon1.png'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    

    gtk.main()


def build_menu():
    menu = gtk.Menu()

    item_weather = gtk.MenuItem('See Weather')
    item_weather.connect('activate', weather)
    menu.append(item_weather)
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

def fetch_wth():
    request = Request('http://api.icndb.com/jokes/random?limitTo=[nerdy]')
    file1 = open("data.json")
    data = json.load(file1)
    unit = "Metric"
    metric_tag = "false"

    current_weather=data[0]["WeatherText"]
    current_temp=data[0]["Temperature"][unit]
    wind_speed=data[0]["Wind"]["Speed"][unit]
    date_w_format = getFormattedDateTime(data[0]["LocalObservationDateTime"])
    city=data[1]["city"]
    country=data[1]["country"]
    print(f"Current Location :{city} {country}")
    print(f"Local observation time: {date_w_format}")
    print(f"Current weather status: {current_weather}")
    print(f"Current temperature: {current_temp['Value']} {current_temp['Unit']}")
    print(f"Wind speed: {wind_speed['Value']} {wind_speed['Unit']}")

    summary = city +", "+country 
    body = "\n" + date_w_format+"\n"+"current weather Satus : "+current_weather +"\n"+ "Current temperature : "+str(current_temp['Value'])+" "+current_temp['Unit']+"\n"+"Wind Speed: "+ str(wind_speed['Value'])+" "+wind_speed['Unit']
    return summary,body
def weather(_):
    summary , body=fetch_wth()
    notification = notify.Notification.new(
        summary,
        body, 
        icon=os.path.abspath('icon2.png')# Optional    
    )

    # Actually show on screen
    notification.show()
def quit(_):
    notify.uninit()
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
