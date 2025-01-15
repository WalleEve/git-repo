# The os Module

"""
The os modules has many uses.
Where we will be covering the followings:
os.name
os.environ
os.chdir()
os.getcwd()
os.getenv()
os.putenv()
os.mkdir()
os.makedirs()
os.remove()
os.rename()
or.rmdir()
os.startfile()
os.walk()
os.path

"""

# To use any of the methods mentioned in this section,
# we will need to import the os module.

import os

# os.name
"""
The os module has both callable functions and normal values.
In the case of os.name, it is just a value.
When we access os.name we will get imformation about what platform we are running on.
We will receive one of the following values: 'posix', 'nt', 'os2', 'java', 'riscos'
"""

print(os.name)
# output: nt


# os.environ, os.getenv(), and os.putenv()
"""
The os.environ value is known as a mapping object that returns a directory of the user's
environment variable, we may not know this, but every time we use our computer, some
environment variable are set. These can give us valuable information, such as number of
processors, type of CPU, the computer name etc,
"""

print(os.environ)

# Output
"""
environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\sayed\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'SAYED', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'EFC_11132': '1', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\sayed', 'LOCALAPPDATA': 'C:\\Users\\sayed\\AppData\\Local', 'LOGONSERVER': '\\\\SAYED', 'NUMBER_OF_PROCESSORS': '12', 'ONEDRIVE': 'C:\\Users\\sayed\\OneDrive', 'ONEDRIVECONSUMER': 'C:\\Users\\sayed\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'C:\\app\\sayed\\product\\21c\\dbhomeXE\\bin;C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Git\\cmd;C:\\Users\\sayed\\AppData\\Local\\Programs\\Python\\Python38-32\\Scripts\\;C:\\Users\\sayed\\AppData\\Local\\Programs\\Python\\Python38-32\\;C:\\Users\\sayed\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1.1\\bin;C:\\Users\\sayed\\AppData\\Local\\atom\\bin;C:\\Users\\sayed\\AppData\\Local\\Programs\\Microsoft VS Code\\bin', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'x86', 'PROCESSOR_ARCHITEW6432': 'AMD64', 'PROCESSOR_IDENTIFIER': 'AMD64 Family 23 Model 96 Stepping 1, AuthenticAMD', 'PROCESSOR_LEVEL': '23', 'PROCESSOR_REVISION': '6001', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files (x86)', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PROMPT': '$P$G', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM COMMUNITY EDITION': 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1.1\\bin;', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\sayed\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\sayed\\AppData\\Local\\Temp', 'USERDOMAIN': 'SAYED', 'USERDOMAIN_ROAMINGPROFILE': 'SAYED', 'USERNAME': 'sayed', 'USERPROFILE': 'C:\\Users\\sayed', 'VBOX_MSI_INSTALL_PATH': 'C:\\Program Files\\Oracle\\VirtualBox\\', 'WINDIR': 'C:\\WINDOWS'})
"""
# We can access the environmental variable using our mormal dictionary methods.
print(os.environ["TMP"])

# we could also use the os.getenv function to access this environment variable.

print(os.getenv("TMP"))

"""
The benefit of using os.getenv() instead od the os.environ dictionary is that of
we happen to try to access an environment variable that doesn't exists, the getenv will just return None.
If we did the same thing with os.environ, we would receive an error.
"""
