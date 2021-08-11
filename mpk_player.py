import sys
import os
import time
import pygame.midi

#pygame.midi.init()
notes = [(261, "C"), (277, "C#", "Db"), (293, "D"), (311, "D#", "Eb"), (329, "E"), (349, "F"), (369, "F#", "Gb"), (392, "G"), (415, "G#", "Ab"), (440, "A"), (466, "A#", "Bb"), (493, "B")]
def freq_from_midi(midi_note):
    
    octave = midi_note//12 #octave numberings start at 1
    value = midi_note%12
    freq =int(notes[value][0]//(2**(4 - octave)))
    if value == 0: 
        print("Octave: " , octave , " Value: ", value)

    return ((notes[value][1], freq ))

def midi_init():
    pygame.midi.init()
    midiInput = pygame.midi.Input(3)
    return midiInput

def process_midi_input(midi_data):
    midi_note, timestamp = midi_data[0]
    note_status, keynum, velocity, unused = midi_note


for n in range(0,96):
    freq_str = freq_from_midi(n)
    if n%12 == 0:
        print("Midi Key: ", n, " Note: " , freq_str[0] , " Frequency: " , freq_str[1])
