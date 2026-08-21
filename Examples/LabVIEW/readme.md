# LabVIEW Examples — XD-M Motor Controller

Xeryon's LabVIEW library handles all communication between the computer and one or more **XD-M** controllers, and exposes simple functions to control the connected stages. It's compact and works for as many stages as you want.

## Getting started

1. Open [`Xeryon Example project.lvproj`](Xeryon%20Example%20project.lvproj) in LabVIEW.
2. Make sure the device tuning file for your stages is in place under [`Preferences/`](Preferences/) — see [First-time use](#first-time-use) below. The file included here is tuned for the stages this example was built with, not a blank sample, so swap in the file matching your own stages before running.
3. Open [`Dynamic multi axis example.vi`](Dynamic%20multi%20axis%20example.vi). To control more or fewer stages, copy or remove the per-axis components inside the VI.
4. Before running, fill in the **Configuration** tab:
   - COM port and baud rate.
   - For each connected stage, its axis letter (e.g. `X`, `Y`, ...).
   - Each stage's resolution and the working units you want it to use — linear and rotating stages differ here.
5. Run the VI, then press **Find Index** on each stage so it can find its reference position and establish an absolute position. After that, you can move each stage with its own controls.

## First-time use

The tuning file included under `Preferences/` matches the demo stages this example was built with — swap it for your own stages before controlling real hardware:

1. Get the `settings_default.txt` file provided with the Windows Interface for each of your stages.
2. Merge them into [`Multi axis file.txt`](Preferences/Multi%20axis%20file.txt), prefixing every parameter with its axis letter (e.g. `C:FREQ=...`, `E:FREQ=...`).
3. Open it and, on any line containing `%`, remove the `%` and everything after it on that line.
4. Find every line containing `MSPD` or `SSPD` and multiply its value by:
   - **1000** for a linear stage
   - **100** for a rotating stage

## Project structure

| Folder | Contents |
|--------|----------|
| [`Axis driver/`](Axis%20driver/) | Low-level VIs implementing the per-axis command protocol — sending/receiving commands, status bits, unit conversion. |
| [`Axis Manager/`](Axis%20Manager/) | VIs for reading axis configuration and managing/enumerating the configured axes. |
| [`Serial driver/`](Serial%20driver/) | VIs handling the underlying COM/serial transport. |
| [`Sequencer/`](Sequencer/) | The sequencer VI — intended as the main program once your axes are configured. |
| [`Preferences/`](Preferences/) | Saved Configuration-tab settings and the device tuning file, read by the example above. |

## Preferences files

| File | Purpose |
|------|---------|
| [`COM-port.txt`](Preferences/COM-port.txt) | Last-used COM port. |
| [`config.txt`](Preferences/config.txt) | Saved Configuration-tab settings — axis letters, stage/resolution codes, and working range. |
| [`Multi axis file.txt`](Preferences/Multi%20axis%20file.txt) | Device tuning file (`settings_default.txt` equivalent), with parameters prefixed per axis letter (e.g. `C:`, `E:`). |

## Requirements

- LabVIEW (version compatible with `Xeryon Example project.lvproj`)
- An XD-M controller connected over a COM (serial) port

> [!TIP]
> If you're looking for the same examples in Python or C++, see [`../Python/readme.md`](../Python/readme.md) or [`../CPP/readme.md`](../CPP/readme.md).
