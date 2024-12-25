# Multi-threading for faster file reading and fetching dat from API's


import threading
import time

def walk_dog(first, second):
    time.sleep(8)
    print(f"You finished walking {first} {second}.")


def take_out_trash():
    time.sleep(2)
    print("You finished taking out the trash.")

def get_mail():
    time.sleep(3)
    print("You finished getting the mail.")


# walk_dog()
# take_out_trash()
# get_mail()

chore1 = threading.Thread(target=walk_dog, args=("scobby","Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()  

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!.")

