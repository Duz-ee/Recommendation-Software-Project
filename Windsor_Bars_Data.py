Legend = ["Name", "Google_rating", "live_music", "Address"]

Bars = [["Lefty's on the O", 4.2,"Yes", "341 Ouellete Ave"], 
["The Patio Lounge Windsor", 3.7, "No" "507 Ouellete Ave"], 
["The Loose Goose RestoPub & Lounge", 4.4, "No", "126 Ouellete Ave"], 
["Treehouse Bar & Grill", 4.2, "No", "351 Ouellete Ave"], 
["Phog Lounge", 4.6, "Yes", "157 University Ave W"], 
["The Dugout Sports Lounge", 4.2, "No", "157 University Ave W"], 
["The Liquid Library", 4.5, "No", "2135 Wyandotte St W"], 
["The Manchester Pub", 4.4, "No", "546 Ouellete Ave"],
["Legends Sports Bar", 3.9, "Yes", "377 Riverside Dr E"], 
["The Bull & Barrel Urban Saloon", 3.9, "No", "670 Ouellette Ave"],
["Maiden Lane Wine & Spirits", 4.8, "No", "494 Pelissier St"], 
["Rockhead Pub", 4.2, "Yes", "1444 Ottawa St"],
["TQLA", 3.0, "No", "481 Ouellete Ave"], 
["Eastwood's Grill and Lounge", 4.5, "No", "63 Riverside Dr E"],
["Vu Bar", 4.3, "Yes", "377 Riverside Dr E"], 
["Jimmy G's Bar and Grill", 4.5, "No", "2109 Wyandotte St W"],
["Victoria Tavern", 4.5, "Yes", "400 Chilver Rd"],
["Rock Bottom Bar & Grill", 4.4, "Yes", "3236 Sandwich St"],
["Dominion House", 4.4, "Yes", "3140 Sandwich St"],
["Verna-Q-Lar Lounge", 4.5, "No", "614 Erie St E"],
["Villians", 4.5, "Yes", "256 Pelissier St"],
["Blind Owl", 4.9, "Yes", "430 Ouellete Ave"],
["Tequila Bob's", 3.6, "No", "576 Ouellette Avenue Upper"],
["Wineology Restaurant & Bar", 4.1, "No", "1646 Wyandotte St E"],
["Hurricanes", 4.2, "No", "3217 Sandwich St."],
["Sidebar Lounge", 4.5, "Yes", "262 Pelissier St"],
["Kurley's AC", 4.6, "No", "1080 Erie St E"],
["Cosmos Lounge", 4.4, "Yes", "377 Riverside Dr E"],
["Bourbon Tap & Grill", 4.2, "Yes", "1199 Ottawa St"],
["Erie St GastroPub", 4.9, "No", "839 Erie St E"],
["Panache Restaurant And Lounge", 4.6, "No", "53 Pitt St E"],
["Kildare House", 4.3, "Yes", "1880 Wyandotte St E"],
["Lucky's RoadHouse", 3.9, "No", "5270 Tecumseh Rd E"],
["Player's Sports Club", 4.3, "Yes", "1530 Langlois Ave"],
["MD's SPORTS BAR and SMOKE HOUSE", 4.5, "No", "380 Mill St"],
["Jakes Roadhouse & Blues Joint", 4.1, "Yes", "2300 Huron Church Rd"],
["Time Out Pub & Grill", 5.0, "No", "3422 Walker Rd"],
["The Barrel House", 4.6, "Yes", "3199 Sandwich St"],
["Hurricanes", 4.2, "No", "3217 Sandwich St"],
["Hooligans Pub & Grub", 4.2, "No", "1898 Shepherd St E"],
["The Thirsty Butler Sports Bar", 4.5, "Yes", "1585 Wyandotte St E"],
["Brews & Cues", 4.3, "No", "5663 Ojibway Pkwy"],
["Average Joes Sports Bar", 4.3, "Yes", "1286 Lauzon Rd"],
["Parks & Rec Gastropub Sports Bar", 4.1, "No", "3087 Forest Glade Dr"],
["Seminole Bar & Grill", 3.8, "No", "3933 Seminole St"],
["Thompson House Restaurant & Pub", 4.3, "Yes", "5370 Wyandotte St E"],
["Lions Head Tavern", 4.0, "Yes", "7880 Wyandotte St E"],
["Lucky's RoadHouse", 3.9, "No", "5270 Tecumseh Rd E"],
["Good Time Charly Bar & Grill", 4.1, "Yes", "4715 Tecumseh Rd E"],
["Buddies Eatery & Tap", 4.2, "No", "3206 Sandwich St S"]]

# def get_live_music(bars):
#     live_music = []
#     for bar in bars:
#         if bar[2] == "Yes":
#             live_music.append(bar)
#     return live_music

# def get_no_live_music(bars):
#     no_live_music = []
#     for bar in bars:
#         if bar[2] == "No":
#             no_live_music.append(bar)
#     return no_live_music


def get_live_music(bars):
    live_music_dict = {}
    for bar in bars:
        if bar[2] == "Yes":
            live_music_dict[bar[0]] = [bar[1], bar[3]]
        else:
            continue
    return live_music_dict
    

print(get_live_music(Bars))
# print(get_no_live_music(Bars))
