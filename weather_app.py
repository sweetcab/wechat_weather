
# coding: utf-8

# In[1]:

import pyowm
import time
from datetime import datetime
import pytz 
from tzlocal import get_localzone 
import itchat
from itchat.content import *


# In[2]:

owm = pyowm.OWM('XXX')  # You MUST provide a valid API key


# In[4]:

def weather_at_city(city,when=0):
    report=""
    # get local timezone    
    local_tz = get_localzone()
    
    if when==0:
        obs_list = owm.weather_at_places(city,'like')
        
        for obs in obs_list:
            #report+=datetime.fromtimestamp(obs.get_reception_time()).strftime('%d-%b-%Y %H:%M:%S')
            l=obs.get_location()
            report+="Now @ "+l.get_name()+", "+l.get_country()+":\n"
            w=obs.get_weather()
            report+=str(w.get_temperature(unit='celsius')['temp_min'])+u"\u00b0"+'C-'
            report+=str(w.get_temperature(unit='celsius')['temp_max'])+u"\u00b0"+'C'
            report+=", "+w.get_detailed_status()
            
    if when==1:
        fc = owm.daily_forecast(city)
        f = fc.get_forecast()
        report+="Today @ "+f.get_location().get_name()+", "+f.get_location().get_country()+":\n"
        lst = f.get_weathers()
        report+=str(lst[0].get_temperature(unit='celsius')['min'])+u"\u00b0"+'C-'
        report+=str(lst[0].get_temperature(unit='celsius')['max'])+u"\u00b0"+'C'
        report+=", "+lst[0].get_detailed_status()
        
    if when==2:
        fc = owm.daily_forecast(city)
        f = fc.get_forecast()
        report+="Tomorrow @ "+f.get_location().get_name()+", "+f.get_location().get_country()+":\n"
        lst = f.get_weathers()
        report+=str(lst[1].get_temperature(unit='celsius')['min'])+u"\u00b0"+'C-'
        report+=str(lst[1].get_temperature(unit='celsius')['max'])+u"\u00b0"+'C'
        report+=", "+lst[1].get_detailed_status()
        
    if when==3:
        fc = owm.daily_forecast(city)
        f = fc.get_forecast()
        lst = f.get_weathers()
        report+="@ "+f.get_location().get_name()+", "+f.get_location().get_country()+":\n"
        report+="Today: "
        report+=str(lst[0].get_temperature(unit='celsius')['min'])+u"\u00b0"+'C-'
        report+=str(lst[0].get_temperature(unit='celsius')['max'])+u"\u00b0"+'C'
        report+=", "+lst[0].get_detailed_status()+"\n"
        report+="Tomorrow: "
        report+=str(lst[1].get_temperature(unit='celsius')['min'])+u"\u00b0"+'C-'
        report+=str(lst[1].get_temperature(unit='celsius')['max'])+u"\u00b0"+'C'
        report+=", "+lst[1].get_detailed_status()+"\n"
        report+="The day after tomorrow  "
        report+=str(lst[2].get_temperature(unit='celsius')['min'])+u"\u00b0"+'C-'
        report+=str(lst[2].get_temperature(unit='celsius')['max'])+u"\u00b0"+'C'
        report+=", "+lst[2].get_detailed_status() 
        
    if when==7:
        fc = owm.daily_forecast(city)
        f = fc.get_forecast()
        lst = f.get_weathers()
        report+="@ "+f.get_location().get_name()+", "+f.get_location().get_country()+":\n"
        for i in range(7):
            report+=datetime.fromtimestamp(lst[i].get_reference_time()).strftime('%d-%b-%Y %a')+": "
            report+=str(lst[i].get_temperature(unit='celsius')['min'])+u"\u00b0"+'C-'
            report+=str(lst[i].get_temperature(unit='celsius')['max'])+u"\u00b0"+'C'
            report+=", "+lst[i].get_detailed_status()+"\n"
            
    if when==10:
        fc = owm.three_hours_forecast(city)
        f = fc.get_forecast()
        lst = f.get_weathers()
        report+="@ "+f.get_location().get_name()+", "+f.get_location().get_country()+":\n"
        for i in range(5):
            report+=datetime.fromtimestamp(lst[i].get_reference_time()).strftime('%d-%b-%Y %H:%M:%S')+": "
            report+=str(lst[i].get_temperature(unit='celsius')['temp_min'])+u"\u00b0"+'C-'
            report+=str(lst[i].get_temperature(unit='celsius')['temp_max'])+u"\u00b0"+'C'
            report+=", "+lst[i].get_detailed_status()+"\n"
    return report


# In[5]:

def weather_look_up(lookup):
    weathermsg=""
    when=-1
    city=""
    lookup_list=lookup.strip().split(" ")
    city=lookup_list[0]
    if len(lookup_list)==1:
        when=0
    else:
        if lookup_list[1].lower()=="now" or lookup_list[1].lower()=="nwo":
            when=0
        elif lookup_list[1].lower()=="today" or lookup_list[1].lower()=="tod" or lookup_list[1].lower()=="tody":
            when=1
        elif lookup_list[1].lower()=="tom" or lookup_list[1].lower()=="tomm" or lookup_list[1].lower()=="tommorow" or lookup_list[1].lower()=="tomorrow" or lookup_list[1].lower()=="tomorow":
            when=2
        elif lookup_list[1].lower()=="days":
            when=3
        elif lookup_list[1].lower()=="week" or lookup_list[1].lower()=="wek":
            when=7
        elif lookup_list[1].lower()=="next" or lookup_list[1].lower()=="nexthours" or lookup_list[1].lower()=="later":
            when=10
        
    if when==-1:
        return "Bad Input"
    
    try:
        weathermsg=weather_at_city(city,when)
    except Exception, e:
        weathermsg=str(e)
    return weathermsg


# In[8]:

@itchat.msg_register(itchat.content.TEXT)
def getweather(msg):
    if msg['ToUserName'] != 'filehelper': return
    weatherresult=weather_look_up(str(msg['Text']))
    itchat.send(weatherresult,'filehelper')
    
if __name__ == '__main__':
    itchat.auto_login(True)
    itchat.run()


