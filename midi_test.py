import sys
import os
import time

import pygame.midi
midi_str = ''
pygame.midi.init()
num_midi_devices = pygame.midi.get_count()
print("-----------------")
print(num_midi_devices)

for m in range(0, num_midi_devices):
    print("Device Number: ", m, " ----------------------- ")
    print(str(pygame.midi.get_device_info(m)))

midiInput = pygame.midi.Input(3)
while(True): 
    while(pygame.midi.Input.poll(midiInput) == False):
        time.sleep(.01)
    #we should have an item in our buffer
    midi_data = pygame.midi.Input.read(midiInput,1)
    midi_note, timestamp = midi_data[0]
    note_status, keynum, velocity, unused = midi_note
    print("Midi Note: \n\tNote Status: ", note_status, " Key Number: ", keynum," Velocity: " , velocity, "\n\tTime Stamp: ", timestamp)
    if note_status == 144:
        key_down = True
    elif note_status == 128: 
        key_down = False
    else:
        print("Unknown status!")


