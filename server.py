import requests
import csv
import time
import json

# with open("data.csv", "a", newline="\n") as file:
#                 csv_file = csv.writer(file)
#                 csv_file.writerow(["matchid", "timestamp", "game_time", "game_state", "pick_1", "pick_2", "pick_3", "pick_4", "pick_5", "pick_6", "pick_7", "pick_8", "pick_9", "pick_10", \
#                     'r1_hero_id', 'r1_level', 'r1_kills', 'r1_deaths', 'r1_assists', 'r1_denies', 'r1_lh', 'r1_gold', 'r1_x', 'r1_y', 'r1_net_worth',\
#                     'r2_hero_id', 'r2_level', 'r2_kills', 'r2_deaths', 'r2_assists', 'r2_denies', 'r2_lh', 'r2_gold', 'r2_x', 'r2_y', 'r2_net_worth',\
#                     'r3_hero_id', 'r3_level', 'r3_kills', 'r3_deaths', 'r3_assists', 'r3_denies', 'r3_lh', 'r3_gold', 'r3_x', 'r3_y', 'r3_net_worth',\
#                     'r4_hero_id', 'r4_level', 'r4_kills', 'r4_deaths', 'r4_assists', 'r4_denies', 'r4_lh', 'r4_gold', 'r4_x', 'r4_y', 'r4_net_worth',\
#                     'r5_hero_id', 'r5_level', 'r5_kills', 'r5_deaths', 'r5_assists', 'r5_denies', 'r5_lh', 'r5_gold', 'r5_x', 'r5_y', 'r5_net_worth',\
#                     'd1_hero_id', 'd1_level', 'd1_kills', 'd1_deaths', 'd1_assists', 'd1_denies', 'd1_lh', 'd1_gold', 'd1_x', 'd1_y', 'd1_net_worth',\
#                     'd2_hero_id', 'd2_level', 'd2_kills', 'd2_deaths', 'd2_assists', 'd2_denies', 'd2_lh', 'd2_gold', 'd2_x', 'd2_y', 'd2_net_worth',\
#                     'd3_hero_id', 'd3_level', 'd3_kills', 'd3_deaths', 'd3_assists', 'd3_denies', 'd3_lh', 'd3_gold', 'd3_x', 'd3_y', 'd3_net_worth',\
#                     'd4_hero_id', 'd4_level', 'd4_kills', 'd4_deaths', 'd4_assists', 'd4_denies', 'd4_lh', 'd4_gold', 'd4_x', 'd4_y', 'd4_net_worth',\
#                     'd5_hero_id', 'd5_level', 'd5_kills', 'd5_deaths', 'd5_assists', 'd5_denies', 'd5_lh', 'd5_gold', 'd5_x', 'd5_y', 'd5_net_worth',\
#                     'r_l1_t1', 'r_l1_t2', 'r_l1_t3', 'r_l2_t1', 'r_l2_t2', 'r_l2_t3', 'r_l3_t1', 'r_l3_t2', 'r_l3_t3', 'r_l2_t4_1', 'r_l2_t4_2',\
#                     'r_l1_b1', 'r_l1_b2', 'r_l2_b1', 'r_l2_b2', 'r_l3_b1', 'r_l3_b2',\
#                     'd_l1_t1', 'd_l1_t2', 'd_l1_t3', 'd_l2_t1', 'd_l2_t2', 'd_l2_t3', 'd_l3_t1', 'd_l3_t2', 'd_l3_t3', 'd_l2_t4_1', 'd_l2_t4_2',\
#                     'd_l1_b1', 'd_l1_b2', 'd_l2_b1', 'd_l2_b2', 'd_l3_b1', 'd_l3_b2'])

