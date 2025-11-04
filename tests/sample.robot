*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    ${BROWSER}
${URL}        ${URL}

*** Test Cases ***
Open URL
    [Arguments]    ${URL}    ${BROWSER}
    Open Browser    ${URL}    ${BROWSER}
    Capture Page Screenshot
    Close Browser
