import pyembroidery
import PySimpleGUI as sg
import os
from pathlib import Path

from pyembroidery import EmbPattern, STOP, write_dst

dst_dir = "C:/"

def main(file,length,fps):
    # print(f'File selected to reverse engineer, {file}')
    localPattern = pyembroidery.read(file)

    # settings for output
    stitchCount = localPattern.count_stitches()
    interval = round(stitchCount / (length * fps) - 1)

    newPattern = EmbPattern()

    pos = 0  # Current line in file
    i = 0  # local interval

    for stitch in localPattern.get_as_stitches():
        if i == interval:
            #print(f'{stitch}')
            if stitch[3] != 5:
                localPattern.stop(position=stitch[0])
                #print(f'New {stitch[0]}: {stitch}\n')
            i = 0
        else:

            pos = pos + 1
            i = i + 1

    #for stitch in localPattern.get_as_stitches():
        #print(f'{stitch}')

    # print(localPattern)
    print(f'Stitches: {stitchCount}')
    print(f'Interval: {interval}')

    design = []

    design.append(stitchCount)
    design.append(interval)
    design.append(localPattern)
    return design
    # write_dst(localPattern, "output.DST")

if __name__ == '__main__':

    keyVideoLength = sg.Text(key='keyVideoLength', size=(5, 1))
    keyVideoFPS = sg.Text(key='keyVideoFPS', size=(5, 1))

    left_pane = [
        # [sg.Image(size=(300, 100), filename='Logo-White.png')],
        [sg.Text("Choose a file: ")],
        [sg.FileBrowse(key='file', initial_folder=dst_dir,
                       file_types=(("*.dst", "*.dst"), ("*.*", "*.*"),))],
        [sg.HSeparator()],
        [sg.Text('Video Specs')],
        [sg.Text('Length in Seconds'), sg.Input('2',key='keyVideoLength')],
        [sg.Text('FPS'), sg.Input('20',key='keyVideoFPS')],
        [sg.Button('Read'), sg.Exit()]
    ]

    right_pane = [
        [sg.Text('Output Information:')],
        [sg.HSeparator()],
        [sg.Text('FileName: ',key='keyFileName')],
        [sg.Text('Total Stitches: ',key='keyStitches')],
        [sg.Text('Stitches per Picture: ',key='keyInterval')],
        [sg.HSeparator()],
        [sg.Button('Export')]
    ]

    row = [
        [
            sg.B('OK'),
            sg.B('Cancel')
        ]
    ]

    layout = [
        [
            sg.Column(left_pane),
            sg.VSeparator(),
            sg.Column(right_pane),
        ]
    ]

    # Create the window
    window = sg.Window("TheEmbroideryNerd - Stop-motion Embroidery Design Parser", layout)

    # Create an event loop
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        filename = values['file']
        videoLength = int(values['keyVideoLength'])
        videoFPS = int(values['keyVideoFPS'])

        window.find_element('keyFileName').Update('FileName: ' + os.path.basename(filename))

        design = main(filename, videoLength, videoFPS)

        window.find_element('keyStitches').Update('Total Stitches: ' + str(design[0]))
        window.find_element('keyInterval').Update('Stitches per Picture: ' + str(design[1]))

        if event == 'Export':
            outputFile = os.path.dirname(os.path.abspath(filename)) + '\\' + \
                         Path(filename).with_suffix('').stem + '.animated.dst'
            print(outputFile)
            write_dst(design[2], outputFile)

    window.close()
