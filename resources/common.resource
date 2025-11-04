*** Settings ***
# Put shared resources, variables, and keywords here for reuse by tests.

*** Variables ***
${DEFAULT_BROWSER}    chrome
${DEFAULT_URL}        https://example.com

*** Keywords ***
Open Example In Default Browser
    [Arguments]    ${url}=${DEFAULT_URL}    ${browser}=${DEFAULT_BROWSER}
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

Close Browser If Open
    Run Keyword And Ignore Error    Close Browser

# Notes:
# - Move locators and common keywords into this file as your suite grows.
# - Use resource files for Page Object-like separation: one resource per page or component.
