# INTRO
Fork from prenagha/snooze.mmbundle

Just adapting a few things to meet my needs. In particular:

# Requirements

**TODO** 

* Confirmation Dialogue before UNSNOOZE

**DONE**

* Use tag "$snoozed" instead of the "Later" IMAP-Folder. This allows me to keep my folders organized and also snooze sent mail (which I like to keep in the "Sent"-Folder

* Add option to Cancel the Picker-Dialogue => (via Cancel Button and ESCAPE-Key)

* Add option to unsnooze mail
    * remove $snoozed-Tag => DONE
    * (Optional) remove the "x-snooze"-header. => DONE. However Original-x-snoozed header remains

* Allow 'xx' to unsnooze email

# Bugs

### Open
* Exact month timespec calculation

### Fixed

* I view all my snoozed email in a smart folder plus subfolders for each snooze date. Unfortunately, when changing the snooze date, the mail remains visible in the old folder. This is only corrected after MM restarts. 

  => Seems to be a bug in MailMate subfolders. Workaround: Do not use the smartfolder checkbox `Submailbox for the messages of each account` 


# CONFIG

To highlight snoozed messages in list view add this to `Styles.plist`:
```javascript
{   styles = 
    (
        {   type = keyword;
            keyword = '$snoozed';
            color = "#6060D0";
        },
	);
}
```

*(My `Styles.plist` is in `~/Library/Application Support/MailMate/`)*
