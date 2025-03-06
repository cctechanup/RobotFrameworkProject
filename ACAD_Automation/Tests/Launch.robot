*** Settings ***
Library    AutoCAD.py

*** Variables ***
${AUTOCAD_PATH}      C:\\Program Files\\Autodesk\\AutoCAD 2026\\acad.exe
${BASELINE_IMAGE}    C:\\ROBOTFramework\\ACAD_Automation\\Baseline.png
${ACTUAL_IMAGE}      C:\\ROBOTFramework\\ACAD_Automation\\actual.png

*** Test Cases ***
Draw Line in AutoCAD
    [Documentation]    Open AutoCAD, draw a line, and verify using image comparison.
    Setup AutoCAD Environment
    Draw and Verify Line
    Teardown AutoCAD

*** Keywords ***
Setup AutoCAD Environment
    Change Resoultion
    Open AutoCAD    ${AUTOCAD_PATH}
    Sleep    5s
    Resize AutoCAD
    Select Drawing Tool
    
Select Drawing Tool
    Click at Coordinates    118    162 
    Sleep    3s
    
Draw and Verify Line
    Draw Line    0,0    100,100
    Sleep     3s
    Zoom Extent    z    e
    Capture and Compare Drawing

Capture and Compare Drawing
    Capture Region    0    0    960    900    ${ACTUAL_IMAGE}
    ${result}=    Compare Images    ${BASELINE_IMAGE}    ${ACTUAL_IMAGE}
    Should Be True    ${result} <= 5    Image Comparision failed!

Teardown AutoCAD
    Close AutoCAD






    
