from Xeryon import *
from matplotlib import pyplot as plt
import time

controller  = Xeryon("COM20", 115200)
axisA       = controller.addAxis(Stage.XLS_312_3N, "A")   # X axis
axisB       = controller.addAxis(Stage.XLS_312_3N, "B")   # Y axis
axisC       = controller.addAxis(Stage.XLS_78_3N, "C")    # Z axis (pen lift)

controller.start()

axisA.findIndex()
axisB.findIndex()
axisC.findIndex()

axisA.setUnits(Units.mm)
axisB.setUnits(Units.mm)
axisC.setUnits(Units.mm)

PEN_UP   = 2     # mm, retracted (not drawing)
PEN_DOWN = 0     # mm, touching surface (drawing)

# ---- Simple vector font: each letter = list of strokes, each stroke = list of (x, y) points ----
LETTERS = {
    "X": [[(0,0),(3,4)], [(0,4),(3,0)]],
    "E": [[(0,0),(0,4)], [(0,4),(2.5,4)], [(0,2),(2,2)], [(0,0),(2.5,0)]],
    "R": [[(0,0),(0,4)], [(0,4),(2.5,4),(2.5,2.2),(0,2.2)], [(0,2.2),(2.5,0)]],
    "Y": [[(0,4),(1.5,2)], [(3,4),(1.5,2)], [(1.5,2),(1.5,0)]],
    "O": [[(0,2),(1.5,4),(3,2),(1.5,0),(0,2)]],
    "N": [[(0,0),(0,4)], [(0,4),(3,0)], [(3,0),(3,4)]],
}

LETTER_WIDTH  = 3.5   # spacing between letters (mm)
SCALE         = 1.0   # scale factor if you need a bigger/smaller word

def build_path(word):
    """Return list of (x, y, pen_down) waypoints for the whole word."""
    path = []
    x_offset = 0
    for ch in word:
        strokes = LETTERS.get(ch.upper(), [])
        for stroke in strokes:
            for i, (x, y) in enumerate(stroke):
                px = (x_offset + x) * SCALE
                py = y * SCALE
                pen_down = (i != 0)   # first point of a stroke = travel move (pen up)
                path.append((px, py, pen_down))
        x_offset += LETTER_WIDTH
    return path

path = build_path("XERYON")

# ---- Start logging so we can plot the traced path afterward ----
axisA.startLogging()
axisB.startLogging()

# Move to the start point with pen up first
first_x, first_y, _ = path[0]
axisC.setDPOS(PEN_UP)
axisA.setDPOS(first_x)
axisB.setDPOS(first_y)
time.sleep(0.5)

for x, y, pen_down in path:
    axisC.setDPOS(PEN_DOWN if pen_down else PEN_UP)   # lift/lower pen
    axisA.setDPOS(x)
    axisB.setDPOS(y)
    while not (axisA.isPositionReached() and axisB.isPositionReached()):
        time.sleep(0.02)

axisC.setDPOS(PEN_UP)   # lift pen at the end

logs_a = axisA.endLogging()
logs_b = axisB.endLogging()

controller.stop()

# ---- Plot the traced shape: X (axis A) vs Y (axis B) ----
plt.plot(logs_a["EPOS"], logs_b["EPOS"])
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Traced path: XERYON")
plt.xlabel("Axis A position (encoder units)")
plt.ylabel("Axis B position (encoder units)")
plt.show()