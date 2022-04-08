# Login to a remote SSH server 
New-SSHSession -ComputerName '192.168.6.71' -Credential (Get-Credential 'john.tiseo@cyber.local') -Port '2222'


while ($True)    
{
    # Add a prompt to run commands 
    $the_cmd = read-host -Prompt "Please enter a command. "

    # Run command on a remote SSH server
    (Invoke-SSHCommand -index 0 $the_cmd).Output
}

# Upload a file to the remote system
Set-SCPItem -ComputerName '192.168.6.71' -Credential (Get-Credential 'john.tiseo@cyber.local') -Path 'C:\Users\jtiseo\Desktop\test.txt' -Destination '/home/john.tiseo/' -Port '2222'


