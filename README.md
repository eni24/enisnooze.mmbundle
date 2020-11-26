# INTRO
Fork from prenagha/snooze.mmbundle

Just adapting a few things to meet my needs. In particular:

# Requirements

**TODO** 
* Add option to unsnooze mail
    * remove $snoozed-Tag
    * (Optional) remove the "x-snooze"-header.

* Confirmation Dialogue before UNSNOOZE

**DONE**

* Use tag "$snoozed" instead of the "Later" IMAP-Folder. This allows me to keep my folders organized and also snooze sent mail (which I like to keep in the "Sent"-Folder

* Add option to Cancel the Picker-Dialogue => (via Cancel Button and ESCAPE-Key)

# Bugs

* I view all my snoozed email in a smart folder plus subfolders for each snooze date. Unfortunately, when changing the snooze date, the mail remains visible in the old folder. This is only corrected after MM restarts. 

* Exact month timespec calculation

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
