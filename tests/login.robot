*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}     https://example.com
${BROWSER}    chrome

*** Test Cases ***
Open Example And Check Title
    Open Browser    ${URL}    ${BROWSER}
    Title Should Be    Example Domain
    Close Browser
