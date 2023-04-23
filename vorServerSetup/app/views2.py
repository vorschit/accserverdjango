from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse, JsonResponse
from .forms import ServerSettingsForm
# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'registration/home.html')  # redirect to your home page after login
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
        form = ServerSettingsForm(request.POST)
        if form.is_valid():
            # retrieve the form data
            server_name = form.cleaned_data['server_name']
            admin_password = form.cleaned_data['admin_password']
            spectator_password = form.cleaned_data['spectator_password']
            tr_requirement = form.cleaned_data['tr_requirement']
            sa_requirement = form.cleaned_data['sa_requirement']
            rc_requirement = form.cleaned_data['rc_requirement']
            max_connections = form.cleaned_data['max_connections']
            max_car_slots = form.cleaned_data['max_car_slots']
            formation_lap_type = form.cleaned_data['formation_lap_type']
            is_locked_prep_phase = form.cleaned_data['is_locked_prep_phase']
            is_race_locked = form.cleaned_data['is_race_locked']
            short_formation_lap = form.cleaned_data['short_formation_lap']
            allow_auto_dq = form.cleaned_data['allow_auto_dq']
            randomize_track = form.cleaned_data['randomize_track']
            register_lobby = form.cleaned_data['register_lobby']
            lan_discovery = form.cleaned_data['lan_discovery']
            dump_leaderboards = form.cleaned_data['dump_leaderboards']
            dump_entry_list = form.cleaned_data['dump_entry_list']

            # create a dictionary with the form data
            form_data = {
                'serverName': server_name,
                'adminPassword': admin_password,
                'spectatorPassword': spectator_password,
                'trRequirement': tr_requirement,
                'saRequirement': sa_requirement,
                'rcRequirement': rc_requirement,
                'maxConnections': max_connections,
                'maxCarSlots': max_car_slots,
                'formationLapType': formation_lap_type,
                'isLockedPrepPhase': is_locked_prep_phase,
                'isRaceLocked': is_race_locked,
                'shortFormationLap': short_formation_lap,
                'allowAutoDQ': allow_auto_dq,
                'randomizeTrackWhenEmpty': randomize_track,
                'registerToLobby': register_lobby,
                'lanDiscovery': lan_discovery,
                'dumpLeaderboards': dump_leaderboards,
                'dumpEntryList': dump_entry_list
            }

            # write the dictionary to a JSON file
            file_path = 'E:/Steam/steamapps/common/Assetto Corsa Competizione Dedicated Server/server/cfg/settings2.json'
            with open(file_path, 'w') as f:
                json.dump(form_data, f,indent=4)

            # return a success response
            return render('generated_json.html',{'form' : form})

    # if the form is not valid, or if the request is not a POST request,
    # render the form with an error message
    return render(request, 'generated_json.html', {'form': form, 'error_message': 'Invalid form data'})