*** Settings ***
Library    SeleniumLibrary
Suite Setup    SuiteSetup
Suite Teardown    SuiteTeardown

*** Keywords ***

SuiteSetup
    Log    Suite setup started
    Open Browser    https://demoqa.com/    chrome
    Click Element    xpath://h5[contains(text(),'Elements')]
    Log    Suite setup ended
    
SuiteTeardown
    Log    Suite teardown started
    Close Browser
    Log    Suite setup ended
    
*** Variables ***
${firstName}    Cosmin
${lastName}    T
${email}    tcosmin@email.com
${age}    24
${salary}    0
${department}    IT


*** Test Cases ***
TextBoxTest
    Log    Testing Text Box
    Click Element    xpath://span[contains(text(),'Text Box')]    
    Input Text    id=userName    Nume    
    Input Text    id=userEmail    Email@email.com
    Input Text    id=currentAddress    AdresaCrt
    Input Text    id=permanentAddress    AdresaPerm
    Click Element    id=submit  
    Element Should Be Visible    id=output    
    Log    Test completed 

CheckBoxTest
    Log    Testing Check Box
    Click Element    xpath://span[contains(text(),'Check Box')]
    Wait Until Element Is Visible    xpath://span[contains(text(),'Home')]    
    Click Element    xpath://span[contains(text(),'Home')]    
    Element Should Be Visible    id=result         
    Log    Test completed
    
RadioButtonTest
    Log    Testing Radio Button
    Click Element    xpath://span[contains(text(),'Radio Button')]
    Click Element    xpath://label[contains(text(),'Yes')]
    Element Should Be Visible    xpath://span[@class='text-success']
    ${content}    Get Text    xpath://span[@class='text-success']
    Should Be Equal As Strings    ${content}    Yes             
    Log    Test completed

WebTablesTest
    Log    Testing Web Tables
    Click Element    xpath://span[contains(text(),'Web Tables')]
    Click Element    id=addNewRecordButton
    Input Text    id=firstName    ${firstName}
    Input Text    id=lastName    ${lastName}
    Input Text    id=userEmail    ${email}
    Input Text    id=age    ${age}
    Input Text    id=salary    ${salary}
    Input Text    id=department    ${department}
    Click Element    id=submit
    @{row_list}    Get WebElements    xpath://div[@class='rt-tr-group']
    FOR    ${row}    IN    @{row_list}
        ${row_data}    Get Element Attribute    ${row}    innerHTML
        ${result}    Evaluate    '${firstName}' in '''${row_data}'''
        Pass Execution If    ${result}    New entry was succesfully found
    END
    Log    Test completed
    
ButtonsTest
    Log    Testing Buttons
    Click Element    xpath://span[contains(text(),'Buttons')]
    Double Click Element    id=doubleClickBtn
    Element Should Be Visible    id=doubleClickMessage
    Open Context Menu    id=rightClickBtn
    Element Should Be Visible    id=rightClickMessage
    Click Element    xpath://button[contains(text(),'Click Me') and not(contains(text(),' Click Me'))]
    Element Should Be Visible    id=dynamicClickMessage
    Log    Test completed
    
LinksTest
    Log    Testing Links
    Click Element    xpath://span[contains(text(),'Links')]
    
    Log    Testing Simple Link
    Click Link    id=simpleLink
    ${handles}    Get Window Handles
    Switch Window      ${handles}[1]
    Element Should Be Visible    xpath://img[@class='banner-image']
    Close Window
    Switch Window      ${handles}[0]
    
    Log    Testing Dynamic Link
    Click Link    id=dynamicLink
    ${handles}    Get Window Handles
    Switch Window      ${handles}[1]
    Element Should Be Visible    xpath://img[@class='banner-image']
    Close Window
    Switch Window      ${handles}[0]
    Log    Test completed
    
DownloadAndUploadTest
    Log    Testing Download and Upload
    Click Element    xpath://span[contains(text(),'Upload and Download')]
    Choose File    id=uploadFile    D:\\Capture.PNG
    Click Link    id=downloadButton   
    Log    Test completed
  
    
