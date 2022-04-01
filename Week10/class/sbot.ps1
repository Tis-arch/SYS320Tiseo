#Send an e-mail using powershell

#Array to hold e-mail to spam
$toSend = @('john.tiseo@mymail.champlain.edu', 'tiseo@mymail.champlain.edu', 'john@mymail.champlain.edu')
# Message Body 
$msg = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
while ($true) 
{
    foreach ($email in $toSend) 
    {
        # Send the email 
        write-host "Send-MailMessage - from 'john.tiseo@mymail.champlain.edu' -To $email -Subject 'HOT SINGLES IN YOUR AREA'`
        -Body $msg -SmtpServer X.X.X.X"
        # Pause for one second
        # start-sleep 1
    }
}