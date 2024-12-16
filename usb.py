# Пример использования pyUSB для USB:
import usb.core
import usb.util

# Поиск устройства
## dev = usb.core.find(idVendor=0xXXXX, idProduct=0xYYYY)

# Проверка на наличие устройства
if dev is None:
    raise ValueError('Device not found')

# Настройка устройства
dev.set_configuration()

# Чтение данных
data = dev.read(0x81, 64)  # Чтение 64 байт из endpoint 0x81
print(data)
# Эти библиотеки и примеры помогут вам начать работу с различными интерфейсами в Python.
# usb

# pyUSB: Библиотека для работы с USB-устройствами. Она позволяет взаимодействовать с USB-устройствами на различных платформах.

# pip install pyusb
# libusb1: Это обертка для libusb, которая позволяет работать с USB-устройствами. Подходит для более низкоуровневого доступа.

# pip install libusb1
# PyUSB1: Это еще одна библиотека для работы с USB, которая предоставляет удобный интерфейс для взаимодействия с USB-устройствами.

# pip install pyusb1
