import sys
import os
import time
import pygame.midi

#pygame.midi.init()
notes = [(261, "C"), (277, "C#", "Db"), (293, "D"), (311, "D#", "Eb"), (329, "E"), (349, "F"), (369, "F#", "Gb"), (392, "G"), (415, "G#", "Ab"), (440, "A"), (466, "A#", "Bb"), (493, "B")]
active_notes = [0 for i in range(0,107)]   #velocity of 0 indicates not is not active. Can set and unset in constant time

def freq_from_midi(midi_note_val): 
    octave = midi_note_val//12 #octave numberings start at 1
    value = midi_note_val%12 #lowest C starts at 0
    freq = int(notes[value][0]//(2**(4 - octave))) #scale from freq of mid C
    return freq

def note_from_midi(midi_note_val):
    return notes[midi_note_val%12][1]

def midi_init():
    pygame.midi.init()
    midiInput = pygame.midi.Input(3) 
     #add logic later to prompt user for desired input
    return midiInput

def process_midi_input(midi_data):
    midi_note, timestamp = midi_data[0]
    note_status, keynum, velocity, unused = midi_note #unpack tuple
    return (note_status, keynum, velocity, timestamp)

def print_all_notes():
    for n in range(0,96):
        freq = freq_from_midi(n)
        note = note_from_midi(n)
        print("Midi Key: ", n, " Note: " , note , " Frequency: " , freq)

def play(midiInput):
    #need a more efficient method for polling. Event based?? 
    while(True):
        while(pygame.midi.Input.poll(midiInput) == False):
            time.sleep(.01)
        #we should have an item in our buffer
        midi_data = pygame.midi.Input.read(midiInput,1)
        midi_note = process_midi_input(midi_data)
        if(midi_note[0] == 144):
            active_notes[midi_note[1]] = midi_note[2]
            print("Setting note ", midi_note[1] , " to ON")
        else:
            active_notes[midi_note[1]] = 0
            print("Setting note ", midi_note[1] , " to OFF")

play(midi_init())
