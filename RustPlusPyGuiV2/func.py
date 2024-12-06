import yaml


def get_base_code():
    with open("cfg.yml", "r") as f:
        contents = yaml.safe_load(f)
        base_code = contents["base_code"]        
    return base_code

def check_base_code(input_code : str):
    pass

def get_main_client_details():
    pass

def get_servers():
    pass

def get_general_server_info(socket): # work on it later
    info = socket.get_info()
    print(type(info))
    pass

def get_map_image(socket):
    map_image = socket.get_map(add_icons=True, add_events=True, add_vending_machines=True, add_team_positions=True, add_grid=True)
    pass
 # finish later. this is a priority