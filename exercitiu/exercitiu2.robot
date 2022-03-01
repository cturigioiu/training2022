*** Settings ***
Library    SeleniumLibrary
Suite Setup    SuiteSetup
Suite Teardown    SuiteTeardown

*** Keywords ***

SuiteSetup
    Log    Suite setup started
    Open Browser    https://demoqa.com/    chrome
    Scroll Element Into View    xpath://h5[contains(text(),'Book Store Application')]
    Click Element    xpath://h5[contains(text(),'Forms')]
    Log    Suite setup ended
    
SuiteTeardown
    Log    Suite teardown started
    Close Browser
    Log    Suite setup ended

Fill Text
    [Arguments]    ${locator}    ${data} 
    Press Keys    ${locator}    CTRL+A    ${data}    
    Press Keys    ${locator}    ESCAPE
    
Fill List
    [Arguments]    ${locator}    ${data}
    FOR    ${element}    IN    @{data}
        Press Keys    ${locator}    ${element}
        Press Keys    ${locator}    RETURN
    END 
    
Fill Text Triage
    [Arguments]    ${locator}    ${data} 
    ${ariaAutoComplete}    Get Element Attribute    ${locator}    ariaAutoComplete
    Run Keyword If    "${ariaAutoComplete}"!="list"    Fill Text    ${locator}    ${data}
    Run Keyword If    "${ariaAutoComplete}"=="list"    Fill List    ${locator}    ${data}
        
Fill File
    [Arguments]    ${locator}    ${data} 
    Choose File    ${locator}    ${data}
    
Fill Textarea
    [Arguments]    ${locator}    ${data} 
    Press Keys    ${locator}    ${data}
    
Fill None
    [Arguments]    ${locator}    ${data} 
    Click Element    xpath://*[@id='${locator}']//label[@value='${data}' or contains(text(),'${data}')]        
    
Get Input Type
    [Arguments]    ${locator}
    Log    Get type for ${locator}
    ${type}    Get Element Attribute    id=${locator}    type
    Log    Got type: ${type}
    [Return]    ${type}
    
Fill Data
    [Arguments]    ${locator}    ${data}  
    ${type}    Get Input Type    ${locator}
    Log    Filling ${data} in ${type} input
    Run Keyword If    "${type}"=="text"    Fill Text Triage    ${locator}    ${data}
    Run Keyword If    "${type}"=="textarea"    Fill Textarea    ${locator}    ${data}
    Run Keyword If    "${type}"=="file"    Fill File    ${locator}    ${data}
    Run Keyword If    "${type}"=="None"    Fill None    ${locator}    ${data}

Fill In Props
    [Arguments]    &{dict}
    Log    Filling form
    Sleep    1
    FOR    ${pair}    IN    &{dict}
        Fill Data    ${pair}[0]    ${pair}[1]
    END
    
*** Variables ***
@{subjects}    Maths    Physics    Computer Science
&{fill_data}    firstName=Cosmin    lastName=T    userEmail=tcosmin@email.com    genterWrapper=Male    userNumber=1231231231    dateOfBirthInput=01 jan 1990    subjectsInput=${subjects}    hobbiesWrapper=Sports    uploadPicture=C:\\Users\\CTurigioiu-Duran\\Pictures\\Capture.PNG    currentAddress=address

*** Test Cases ***

WebTablesTest
    Log    Testing Form
    Click Element    xpath://span[contains(text(),'Practice Form')]
    Press Keys    xpath://body    PAGE_DOWN
    Fill In Props    &{fill_data}
    
    SLEEp    5
    Log    Test completed
