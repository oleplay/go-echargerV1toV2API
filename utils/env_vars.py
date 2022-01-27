from os import environ

def get_env():
    env_vars = {}
    if environ.get("GOECHARGER_URL"):
        env_vars['goecharger_url'] = environ.get("GOECHARGER_URL")
    else:
        print("GOECHARGER_URL not set")
        print("Using default: http://go-echarger")
        env_vars['goecharger_url'] = "http://go-echarger"

    if environ.get("PhaseSwitch_URL"):
        env_vars['phaseswitch_url'] = environ.get("PhaseSwitch_URL")
    else:
        print("PhaseSwitch_URL not set")
        print("Using default: http://phaseswitch")
        env_vars['phaseswitch_url'] = "http://phaseswitch"
    return env_vars

