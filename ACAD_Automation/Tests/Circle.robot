*** Settings ***
Library    AutoCAD.py

*** Test Cases ***

Draw Circle
    [Documentation]    Open AutoCAD, draw a Circle, and close the application.
    ChangeResoultion
    Open AutoCAD    C:\\Program Files\\Autodesk\\AutoCAD 2026\\acad.exe
    Sleep      8s
    Click at Coordinates    118    162 
    Sleep      5s       
    Draw Circle       0,0    20
    Sleep      5s
    Zoom Extent    z   e
    Sleep      5s
    Close Autocad