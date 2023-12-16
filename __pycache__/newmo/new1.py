# import datetime
# a=datetime.datetime.now()
# print('datetime:',a)
# import platform,os ,getpass
# a=platform.system()
# print('operating system:',a)
# print('architecture:',platform.architecture())
# print('processor:',platform.processor())
# print('username:',getpass.getuser())
import platform

my_system = platform.uname()

print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")
