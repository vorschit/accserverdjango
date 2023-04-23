from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse, JsonResponse
from .forms import ServerSettingsForm
# Create your views here.

@login_required
def home(request):

    #server setting
    serverName = request.POST.get('serverName')
    adminPassword = request.POST.get('adminPassword')
    spectatorPassword = request.POST.get('spectatorPassword')
    TR = request.POST.get('TR')
    SA = request.POST.get('SA')
    RC = request.POST.get('RC')
    mConnection = request.POST.get('mConnection')
    formationLap = request.POST.get('formationLap')
    mCarSlot = request.POST.get('mCarSlot')
    formationLap = request.POST.get('formationLap')
    prephase = request.POST.get('prephase')
    racelocked = request.POST.get('racelocked')
    shortformationlap = request.POST.get('shortformationlap')
    autodq = request.POST.get('autodq')
    randomizetrack = request.POST.get('randomizetrack')
    registerlobby = request.POST.get('registerlobby')
    landiscovery = request.POST.get('landiscovery')
    dumpleaderboard = request.POST.get('dumpleaderboard')
    dumpentrylist = request.POST.get('dumpentrylist')

    # Miscellaneaous
    preRace = request.POST.get('preRace')
    postRace = request.POST.get('postRace')
    overTime = request.POST.get('overTime')
    postQualy = request.POST.get('postQualy')
    track = request.POST.get('track')

    #Weather
    amTemp = request.POST.get('amTemp')
    trTemp = request.POST.get('trTemp')
    cCover = request.POST.get('cCover')
    rLevel = request.POST.get('rLevel')
    wRandom = request.POST.get('wRandom')

    #format value
    #cCover = int(cCover)/100
    #rLevel = int(rLevel)/100
    if cCover is not None:
        cCover = int(cCover) / 100

    if rLevel is not None:
        rLevel = int(rLevel) / 100
    

    if request.method == 'POST':

        #setting .json file
        settings_dict = {
            "serverName": serverName,
            "adminPassword": adminPassword,
            "password": "",
            "spectatorPassword": spectatorPassword,
            "centralEntryListPath": "",
            "carGroup": "FreeForAll",
            "trackMedalsRequirement": TR,
            "safetyRatingRequirement": SA,
            "racecraftRatingRequirement": RC,
            "maxCarSlots": mCarSlot,
            "isRaceLocked": racelocked,
            "isLockedPrepPhase": prephase,
            "shortFormationLap": shortformationlap,
            "dumpLeaderboards": dumpleaderboard,
            "dumpEntryList": dumpentrylist,
            "randomizeTrackWhenEmpty": randomizetrack,
            "allowAutoDQ": autodq,
            "ignorePrematureDisconnects": 0,
            "formationLapType": formationLap,
            "configVersion": 1
        }

        # event .json file
        event_dict={
            "ambientTemp": int(amTemp),
            "cloudLevel": float(cCover),
            "configVersion": 1,
            "isFixedConditionQualification": 1,
            "postQualySeconds": int(postQualy),
            "postRaceSeconds": int(postRace),
            "preRaceWaitingTimeSeconds": int(preRace),
            "rain": float(rLevel) / 100,
            "sessionOverTimeSeconds": int(overTime),
            "sessions": [
                {
                  "dayOfWeekend": 3,
                  "hourOfDay": 16,
                  "sessionDurationMinutes": 500,
                  "sessionType": "Q",
                  "timeMultiplier": 1
                },
                {
                  "dayOfWeekend": 2,
                  "hourOfDay": 13,
                  "sessionDurationMinutes": 60,
                  "sessionType": "R",
                  "timeMultiplier": 1
                }
            ],
            "simracerWeatherConditions": 1,
            "track": track,
            "trackTemp": int(trTemp),
            "weatherRandomness": int(wRandom)
        }
        
        print(event_dict)
        print(settings_dict)
        #event dump json
        with open('E:/Steam/steamapps/common/Assetto Corsa Competizione Dedicated Server/server/cfg/event2.json', "w") as f:
            json.dump(event_dict, f,indent="")
        #settings dump json
        with open('E:/Steam/steamapps/common/Assetto Corsa Competizione Dedicated Server/server/cfg/settings2.json', 'w') as outfile:
            json.dump(settings_dict, outfile, indent="")

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