def collect_data(server_ids):
    if server_ids:
        for server in server_ids:
            try:
                game_data = requests.get("https://api.steampowered.com/IDOTA2MatchStats_570/GetRealtimeStats/v1?server_steam_id={}&key=03596879227149016F52869E8C8FD226".format(server)).json()
            except BaseException:
                continue
            except json.JSONDecodeError:
                continue
            with open("data.csv", "a", newline="\n") as file:
                csv_file = csv.writer(file)
                # csv_file.writerow(["matchid", "timestamp", "game_time", "game_state", "pick_1", "pick_2", "pick_3", "pick_4", "pick_5", "pick_6", "pick_7", "pick_8", "pick_9", "pick_10", \
                #     'r1_hero_id', 'r1_level', 'r1_kills', 'r1_deaths', 'r1_assists', 'r1_denies', 'r1_lh', 'r1_gold', 'r1_x', 'r1_y', 'r1_net_worth',\
                #     'r2_hero_id', 'r2_level', 'r2_kills', 'r2_deaths', 'r2_assists', 'r2_denies', 'r2_lh', 'r2_gold', 'r2_x', 'r2_y', 'r2_net_worth',\
                #     'r3_hero_id', 'r3_level', 'r3_kills', 'r3_deaths', 'r3_assists', 'r3_denies', 'r3_lh', 'r3_gold', 'r3_x', 'r3_y', 'r3_net_worth',\
                #     'r4_hero_id', 'r4_level', 'r4_kills', 'r4_deaths', 'r4_assists', 'r4_denies', 'r4_lh', 'r4_gold', 'r4_x', 'r4_y', 'r4_net_worth',\
                #     'r5_hero_id', 'r5_level', 'r5_kills', 'r5_deaths', 'r5_assists', 'r5_denies', 'r5_lh', 'r5_gold', 'r5_x', 'r5_y', 'r5_net_worth',\
                #     'd1_hero_id', 'd1_level', 'd1_kills', 'd1_deaths', 'd1_assists', 'd1_denies', 'd1_lh', 'd1_gold', 'd1_x', 'd1_y', 'd1_net_worth',\
                #     'd2_hero_id', 'd2_level', 'd2_kills', 'd2_deaths', 'd2_assists', 'd2_denies', 'd2_lh', 'd2_gold', 'd2_x', 'd2_y', 'd2_net_worth',\
                #     'd3_hero_id', 'd3_level', 'd3_kills', 'd3_deaths', 'd3_assists', 'd3_denies', 'd3_lh', 'd3_gold', 'd3_x', 'd3_y', 'd3_net_worth',\
                #     'd4_hero_id', 'd4_level', 'd4_kills', 'd4_deaths', 'd4_assists', 'd4_denies', 'd4_lh', 'd4_gold', 'd4_x', 'd4_y', 'd4_net_worth',\
                #     'd5_hero_id', 'd5_level', 'd5_kills', 'd5_deaths', 'd5_assists', 'd5_denies', 'd5_lh', 'd5_gold', 'd5_x', 'd5_y', 'd5_net_worth',\
                #     'r_l1_t1', 'r_l1_t2', 'r_l1_t3', 'r_l2_t1', 'r_l2_t2', 'r_l2_t3', 'r_l3_t1', 'r_l3_t2', 'r_l3_t3', 'r_l2_t4_1', 'r_l2_t4_2',\
                #     'r_l1_b1', 'r_l1_b2', 'r_l2_b1', 'r_l2_b2', 'r_l3_b1', 'r_l3_b2',\
                #     'd_l1_t1', 'd_l1_t2', 'd_l1_t3', 'd_l2_t1', 'd_l2_t2', 'd_l2_t3', 'd_l3_t1', 'd_l3_t2', 'd_l3_t3', 'd_l2_t4_1', 'd_l2_t4_2',\
                #     'd_l1_b1', 'd_l1_b2', 'd_l2_b1', 'd_l2_b2', 'd_l3_b1', 'd_l3_b2'])
                if "match" in game_data.keys():
                    if game_data["match"]["game_state"] == 5:
                        try:    
                            csv_file.writerow([game_data["match"]["matchid"], game_data["match"]["timestamp"], game_data["match"]["game_time"], game_data["match"]["game_state"],\
                            game_data["match"]["picks"][0]["hero"], game_data["match"]["picks"][1]["hero"], game_data["match"]["picks"][2]["hero"], game_data["match"]["picks"][3]["hero"], \
                            game_data["match"]["picks"][4]["hero"], game_data["match"]["picks"][5]["hero"], game_data["match"]["picks"][6]["hero"], game_data["match"]["picks"][7]["hero"], \
                            game_data["match"]["picks"][8]["hero"], game_data["match"]["picks"][9]["hero"], game_data["teams"][0]["players"][0]["heroid"], game_data["teams"][0]["players"][0]["level"],\
                            game_data["teams"][0]["players"][0]["kill_count"], game_data["teams"][0]["players"][0]["death_count"], game_data["teams"][0]["players"][0]["assists_count"], game_data["teams"][0]["players"][0]["denies_count"],\
                            game_data["teams"][0]["players"][0]["lh_count"], game_data["teams"][0]["players"][0]["gold"], game_data["teams"][0]["players"][0]["x"], game_data["teams"][0]["players"][0]["y"], \
                            game_data["teams"][0]["players"][0]["net_worth"], game_data["teams"][0]["players"][1]["heroid"], game_data["teams"][0]["players"][1]["level"],\
                            game_data["teams"][0]["players"][1]["kill_count"], game_data["teams"][0]["players"][1]["death_count"], game_data["teams"][0]["players"][1]["assists_count"], game_data["teams"][0]["players"][1]["denies_count"],\
                            game_data["teams"][0]["players"][1]["lh_count"], game_data["teams"][0]["players"][1]["gold"], game_data["teams"][0]["players"][1]["x"], game_data["teams"][0]["players"][1]["y"], \
                            game_data["teams"][0]["players"][1]["net_worth"], game_data["teams"][0]["players"][2]["heroid"], game_data["teams"][0]["players"][2]["level"],\
                            game_data["teams"][0]["players"][2]["kill_count"], game_data["teams"][0]["players"][2]["death_count"], game_data["teams"][0]["players"][2]["assists_count"], game_data["teams"][0]["players"][2]["denies_count"],\
                            game_data["teams"][0]["players"][2]["lh_count"], game_data["teams"][0]["players"][2]["gold"], game_data["teams"][0]["players"][2]["x"], game_data["teams"][0]["players"][2]["y"], \
                            game_data["teams"][0]["players"][2]["net_worth"], game_data["teams"][0]["players"][3]["heroid"], game_data["teams"][0]["players"][3]["level"],\
                            game_data["teams"][0]["players"][3]["kill_count"], game_data["teams"][0]["players"][3]["death_count"], game_data["teams"][0]["players"][3]["assists_count"], game_data["teams"][0]["players"][3]["denies_count"],\
                            game_data["teams"][0]["players"][3]["lh_count"], game_data["teams"][0]["players"][3]["gold"], game_data["teams"][0]["players"][3]["x"], game_data["teams"][0]["players"][3]["y"], \
                            game_data["teams"][0]["players"][3]["net_worth"], game_data["teams"][0]["players"][4]["heroid"], game_data["teams"][0]["players"][4]["level"],\
                            game_data["teams"][0]["players"][4]["kill_count"], game_data["teams"][0]["players"][4]["death_count"], game_data["teams"][0]["players"][4]["assists_count"], game_data["teams"][0]["players"][4]["denies_count"],\
                            game_data["teams"][0]["players"][4]["lh_count"], game_data["teams"][0]["players"][4]["gold"], game_data["teams"][0]["players"][4]["x"], game_data["teams"][0]["players"][4]["y"], \
                            game_data["teams"][0]["players"][4]["net_worth"], game_data["teams"][1]["players"][0]["heroid"], game_data["teams"][1]["players"][0]["level"],\
                            game_data["teams"][1]["players"][0]["kill_count"], game_data["teams"][1]["players"][0]["death_count"], game_data["teams"][1]["players"][0]["assists_count"], game_data["teams"][1]["players"][0]["denies_count"],\
                            game_data["teams"][1]["players"][0]["lh_count"], game_data["teams"][1]["players"][0]["gold"], game_data["teams"][1]["players"][0]["x"], game_data["teams"][1]["players"][0]["y"], \
                            game_data["teams"][1]["players"][0]["net_worth"], game_data["teams"][1]["players"][1]["heroid"], game_data["teams"][1]["players"][1]["level"],\
                            game_data["teams"][1]["players"][1]["kill_count"], game_data["teams"][1]["players"][1]["death_count"], game_data["teams"][1]["players"][1]["assists_count"], game_data["teams"][1]["players"][1]["denies_count"],\
                            game_data["teams"][1]["players"][1]["lh_count"], game_data["teams"][1]["players"][1]["gold"], game_data["teams"][1]["players"][1]["x"], game_data["teams"][1]["players"][1]["y"], \
                            game_data["teams"][1]["players"][1]["net_worth"], game_data["teams"][1]["players"][2]["heroid"], game_data["teams"][1]["players"][2]["level"],\
                            game_data["teams"][1]["players"][2]["kill_count"], game_data["teams"][1]["players"][2]["death_count"], game_data["teams"][1]["players"][2]["assists_count"], game_data["teams"][1]["players"][2]["denies_count"],\
                            game_data["teams"][1]["players"][2]["lh_count"], game_data["teams"][1]["players"][2]["gold"], game_data["teams"][1]["players"][2]["x"], game_data["teams"][1]["players"][2]["y"], \
                            game_data["teams"][1]["players"][2]["net_worth"], game_data["teams"][1]["players"][3]["heroid"], game_data["teams"][1]["players"][3]["level"],\
                            game_data["teams"][1]["players"][3]["kill_count"], game_data["teams"][1]["players"][3]["death_count"], game_data["teams"][1]["players"][3]["assists_count"], game_data["teams"][1]["players"][3]["denies_count"],\
                            game_data["teams"][1]["players"][3]["lh_count"], game_data["teams"][1]["players"][3]["gold"], game_data["teams"][1]["players"][3]["x"], game_data["teams"][1]["players"][3]["y"], \
                            game_data["teams"][1]["players"][3]["net_worth"], game_data["teams"][1]["players"][4]["heroid"], game_data["teams"][1]["players"][4]["level"],\
                            game_data["teams"][1]["players"][4]["kill_count"], game_data["teams"][1]["players"][4]["death_count"], game_data["teams"][1]["players"][4]["assists_count"], game_data["teams"][1]["players"][4]["denies_count"],\
                            game_data["teams"][1]["players"][4]["lh_count"], game_data["teams"][1]["players"][4]["gold"], game_data["teams"][1]["players"][4]["x"], game_data["teams"][1]["players"][4]["y"], \
                            game_data["teams"][1]["players"][4]["net_worth"], \
                            game_data["buildings"][0]["destroyed"], game_data["buildings"][1]["destroyed"], game_data["buildings"][2]["destroyed"], game_data["buildings"][3]["destroyed"], \
                            game_data["buildings"][4]["destroyed"], game_data["buildings"][5]["destroyed"], game_data["buildings"][6]["destroyed"], game_data["buildings"][7]["destroyed"], \
                            game_data["buildings"][8]["destroyed"], game_data["buildings"][9]["destroyed"], game_data["buildings"][10]["destroyed"], game_data["buildings"][11]["destroyed"], \
                            game_data["buildings"][12]["destroyed"], game_data["buildings"][13]["destroyed"], game_data["buildings"][14]["destroyed"], game_data["buildings"][15]["destroyed"], \
                            game_data["buildings"][16]["destroyed"], game_data["buildings"][18]["destroyed"], game_data["buildings"][19]["destroyed"], \
                            game_data["buildings"][20]["destroyed"], game_data["buildings"][21]["destroyed"], game_data["buildings"][22]["destroyed"], game_data["buildings"][23]["destroyed"], \
                            game_data["buildings"][24]["destroyed"], game_data["buildings"][25]["destroyed"], game_data["buildings"][26]["destroyed"], game_data["buildings"][27]["destroyed"], \
                            game_data["buildings"][28]["destroyed"], game_data["buildings"][29]["destroyed"], game_data["buildings"][30]["destroyed"], game_data["buildings"][31]["destroyed"], \
                            game_data["buildings"][32]["destroyed"], game_data["buildings"][33]["destroyed"], game_data["buildings"][34]["destroyed"]])
                        except KeyError:
                            continue  
                        except IndexError:
                            continue  
                    else:
                        continue
                else:
                    continue

