from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse, JsonResponse
from .forms import ServerSettingsForm
import os
import subprocess
# Create your views here.

@login_required
def home(request):
    
    session = request.POST.get('session')
    day = request.POST.get('day')
    time_scale = request.POST.get('time_scale')
    start_time = request.POST.get('start_time')
    duration = request.POST.get('duration')

    sessionR = request.POST.get('sessionR')
    dayR = request.POST.get('dayR')
    time_scaleR = request.POST.get('time_scaleR')
    start_timeR = request.POST.get('start_timeR')
    durationR = request.POST.get('durationR')
    #server setting

    
    serverName = request.POST.get('serverName')
    adminPassword = request.POST.get('adminPassword')
    spectatorPassword = request.POST.get('spectatorPassword')
    TR = request.POST.get('TR')
    SA = request.POST.get('SA')
    RC = request.POST.get('RC')
    formationLapType = request.POST.get('formationLapType')

    track = request.POST.get('track')

    #Weather
    amTemp = request.POST.get('amTemp')
    trTemp = request.POST.get('trTemp')
    cCover = request.POST.get('cCover')
    rLevel = request.POST.get('rLevel')
    wRandom = request.POST.get('wRandom')

    #format value
    if cCover is not None:
        cCover = int(cCover) / 100

    if rLevel is not None:
        rLevel = int(rLevel) / 100
    

    if request.method == 'POST':

        #terminated accServer.exe
        #terminateServer()
        terminate_process2()

        #setting .json file
        settings_dict = {
            "serverName": serverName,
            "adminPassword": adminPassword,
            "password": "",
            "spectatorPassword": spectatorPassword,
            "centralEntryListPath": "",
            "carGroup": "FreeForAll",
            "trackMedalsRequirement": int(TR),
            "safetyRatingRequirement": int(SA),
            "racecraftRatingRequirement": int(RC),
            "maxCarSlots": "20",
            "isRaceLocked": "1",
            "isLockedPrepPhase": "0",
            "shortFormationLap": "1",
            "dumpLeaderboards": "0",
            "dumpEntryList": "0",
            "randomizeTrackWhenEmpty": "0",
            "allowAutoDQ": "0",
            "ignorePrematureDisconnects": 0,
            "formationLapType": int(formationLapType),
            "configVersion": 1
        }

        ## event .json file
        event_dict={
            "ambientTemp": int(amTemp),
            "cloudLevel": float(cCover),
            "configVersion": 1,
            "isFixedConditionQualification": 1,
            "postQualySeconds": "80",
            "postRaceSeconds": "60",
            "preRaceWaitingTimeSeconds": "60",
            "rain": float(rLevel) / 100,
            "sessionOverTimeSeconds": "120",
            "sessions": [
                {
                  "dayOfWeekend": int(day),
                  "hourOfDay": int(start_time),
                  "sessionDurationMinutes": int(duration),
                  "sessionType": session,
                  "timeMultiplier": int(time_scale)
                },
                {
                  "dayOfWeekend": int(dayR),
                  "hourOfDay": int(start_timeR),
                  "sessionDurationMinutes": int(durationR),
                  "sessionType": sessionR,
                  "timeMultiplier": int(time_scaleR)
                }
            ],
            "simracerWeatherConditions": 1,
            "track": track,
            "trackTemp": int(trTemp),
            "weatherRandomness": int(wRandom)
        }
        
        #event dump json
        with open('E:/Steam/steamapps/common/Assetto Corsa Competizione Dedicated Server/server/cfg/event.json', "w") as f:
            json.dump(event_dict, f,indent="")
        #settings dump json
        with open('E:/Steam/steamapps/common/Assetto Corsa Competizione Dedicated Server/server/cfg/settings.json', 'w') as outfile:
            json.dump(settings_dict, outfile, indent="")
        
        working_dir = 'E:/Steam/steamapps/common/Assetto Corsa Competizione Dedicated Server/server/cfg/'
        #start server
        #os.startfile("E:/Steam/steamapps/common/Assetto Corsa Competizione Dedicated Server/server/accServer.exe")

        os.chdir("E:/Steam/steamapps/common/Assetto Corsa Competizione Dedicated Server/server/")
        os.system("accServer.exe")

    else:
        return render(request, 'registration/home.html')
    return render(request, 'registration/generated_json.html')
    

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # redirect to your home page after login
        else:
            # Invalid login
            return render(request, 'registration/login.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'registration/login.html')
        

def user_logout(request):
    logout(request)
    return redirect('app:login')  # redirect to login page after logout

def generated_json(request):
    if request.method == 'POST':
        serverName = request.POST.get('serverName')
        print(serverName)
    else:
        return render(request, 'registration/home.html')
    serverName = request.POST.get('serverName')
    print(serverName)
    return render(request, 'registration/login.html')
    
def terminateServer():
    output = subprocess.check_output(["tasklist", "/fi", "imagename eq accServer.exe"])

    # decode the output to a string and split it by newline
    lines = output.decode().split("\n")

    # get the PID if accServer.exe is running
    if len(lines) > 2:
        pid = lines[2].split()[1]
        subprocess.call(["taskkill", "/PID", pid, "/F"])
    else:
        print("accServer.exe is not running")

    import time
    time.sleep(3)

import psutil
def terminate_process(request):
    if request.method == 'POST':
        process_name='accServer.exe'
        print('start to kill accServer.exe')
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == process_name:
                pid = proc.pid
                os.kill(pid, 9)
    return render(request, 'registration/home.html')

def terminate_process2():
    process_name='accServer.exe'
    print('start to kill accServer.exe')
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            pid = proc.pid
            os.kill(pid, 9)