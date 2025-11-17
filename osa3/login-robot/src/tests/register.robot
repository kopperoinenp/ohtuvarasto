*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  validi  validi123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  validi  validi123
    Input New Command
    Input Credentials  validi  validi123
    Output Should Contain  Username already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  va  validi123
    Output Should Contain  Username too short

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input Credentials  völidi1  validi123
    Output Should Contain  Username must contain only letters a-z

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  validi  validi1
    Output Should Contain  Password must be over 8 characters and contain something other than a letter

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  validi  validiii
    Output Should Contain  Password must be over 8 characters and contain something other than a letter