while True:
    server_ids = []
    for j in range(4):
        try:
            r = requests.get("https://api.steampowered.com/IDOTA2Match_570/GetTopLiveGame/v1/?key=03596879227149016F52869E8C8FD226&partner={}".format(j))
        except BaseException:
            continue
        except ConnectionError:
            continue
        try:
            data = r.json()
        except json.JSONDecodeError:
            continue
        if "game_list" in data.keys():
            for i in data["game_list"]:
                if "team_name_radiant" in i and "team_name_dire" in i:
                    server_ids.append(i["server_steam_id"])
        else:
            continue
        time.sleep(1)
    server_ids = list(set(server_ids))            
    collect_data(server_ids)
    time.sleep(56)




# def collect_data(server_ids):
#     if server_ids:
#         for server in server_ids:
#             game_data = requests.get("https://api.steampowered.com/IDOTA2MatchStats_570/GetRealtimeStats/v1?server_steam_id={}&key=03596879227149016F52869E8C8FD226".format(server)).json()
#             with open("data.csv", "a", newline="") as file:
#                 csv_file = csv.writer(file)
#                 # csv_file.writerow(["matchid", "timestamp", "game_time", "game_state", "pick_1", "pick_2", "pick_3", "pick_4", "pick_5", "pick_6", "pick_7", "pick_8", "pick_9", "pick_10", \
#                 #     'r1_hero_id', 'r1_level', 'r1_kills', 'r1_deaths', 'r1_assists', 'r1_denies', 'r1_lh', 'r1_gold', 'r1_x', 'r1_y', 'r1_net_worth',\
#                 #     'r2_hero_id', 'r2_level', 'r2_kills', 'r2_deaths', 'r2_assists', 'r2_denies', 'r2_lh', 'r2_gold', 'r2_x', 'r2_y', 'r2_net_worth',\
#                 #     'r3_hero_id', 'r3_level', 'r3_kills', 'r3_deaths', 'r3_assists', 'r3_denies', 'r3_lh', 'r3_gold', 'r3_x', 'r3_y', 'r3_net_worth',\
#                 #     'r4_hero_id', 'r4_level', 'r4_kills', 'r4_deaths', 'r4_assists', 'r4_denies', 'r4_lh', 'r4_gold', 'r4_x', 'r4_y', 'r4_net_worth',\
#                 #     'r5_hero_id', 'r5_level', 'r5_kills', 'r5_deaths', 'r5_assists', 'r5_denies', 'r5_lh', 'r5_gold', 'r5_x', 'r5_y', 'r5_net_worth',\
#                 #     'd1_hero_id', 'd1_level', 'd1_kills', 'd1_deaths', 'd1_assists', 'd1_denies', 'd1_lh', 'd1_gold', 'd1_x', 'd1_y', 'd1_net_worth',\
#                 #     'd2_hero_id', 'd2_level', 'd2_kills', 'd2_deaths', 'd2_assists', 'd2_denies', 'd2_lh', 'd2_gold', 'd2_x', 'd2_y', 'd2_net_worth',\
#                 #     'd3_hero_id', 'd3_level', 'd3_kills', 'd3_deaths', 'd3_assists', 'd3_denies', 'd3_lh', 'd3_gold', 'd3_x', 'd3_y', 'd3_net_worth',\
#                 #     'd4_hero_id', 'd4_level', 'd4_kills', 'd4_deaths', 'd4_assists', 'd4_denies', 'd4_lh', 'd4_gold', 'd4_x', 'd4_y', 'd4_net_worth',\
#                 #     'd5_hero_id', 'd5_level', 'd5_kills', 'd5_deaths', 'd5_assists', 'd5_denies', 'd5_lh', 'd5_gold', 'd5_x', 'd5_y', 'd5_net_worth',\
#                 #     'r_l1_t1', 'r_l1_t2', 'r_l1_t3', 'r_l2_t1', 'r_l2_t2', 'r_l2_t3', 'r_l3_t1', 'r_l3_t2', 'r_l3_t3', 'r_l2_t4_1', 'r_l2_t4_2',\
#                 #     'r_l1_b1', 'r_l1_b2', 'r_l2_b1', 'r_l2_b2', 'r_l3_b1', 'r_l3_b2',\
#                 #     'd_l1_t1', 'd_l1_t2', 'd_l1_t3', 'd_l2_t1', 'd_l2_t2', 'd_l2_t3', 'd_l3_t1', 'd_l3_t2', 'd_l3_t3', 'd_l2_t4_1', 'd_l2_t4_2',\
#                 #     'd_l1_b1', 'd_l1_b2', 'd_l2_b1', 'd_l2_b2', 'd_l3_b1', 'd_l3_b2'])
#                 if game_data["match"]["game_state"] == 5:
#                     csv_file.writerow([game_data["match"]["matchid"], game_data["match"]["timestamp"], game_data["match"]["game_time"], game_data["match"]["game_state"],\
#                     game_data["match"]["picks"][0]["hero"], game_data["match"]["picks"][1]["hero"], game_data["match"]["picks"][2]["hero"], game_data["match"]["picks"][3]["hero"], \
#                     game_data["match"]["picks"][4]["hero"], game_data["match"]["picks"][5]["hero"], game_data["match"]["picks"][6]["hero"], game_data["match"]["picks"][7]["hero"], \
#                     game_data["match"]["picks"][8]["hero"], game_data["match"]["picks"][9]["hero"], game_data["teams"][0]["players"][0]["heroid"], game_data["teams"][0]["players"][0]["level"],\
#                     game_data["teams"][0]["players"][0]["kill_count"], game_data["teams"][0]["players"][0]["death_count"], game_data["teams"][0]["players"][0]["assists_count"], game_data["teams"][0]["players"][0]["denies_count"],\
#                     game_data["teams"][0]["players"][0]["lh_count"], game_data["teams"][0]["players"][0]["gold"], game_data["teams"][0]["players"][0]["x"], game_data["teams"][0]["players"][0]["y"], \
#                     game_data["teams"][0]["players"][0]["net_worth"], game_data["teams"][0]["players"][1]["heroid"], game_data["teams"][0]["players"][1]["level"],\
#                     game_data["teams"][0]["players"][1]["kill_count"], game_data["teams"][0]["players"][1]["death_count"], game_data["teams"][0]["players"][1]["assists_count"], game_data["teams"][0]["players"][1]["denies_count"],\
#                     game_data["teams"][0]["players"][1]["lh_count"], game_data["teams"][0]["players"][1]["gold"], game_data["teams"][0]["players"][1]["x"], game_data["teams"][0]["players"][1]["y"], \
#                     game_data["teams"][0]["players"][1]["net_worth"], game_data["teams"][0]["players"][2]["heroid"], game_data["teams"][0]["players"][2]["level"],\
#                     game_data["teams"][0]["players"][2]["kill_count"], game_data["teams"][0]["players"][2]["death_count"], game_data["teams"][0]["players"][2]["assists_count"], game_data["teams"][0]["players"][2]["denies_count"],\
#                     game_data["teams"][0]["players"][2]["lh_count"], game_data["teams"][0]["players"][2]["gold"], game_data["teams"][0]["players"][2]["x"], game_data["teams"][0]["players"][2]["y"], \
#                     game_data["teams"][0]["players"][2]["net_worth"], game_data["teams"][0]["players"][3]["heroid"], game_data["teams"][0]["players"][3]["level"],\
#                     game_data["teams"][0]["players"][3]["kill_count"], game_data["teams"][0]["players"][3]["death_count"], game_data["teams"][0]["players"][3]["assists_count"], game_data["teams"][0]["players"][3]["denies_count"],\
#                     game_data["teams"][0]["players"][3]["lh_count"], game_data["teams"][0]["players"][3]["gold"], game_data["teams"][0]["players"][3]["x"], game_data["teams"][0]["players"][3]["y"], \
#                     game_data["teams"][0]["players"][3]["net_worth"], game_data["teams"][0]["players"][4]["heroid"], game_data["teams"][0]["players"][4]["level"],\
#                     game_data["teams"][0]["players"][4]["kill_count"], game_data["teams"][0]["players"][4]["death_count"], game_data["teams"][0]["players"][4]["assists_count"], game_data["teams"][0]["players"][4]["denies_count"],\
#                     game_data["teams"][0]["players"][4]["lh_count"], game_data["teams"][0]["players"][4]["gold"], game_data["teams"][0]["players"][4]["x"], game_data["teams"][0]["players"][4]["y"], \
#                     game_data["teams"][0]["players"][4]["net_worth"], game_data["teams"][1]["players"][0]["heroid"], game_data["teams"][1]["players"][0]["level"],\
#                     game_data["teams"][1]["players"][0]["kill_count"], game_data["teams"][1]["players"][0]["death_count"], game_data["teams"][1]["players"][0]["assists_count"], game_data["teams"][1]["players"][0]["denies_count"],\
#                     game_data["teams"][1]["players"][0]["lh_count"], game_data["teams"][1]["players"][0]["gold"], game_data["teams"][1]["players"][0]["x"], game_data["teams"][1]["players"][0]["y"], \
#                     game_data["teams"][1]["players"][0]["net_worth"], game_data["teams"][1]["players"][1]["heroid"], game_data["teams"][1]["players"][1]["level"],\
#                     game_data["teams"][1]["players"][1]["kill_count"], game_data["teams"][1]["players"][1]["death_count"], game_data["teams"][1]["players"][1]["assists_count"], game_data["teams"][1]["players"][1]["denies_count"],\
#                     game_data["teams"][1]["players"][1]["lh_count"], game_data["teams"][1]["players"][1]["gold"], game_data["teams"][1]["players"][1]["x"], game_data["teams"][1]["players"][1]["y"], \
#                     game_data["teams"][1]["players"][1]["net_worth"], game_data["teams"][1]["players"][2]["heroid"], game_data["teams"][1]["players"][2]["level"],\
#                     game_data["teams"][1]["players"][2]["kill_count"], game_data["teams"][1]["players"][2]["death_count"], game_data["teams"][1]["players"][2]["assists_count"], game_data["teams"][1]["players"][2]["denies_count"],\
#                     game_data["teams"][1]["players"][2]["lh_count"], game_data["teams"][1]["players"][2]["gold"], game_data["teams"][1]["players"][2]["x"], game_data["teams"][1]["players"][2]["y"], \
#                     game_data["teams"][1]["players"][2]["net_worth"], game_data["teams"][1]["players"][3]["heroid"], game_data["teams"][1]["players"][3]["level"],\
#                     game_data["teams"][1]["players"][3]["kill_count"], game_data["teams"][1]["players"][3]["death_count"], game_data["teams"][1]["players"][3]["assists_count"], game_data["teams"][1]["players"][3]["denies_count"],\
#                     game_data["teams"][1]["players"][3]["lh_count"], game_data["teams"][1]["players"][3]["gold"], game_data["teams"][1]["players"][3]["x"], game_data["teams"][1]["players"][3]["y"], \
#                     game_data["teams"][1]["players"][3]["net_worth"], game_data["teams"][1]["players"][4]["heroid"], game_data["teams"][1]["players"][4]["level"],\
#                     game_data["teams"][1]["players"][4]["kill_count"], game_data["teams"][1]["players"][4]["death_count"], game_data["teams"][1]["players"][4]["assists_count"], game_data["teams"][1]["players"][4]["denies_count"],\
#                     game_data["teams"][1]["players"][4]["lh_count"], game_data["teams"][1]["players"][4]["gold"], game_data["teams"][1]["players"][4]["x"], game_data["teams"][1]["players"][4]["y"], \
#                     game_data["teams"][1]["players"][4]["net_worth"], \
#                     game_data["buildings"][0]["destroyed"], game_data["buildings"][1]["destroyed"], game_data["buildings"][2]["destroyed"], game_data["buildings"][3]["destroyed"], \
#                     game_data["buildings"][4]["destroyed"], game_data["buildings"][5]["destroyed"], game_data["buildings"][6]["destroyed"], game_data["buildings"][7]["destroyed"], \
#                     game_data["buildings"][8]["destroyed"], game_data["buildings"][9]["destroyed"], game_data["buildings"][10]["destroyed"], game_data["buildings"][11]["destroyed"], \
#                     game_data["buildings"][12]["destroyed"], game_data["buildings"][13]["destroyed"], game_data["buildings"][14]["destroyed"], game_data["buildings"][15]["destroyed"], \
#                     game_data["buildings"][16]["destroyed"], game_data["buildings"][18]["destroyed"], game_data["buildings"][19]["destroyed"], \
#                     game_data["buildings"][20]["destroyed"], game_data["buildings"][21]["destroyed"], game_data["buildings"][22]["destroyed"], game_data["buildings"][23]["destroyed"], \
#                     game_data["buildings"][24]["destroyed"], game_data["buildings"][25]["destroyed"], game_data["buildings"][26]["destroyed"], game_data["buildings"][27]["destroyed"], \
#                     game_data["buildings"][28]["destroyed"], game_data["buildings"][29]["destroyed"], game_data["buildings"][30]["destroyed"], game_data["buildings"][31]["destroyed"], \
#                     game_data["buildings"][32]["destroyed"], game_data["buildings"][33]["destroyed"], game_data["buildings"][34]["destroyed"]])
#                 else:
#                     continue