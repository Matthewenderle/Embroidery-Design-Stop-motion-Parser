# Stop-motion Embroidery Design Parser

> A Python script to turn any DST file into a stop-motion enabled design 

The purpose of this script is to take a DST file provided from an embroidery design file and parse it into *pyembroidery* to add machine stops and trims. Adding these commands into the DST file allows a machine operator to load the machine and stitch the number of stitches automatically and then the machine will eject the design to take a picture; in much the same way as stop-motion.

![img](https://i.imgur.com/4uaMBhG.png)

## 📦 Python Libraries

### PyEmbroidery

| Name | Description |
| --- | --- |
| [`pyembroidery`](https://github.com/EmbroidePy/pyembroidery) | pyembroidery library for reading and writing a variety of embroidery formats.  |

### PySimpleGUI

| Name | Description |
| --- | --- |
| [`pysimplegui`](https://www.pysimplegui.org/en/latest/) | Python GUIs for Humans |

## 🤖 Why use PySimpleGUI?

PySimpleGUI is being used to make the script **easier to use** for **non-techie people**. The purpose of this script *could* be done solely in the command line, but why not have a GUI? 


## 🎨 Features

* Specify the length in seconds that you would like the GIF to be.
* Specify the amount of frames per second to take. The higher the number, the more stitches will be done per picture.

## 🐾 Examples

### Animate logos into GIFs

![bjj-hat-logo](https://i.imgur.com/Ynfaqt9.gif)


### Setup

Clone it to local computer. Install python libraries.

```sh
$ git clone https://github.com/Matthewenderle/Stop-motion-Embroidery-Design-Parser.git
$ pip install pyembroidery
$ pip install pysimplegui
$ python main.py
```

