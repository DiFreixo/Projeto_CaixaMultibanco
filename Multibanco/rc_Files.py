# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.6.1
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x00\x94\
\xef\
\xbb\xbfConta;00012345\
6789;;;;\x0d\x0aClient\
e;Maria dos Sant\
os;;;;\x0d\x0aNIB;1234\
4321123456700000\
0;;;;\x0d\x0aIBAN;PT50\
1234432112345678\
90172;;;;\x0d\x0aSWIFT\
/BIC;BANCXXYY;;;\
;\x0d\x0a\
"

qt_resource_name = b"\
\x00\x03\
\x00\x00H\x86\
\x00C\
\x00S\x00V\
\x00\x11\
\x0f=\xd1\xa6\
\x00C\
\x00o\x00n\x00s\x00u\x00l\x00t\x00a\x00r\x00I\x00B\x00A\x00N\x00.\x00c\x00s\x00v\
\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x8d\xb2\xd3\xb0\x97\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
