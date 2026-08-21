from Xeryon import *                                    # Import the Xeryon library
from matplotlib import pyplot as plt                    # Import the matplotlib library

controller  = Xeryon("COM20", 115200)                       # Setup serial communication, select the correct COM-port and baudrate
axisA       = controller.addAxis(Stage.XLS_312_3N, "A")     # Add axis A
axisB       = controller.addAxis(Stage.XLS_312_3N, "B")     # Add axis B
axisC       = controller.addAxis(Stage.XLS_78_3N, "C")      # Add axis C

controller.start()              # Start the controller

axisA.findIndex()               # Search for the index of axis A
axisB.findIndex()               # Search for the index of axis B
axisC.findIndex()               # Search for the index of axis C

axisA.setUnits(Units.mm)        # Set units to mm for axis A
axisB.setUnits(Units.mm)        # Set units to mm for axis B
axisC.setUnits(Units.mm)        # Set units to mm for axis C

axisA.startLogging()            # Start logging for axis A
axisB.startLogging()            # Start logging for axis B
axisC.startLogging()            # Start logging for axis C

axisA.startScan(-1)             # Start scan in the -1 direction
axisB.startScan(-1)             # Start scan in the -1 direction
axisC.startScan(-1)             # Start scan in the -1 direction
time.sleep(2)                   # Wait 2 seconds
axisA.startScan(1)              # Start scan in the 1 direction
axisB.startScan(1)              # Start scan in the 1 direction
axisC.startScan(1)              # Start scan in the 1 direction
time.sleep(2)                   # Wait 2 seconds

axisA.setSpeed(5)               # Set speed to 5 mm/s
axisB.setSpeed(5)               # Set speed to 5 mm/s
axisC.setSpeed(5)               # Set speed to 5 mm/s

axisA.startScan(-1)             # Start scan in the -1 direction
time.sleep(1)                   # Wait 1 second
axisA.stopScan()                # Stop scan
time.sleep(2)                   # Wait 2 seconds
axisA.startScan(-1, 1)          # Start scan in the -1 direction for 1 second
time.sleep(2)                   # Wait 2 seconds

axisB.startScan(-1)             # Start scan in the 1 direction
time.sleep(1)                   # Wait 1 second
axisB.stopScan()                # Stop scan
time.sleep(2)                   # Wait 2 seconds
axisB.startScan(-1, 1)          # Start scan in the 1 direction for 1 second
time.sleep(2)                   # Wait 2 seconds

axisC.startScan(-1)             # Start scan in the -1 direction
time.sleep(1)                   # Wait 1 second
axisC.stopScan()                # Stop scan
time.sleep(2)                   # Wait 2 seconds
axisC.startScan(-1, 1)          # Start scan in the -1 direction for 1 second
time.sleep(2)                   # Wait 2 seconds

axisA.setDPOS(0)                # Go to position 0 mm
axisB.setDPOS(0)                # Go to position 0 mm
axisC.setDPOS(0)                # Go to position 0 mm

time.sleep(2)                   # Wait 2 seconds
axisA.setDPOS(10)               # Go to position 10 mm
time.sleep(2)                   # Wait 2 seconds
axisA.setSpeed(200)             # Set speed to 200 mm/s
axisA.setDPOS(-10)              # Go to position -10 mm
time.sleep(2)                   # Wait 2 seconds
axisA.setDPOS(0)                # Go to position 0 mm
time.sleep(2)                   # Wait 2 seconds

axisB.setDPOS(10)               # Go to position 10 mm
time.sleep(2)                   # Wait 2 seconds
axisB.setSpeed(200)             # Set speed to 200 mm/s
axisB.setDPOS(-10)              # Go to position -10 mm
time.sleep(2)                   # Wait 2 seconds
axisB.setDPOS(0)                # Go to position 0 mm
time.sleep(2)                   # Wait 2 seconds

axisC.setDPOS(10)               # Go to position 10 mm
time.sleep(2)                   # Wait 2 seconds
axisC.setSpeed(200)             # Set speed to 200 mm/s
axisC.setDPOS(-10)              # Go to position -10 mm
time.sleep(2)                   # Wait 2 seconds
axisC.setDPOS(0)                # Go to position 0 mm
time.sleep(2)                   # Wait 2 seconds

