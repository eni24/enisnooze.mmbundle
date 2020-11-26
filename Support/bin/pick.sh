#!/bin/bash

DEF=`1d"`
osascript <<END
tell application "System Events"
	activate
	set theDate to the text returned of (display dialog "Enter Snooze time. Options are:\n- <N>d: <N>days\n- <N>w: <N>weeks\n- <N>m: <N>months\n- yyyy-mm-dd \n- mon, tue, ..., sun" default answer "${DEF}" with title "Snooze Message" buttons {"Cancel", "Snooze"} default button "Snooze" cancel button "Cancel")
	return theDate
end tell
END