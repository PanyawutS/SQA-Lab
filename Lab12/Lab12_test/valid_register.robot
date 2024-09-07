*** Settings ***
Documentation     Test cases for successful event registrations.
Resource          Resource.robot
Suite Setup       Open Browser To Registration Page
Suite Teardown    Close Browser
Test Setup        Go To Registration Page

*** Test Cases ***
Valid Registration
    [Documentation]    ทดสอบการลงทะเบียนด้วยข้อมูลที่ถูกต้อง
    Go To Registration Page
    Input Registration Details    Somsri    Sodsai    CS KKU    somsri@kkumail.com    081-001-1234
    Submit Registration
    Registration Success Page Should Be Open

Valid Registration Without Organization
    [Documentation]    ทดสอบการลงทะเบียนโดยไม่กรอกชื่อองค์กร
    Go To Registration Page
    Input Registration Details    Somsri    Sodsai    ${EMPTY}   somsri@kkumail.com    081-001-1234
    Submit Registration
    Registration Success Page Should Be Open

