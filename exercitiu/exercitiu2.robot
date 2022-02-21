*** Settings ***
Library    SeleniumLibrary
Suite Setup    SuiteSetup
Suite Teardown    SuiteTeardown

*** Keywords ***

SuiteSetup
    Log    Suite setup started
    Open Browser    https://demoqa.com/    chrome
    Click Element    xpath://h5[contains(text(),'Forms')]
    Log    Suite setup ended
    
SuiteTeardown
    Log    Suite teardown started
    Close Browser
    Log    Suite setup ended
    
*** Variables ***
${firstName}    Cosmin
${lastName}    T
${email}    tcosmin@email.com
${gender}    Male
${mobile_no}    1231231231
${dob}    01 jan 1990
@{subjects}    Maths    Physics    Computer    Science
@{hobbies}    Sports
${filename}    D:\\Capture.PNG
${current_address}    address
${state}    NCR
${city}    Noida

*** Test Cases ***

WebTablesTest
    Log    Testing Form
    Click Element    xpath://span[contains(text(),'Practice Form')]

    Input Text    id=firstName    ${firstName}
    Input Text    id=lastName    ${lastName}
    Input Text    id=userEmail    ${email}
    
    Click Element    xpath://label[contains(text(),'${gender}')]  
    
    Input Text    id=userNumber    ${mobile_no}   
    
    Execute Javascript    document.getElementById('dateOfBirthInput').value = "${dob}";
    
    FOR    ${subject}    IN    @{subjects}
        Input Text    id=subjectsInput    ${subject}
        Press Keys    id=subjectsInput    TAB
    END
    
    FOR    ${hobbie}    IN    @{hobbies}
        Click Element    xpath://label[contains(text(),'${hobbie}')]
    END

    Choose File    id=uploadPicture    ${filename}

    Input Text    id=currentAddress    ${current_address}
    
    Input Text    xpath://div[@id='state']//input    ${state}
    Press Keys    xpath://div[@id='state']//input    TAB
    
    Input Text    xpath://div[@id='city']//input    ${city}
    Press Keys    xpath://div[@id='city']//input    TAB
    
    Press Keys    id=currentAddress    PAGE_DOWN
    Sleep    0.5
    Click Button    id=submit    
    
    @{row_list}    Get WebElements    xpath://tbody//tr
    
    FOR    ${row}    IN    @{row_list}
        ${row_data}    Get Element Attribute    ${row}    innerHTML
        Evaluate    '${firstName}' in '''${row_data}''' or '${email}' in '''${row_data}'''
    END

    Log    Test completed
