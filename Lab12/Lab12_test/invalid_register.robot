*** Settings ***
Documentation     Test cases for failed event registrations due to invalid inputs.
Resource          Resource.robot
Suite Setup       Open Browser To Registration Page
Suite Teardown    Close Browser
Test Setup        Go To Registration Page

*** Test Cases ***
Missing First Name
    [Documentation]    ทดสอบเมื่อไม่ได้กรอกชื่อ
    Go To Registration Page
    Input Registration Details    ${EMPTY}    Sodsai    CS KKU    somsri@kkumail.com    081-001-1234
    Submit Registration
    Error Message Should Be Shown    *Please enter your first name!!

Missing Last Name
    [Documentation]    ทดสอบเมื่อไม่ได้กรอกนามสกุล
    Go To Registration Page
    Input Registration Details    Somsri    ${EMPTY}    CS KKU    somsri@kkumail.com    081-001-1234
    Submit Registration
    Error Message Should Be Shown    *Please enter your last name!!

Missing Name
    [Documentation]    ทดสอบเมื่อไม่ได้กรอกชื่อ-นามสกุล
    Go To Registration Page
    Input Registration Details    ${EMPTY}    ${EMPTY}    CS KKU    somsri@kkumail.com    081-001-1234
    Submit Registration
    Error Message Should Be Shown    *Please enter your name!!

Missing E-mail
    [Documentation]    ทดสอบเมื่อไม่ได้กรอกอีเมล
    Go To Registration Page
    Input Registration Details    Somsri    Sodsai    CS KKU    ${EMPTY}    081-001-1234
    Submit Registration
    Error Message Should Be Shown    *Please enter your email!!

Empty Phone Number
    [Documentation]    ทดสอบเมื่อไม่ได้กรอกเบอร์โทร
    Go To Registration Page
    Input Registration Details    Somsri    Sodsai    CS KKU    somsri@kkumail.com    ${EMPTY}
    Submit Registration
    Error Message Should Be Shown    Please enter your phone number!!

Invalid Phone Number
    [Documentation]    ทดสอบเมื่อกรอกเบอร์โทรไม่ถูกต้อง
    Go To Registration Page
    Input Registration Details    Somsri    Sodsai    CS KKU    somsri@kkumail.com    1234
    Submit Registration
    Error Message Should Be Shown    Please enter a valid phone number!!, e.g., 081-234-5678, 081 234 5678, or 081.234.5678


