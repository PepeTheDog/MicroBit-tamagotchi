from microbit import *
import random

state = "happy"
state_changer = 0
food = 0
toy = 0
time = 0
frame_timer = 0
food_timer = 0
toy_timer = 0

happy = Image("00000:" "06060:" "00000:" "60006:" "06660:")
sad = Image("00000:" "06060:" "00000:" "06660:" "60006:")
hungry = Image("06060:" "00000:" "06660:" "60006:" "06660:")
dead = Image("00000:" "66066:" "00000:" "06660:" "00000:")

while True:
    if button_a.is_pressed():
        food_timer = running_time()
        food = 1
    if button_b.is_pressed():
        toy_timer = running_time()
        toy = 1
    if food == 1 and running_time() - food_timer >= 1000:
        food_timer = 0
        food = 0
    if toy == 1 and running_time() - toy_timer >= 1000:
        toy_timer = 0
        toy = 0
    if running_time() - frame_timer >= 100:
        frame_timer = running_time()
        if state == "happy":
            display.show(happy)
            state_changer = 0
        if state == "happy" and state_changer == 0:
            state_changer = random.randint(1, 1102)
        if state == "happy" and state_changer <= 51:
            state = "hungry"
            time = running_time()
        elif state == "happy" and state_changer >= 1051:
            state = "sad"
            time = running_time()
        state_changer = 0
        # happy
        if state == "hungry":
            display.show(hungry)
        if state == "hungry" and food == 0:
            if running_time() - time >= 5000:
                state = "dead"
        elif state == "hungry" and food == 1:
            state = "happy"
            food = 0
        # hungry
        if state == "sad":
            display.show(sad)
        if state == "sad" and toy == 0:
            if running_time() - time >= 5000:
                state = "dead"
        elif state == "sad" and toy == 1:
            state = "happy"
            toy = 0
        # sad
        if state == "dead":
            display.show(dead)
