#
# VGA Control ROM generator
#

from numpy import uint8

Hsync  = uint8(1) << 7
Vsync  = uint8(1) << 6
Reset590 = uint8(1) << 5
Reset4040 = uint8(1) << 4
Red = uint8(1) << 2
Green = uint8(1) << 1
Blue = uint8(1) << 0

control: uint8 = [0 for _ in range(1 << 17)]

for addr in range(26250):
    x = addr % 50
    y = addr // 50
    if x < 41 or x > 47:
        control[addr] |= Hsync
    if y < 490 or y > 492:
        control[addr] |= Vsync
    if x < 40 and y < 480:
        control[addr] |= x & 0x07
    if addr == 26249:
        control[addr] |= Reset4040
    else:
        control[addr] |= Reset590
    print(addr, x, y, bin(control[addr]))

control_bytes = bytearray(control)
control_bin = open("control.bin", "wb")
control_bin.write(control_bytes)
control_bin.close()
