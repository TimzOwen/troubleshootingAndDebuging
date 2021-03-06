# Meeting email reminder
# Fix the issue of some meetings not working

meeting_info = $(zenity --forms\
    --title 'Meeting'--text 'Reminder information'\
    --add-calender 'Date' --add-entry 'Title' \
    --add-entry 'Emails'\
    2>/dev/null)
echo $meeting_info
if [[ -n "$meeting_info" ]]; then
    python3 send_reminders.py "meeting info"
fi
