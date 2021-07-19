# FIRST BOT BY JLUISDEV
from pypresence import Presence
import time

#enviroments
my_state = "Solo"
my_details = "Ruby, Python, JavaScript && C++"
my_large_image = "joker"
my_small_image = "joker"
client_id = "TU_ID_DE_Aplicacion"

#Buttons & LINKS
my_label_1 = "My repos!"
my_url_1 = "https://github.com/jluisdeveloper"

my_label_2 = "Atcoder SadistCoder"
my_url_2 = "https://atcoder.jp/users/SadistCoder"

RPC = Presence(client_id) 
RPC.connect() 

print(RPC.update(state=my_state, details=my_details, large_image=my_large_image, small_image=my_small_image, buttons=[{"label": my_label_1, "url": my_url_1}, {"label": my_label_2, "url": my_url_2}], start=time.time()))

while True: 
    time.sleep(15) 