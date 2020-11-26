#!/bin/bash

DEF=`date -v+1d "+%Y-%m-%d"`
osascript <<END
tell application "System Events"
	activate
	set theDate to the text returned of (display dialog "Snooze until yyyy-mm-dd?" default answer "${DEF}" with title "Snooze Message -- Pick Date" buttons {"Snooze"} default button 1)
	return theDate
end tell
END