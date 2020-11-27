# INTRO
Fork from prenagha/snooze.mmbundle

Just adapting a few things to meet my needs. In particular:

# Features

* Using tag "$snoozed" instead of the "Later" IMAP-Folder. This allows me to keep my folders organized as I wish; and to snooze sent mail (which I like to keep in the "Sent"-Folder

* Picker-Dialogue 
  * Shows entry options
  * Can by Cancelled voa Escape-Key and Cancel Button

* Picker Dialogue allows:
  * Snooze for days (1d, 5d, ...), weeks (1w, 3w) and months (1m, 2m, ...)
  * Snooze until next weekday (mon, tue, wed, ..., sun)
  * Snooze until tomorrow (tom)
  * Snooze until date (2020-22-10, 2030-05-03, ...)
  * Unsnooze (xx)

* Option to unsnooze mail. This removes the $snoozed-Tag as well as the "x-snooze"-header (However Original-x-snoozed header remains)

* Key shortcuts
  * ^z: show snooze dialogue
  * ^Z: unsnooze

# Installation
1. Set up python on your mac
2. Download or Clone repo
3. Copy or link the repo to your `mailmate/bundles` directory.
4. Start Mailmate. "Snooze" should by in the Command menu

## example
```bash
  $ cd my/path/to/the/repo/
  $ git clone ...
  $ cd /Users/XXXX/Library/Application Support/MailMate/Bundles
  $ ln -s enisnooze.mmbundle -> my/path/to/the/repo/enisnooze.mmbundle/
```

# CONFIG

## Highlight snoozed messages in list view
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

## Create smart folder to view scheduled mail by date
Create a smart folder like this:

* **Mailboxes:** Pick one Mailbox. I use one Account per smart folder (see issue below).
* **Conditions:** Tags/Keywords include "$snoozed"
* **Submailbox for each unique value of:** x-Snooze   (you may need to snooze an email before this option shows up)

DO NOT USE THE OPTION `Submailbox for the messages of each account`. 
It seems Mailmate has a bug here. When using the option, MailMate won't refreshing the folders properly when changing snooze times. 



