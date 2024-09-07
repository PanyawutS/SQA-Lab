*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${SERVER}         localhost:7272
${BROWSER}        Firefox
${DELAY}          0
${URL}            http://${SERVER}/
${REGISTER URL}   http://${SERVER}/Lab12/Registration.html
${SUCCESS URL}    http://${SERVER}/Lab12/Success.html

*** Keywords ***
Open Browser To Registration Page
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

Go To Registration Page
    Go To    ${REGISTER URL}
    Registration Page Should Be Open

Registration Page Should Be Open
    Title Should Be    Event Registration

Wait For First Name Field
    Wait Until Element Is Visible    id=firstname    timeout=10s

Input Registration Details
    [Arguments]    ${firstName}    ${lastName}    ${organization}    ${email}    ${phone}
    Wait For First Name Field
    Input Text    id=firstname    ${firstName}
    Input Text    id=lastname    ${lastName}
    Run Keyword If    '${organization}' != '${EMPTY}'    Input Text    id=organization    ${organization}
    Input Text    id=email    ${email}
    Input Text    id=phone    ${phone}

Submit Registration
    Click Button    id=registerButton

Registration Success Page Should Be Open
    ${current_url}=    Get Location
    Should Start With    ${current_url}    ${SUCCESS URL}
    Title Should Be    Success
    Page Should Contain    Thank you for participating in our event

Error Message Should Be Shown
    [Arguments]    ${message}
    Page Should Contain    ${message}


