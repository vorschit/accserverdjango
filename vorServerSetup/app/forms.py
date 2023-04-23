from django import forms

class ServerSettingsForm(forms.Form):
    server_name = forms.CharField(label='Server Name', max_length=100)
    admin_password = forms.CharField(label='Admin Password', max_length=255)
    spectator_password = forms.CharField(label='Spectator Password', max_length=255)
    tr_requirement = forms.IntegerField(label='Track Medals Requirement')
    sa_requirement = forms.IntegerField(label='Safety Rating Requirement')
    rc_requirement = forms.IntegerField(label='Racecraft Rating Requirement')
    max_connections = forms.IntegerField(label='Max Connections')
    max_car_slots = forms.IntegerField(label='Max Car Slots')
    formation_lap_type = forms.ChoiceField(
        label='Formation Lap Type',
        choices=[('0', 'No formation lap'), ('1', 'Full formation lap'), ('2', 'Rolling start')]
    )
    is_locked_prep_phase = forms.BooleanField(label='Lock Server During Preparation Phase', required=False)
    is_race_locked = forms.BooleanField(label='Lock Server During Race', required=False)
    short_formation_lap = forms.BooleanField(label='Short Formation Lap', required=False)
    allow_auto_dq = forms.BooleanField(label='Auto Disqualify Drivers', required=False)
    randomize_track = forms.BooleanField(label='Randomize Track When Empty', required=False)
    register_lobby = forms.BooleanField(label='Register to Lobby', required=False)
    lan_discovery = forms.BooleanField(label='LAN Discovery', required=False)
    dump_leaderboards = forms.BooleanField(label='Dump Leaderboards', required=False)
    dump_entry_list = forms.BooleanField(label='Dump Entry List', required=False)

