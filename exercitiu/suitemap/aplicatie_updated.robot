*** Settings ***
Library    SeleniumLibrary
Library    practice_form.PracticeForm    WITH NAME    pf

*** Variables ***
@{subjects}    Maths    Physics    Computer Science
@{hobbies}    Sports    Music
&{d}    Name=Cosmin T    Email=cturigioiu@email.com    Gender=Male    Mobile=1231231231    Date of Birth=01 Jan 1990    Subjects=${subjects}    Hobbies=${hobbies}    Current Address=Adresa curenta    State and City=NCR Delhi

*** Test Cases ***

Test
    Log    Testing Form
    Form Fill ${d}
    Form Submit
    ${status}    Form Verify ${d}
    Should Be True    ${status}        
    Log    Test Completed