for _ in range(0,10):           # Step 10 x 1 mm
    axisA.step(1)               # Step 1 mm
    time.sleep(0.5)             # Wait 0.5 seconds
time.sleep(2)                   # Wait 2 seconds

for _ in range(0,10):           # Step 10 x 1 mm
    axisB.step(1)               # Step 1 mm
    time.sleep(0.5)             # Wait 0.5 seconds
time.sleep(2)                   # Wait 2 seconds

for _ in range(0,10):           # Step 10 x 1 mm
    axisC.step(1)               # Step 1 mm
    time.sleep(0.5)             # Wait 0.5 seconds
time.sleep(2)                   # Wait 2 seconds

axisA.setUnits(Units.mu)        # Set units to mu
axisB.setUnits(Units.mu)        # Set units to mu
axisC.setUnits(Units.mu)        # Set units to mu

axisA.setDPOS(-10000)           # Go to position -10000 mu
axisB.setDPOS(-10000)           # Go to position -10000 mu
axisC.setDPOS(-10000)           # Go to position -10000 mu

time.sleep(2)                   # Wait 2 seconds

print("Bit  0 = ", axisA.isAmplifiersEnabled())         # Check bit 0
print("Bit  1 = ", axisA.isEndStop())                   # Check bit 1
print("Bit  2 = ", axisA.isThermalProtection1())        # Check bit 2
print("Bit  3 = ", axisA.isThermalProtection2())        # Check bit 3
print("Bit  4 = ", axisA.isForceZero())                 # Check bit 4
print("Bit  5 = ", axisA.isMotorOn())                   # Check bit 5
print("Bit  6 = ", axisA.isClosedLoop())                # Check bit 6
print("Bit  7 = ", axisA.isEncoderAtIndex())            # Check bit 7
print("Bit  8 = ", axisA.isEncoderValid())              # Check bit 8
print("Bit  9 = ", axisA.isSearchingIndex())            # Check bit 9
print("Bit 10 = ", axisA.isPositionReached())           # Check bit 10
print("Bit 11 = ", axisA.isErrorCompensation())         # Check bit 11
print("Bit 12 = ", axisA.isEncoderError())              # Check bit 12
print("Bit 13 = ", axisA.isScanning())                  # Check bit 13
print("Bit 14 = ", axisA.isAtLeftEnd())                 # Check bit 14
print("Bit 15 = ", axisA.isAtRightEnd())                # Check bit 15
print("Bit 16 = ", axisA.isErrorLimit())                # Check bit 16
print("Bit 17 = ", axisA.isSearchingOptimalFrequency()) # Check bit 17
print("Bit 18 = ", axisA.isSafetyTimeoutTriggered())    # Check bit 18
print("Bit 19 = ", axisA.isEtherCatAcknowledge())       # Check bit 19
print("Bit 20 = ", axisA.isEmergencyStop())             # Check bit 20
print("Bit 21 = ", axisA.isPositionFailTriggered())     # Check bit 21

logs = axisA.endLogging()   # Stop logging
print(logs)                 # Print logs

epos_a_raw = logs["EPOS"][0::3]
epos_b_raw = logs["EPOS"][1::3]
epos_c_raw = logs["EPOS"][2::3]

# Convert encoder units to units for each axis
epos_a = [axisA.convertEncoderUnitsToUnits(v, axisA.units) for v in epos_a_raw]
epos_b = [axisB.convertEncoderUnitsToUnits(v, axisB.units) for v in epos_b_raw]
epos_c = [axisC.convertEncoderUnitsToUnits(v, axisC.units) for v in epos_c_raw]

plt.plot(epos_a, label='Axis A (' + str(axisA.units) + ')')
plt.plot(epos_b, label='Axis B (' + str(axisB.units) + ')')
plt.plot(epos_c, label='Axis C (' + str(axisC.units) + ')')

plt.ylabel('EPOS')
plt.xlabel("Sample")
plt.title("EPOS - All Axes")
plt.legend()
plt.show()

controller.stop()