import usb.core
import usb.util

scarlet = usb.core.find(idVendor = 0x1235)  # Focusrite
if not scarlet: 
    print("No Scarlet")

c = 1
for config in scarlet:
    print('config'), c
    print('Interfaces'), config.bNumInterfaces
    for i in range(config.bNumInterfaces):
        if scarlet.is_kernel_driver_active(i):
            scarlet.detach_kernel_driver(i)
        print(i)
    c+=1

scarlet.set_configuration()
