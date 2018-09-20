# applestoreinventory
Python Script to lookup inventory for any Apple part number by zip code

# Requirements
## macOS
### Install PIP
`sudo easy_install pip`

### Install requests
`sudo pip install requests`

## iOS
Purchase [Pythonista](http://omz-software.com/pythonista/) 

## Script
Simply modify the following line in the script

`get_status("AirPods",  "MMEF2AM/A", "95014")`

## Output
If everything works you should see this
```
==========================================
Checking AirPods 95014
==========================================
Infinite Loop       :            available
Apple Park          :            available
Valley Fair         :            available
Los Gatos           :            available
Oakridge            :            available
Palo Alto           :            available
Stanford            :            available
Hillsdale           :            available
Burlingame          :            available
Stoneridge Mall     :            available
Stonestown          :            available
Union Square        :            available
```
