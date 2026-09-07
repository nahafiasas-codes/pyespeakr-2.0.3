pyespeakr 2.0.3

pyespeakr is a Python module that provides a layer between the eSpeak text-to-speech engine and Python. It allows Python programs to use eSpeak through a simple Python interface.

Version 2.0.3 contains significant internal changes. The module has been redesigned from a function-based architecture to an object-oriented architecture. This change was made primarily to improve code organization, command management, and maintainability.

The module has not significantly increased in size despite these internal changes. Its size remains approximately 3–4 KB.

Creating a Pypkr Object

The main interface of the module is the "Pypkr" class.
------------------------------------------
import pyespeakr as pypkr

class_pypkr = pypkr.Pypkr()
------------------------------------------
After creating an object, the available settings and methods can be accessed through that object.

Main Class Attributes

The "Pypkr" class provides several attributes for controlling the behavior of the speech engine.

Attribute| Default value| Description
"language"| ""en""| Sets the language used for speech synthesis.
"voices"| ""m3""| Selects the voice used by eSpeak.
"speed"| "175"| Controls the speech speed.
"volume"| "100"| Controls the speech volume.
"word_gap"| "0"| Controls the gap between words.
"pitch"| "50"| Controls the voice pitch.
"espeak"| "0"| Selects the speech engine. "0" uses "espeak", while "1" uses "espeak-ng".
"name"| ""a.wav""| Specifies the filename used when saving generated speech.
"__version__"| ""2.0.0""| Contains the current module version.

For example, the speech speed can be changed directly:

class_pypkr.speed = 200

The voice can also be changed:

class_pypkr.voice("f", 1)

Main Methods

"say(data)"

Converts the provided text to speech and plays it immediately.
------------------------------------------
class_pypkr.say("Hello")
------------------------------------------
The text is sent to the selected eSpeak engine using the current language, voice, speed, volume, word gap, and pitch settings.

By default, the text is spoken using an English male voice.

"save_to_file(data)"

Converts the provided text to speech and saves the generated audio to a WAV file.
------------------------------------------
class_pypkr.save_to_file("Hello")
------------------------------------------
The default output filename is:

a.wav

The filename can be changed through the "name" attribute:

class_pypkr.name = "hello.wav"
class_pypkr.save_to_file("Hello")

"voice(data, data1)"

Changes the selected voice.

The first argument specifies the voice family:

- ""m"" — male voice
- ""f"" — female voice

The second argument specifies the voice number.

Example:

class_pypkr.voice("m", 3)

or:

class_pypkr.voice("f", 2)

The method returns "0" when the requested voice is accepted and "1" when the requested voice is invalid.

Engine Selection

pyespeakr supports two eSpeak command-line engines:

espeak
espeak-ng

The selected engine is controlled through the "espeak" attribute.

class_pypkr.espeak = 0

uses:

espeak

while:

class_pypkr.espeak = 1

uses:

espeak-ng

Parameter Validation

Before speech generation, pyespeakr performs basic validation of its configuration values.

Invalid values for speed, volume, pitch, word gap, or engine selection are replaced with their default values.

This helps prevent invalid settings from being passed to the eSpeak engine.

General Workflow

A typical use of pyespeakr looks like this:
------------------------------------------
import pyespeakr as pypkr

class_pypkr = pypkr.Pypkr()

class_pypkr.language = "en"
class_pypkr.speed = 175
class_pypkr.volume = 100

class_pypkr.say("Hello")
------------------------------------------
The same configuration can be used to generate an audio file:
------------------------------------------
class_pypkr.save_to_file("Hello")
------------------------------------------
Removed Functionality

The "open_file" function has been removed in version 2.0.0 due to internal implementation problems.

It is no longer part of the public API of the module.

Additionally, code written for version 1.0.0 is no longer supported in version 2.0.3. Version 2.0.3 uses a different internal architecture, and code written for version 1.0.0 may not work without modifications.