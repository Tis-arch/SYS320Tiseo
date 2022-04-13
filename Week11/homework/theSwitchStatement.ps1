<#
    This script will grab the ip addresses from two threat intel reports and save the list in a temporary file.
    Then, this program will get user input to generate either Windows Firewall rules or IPTables rules that block these addresses.
    If IPTables is selected, then it will also SCP the file over to the remote server.
#>

# Array of websites containing threat intel
$drop_urls = @('https://rules.emergingthreats.net/blockrules/emerging-botcc.rules','https://rules.emergingthreats.net/blockrules/compromised-ips.txt')

# Loop through the URLs for the rules list
foreach ($u in $drop_urls) {
    
    # Extract the filename
    $temp = $u.Split("/")
    
    # The last element in the array plucked off is the filename
    $file_name = $temp[-1]

    # If the file is already downloaded, don't download it again 
    if (Test-Path $file_name)
    {
        continue
    }
    else 
    {
        # Download the rules list
        Invoke-WebRequest -Uri $u -OutFile $file_name
    }
}

# Array containg the filename
$input_paths = @('C:\Users\johnt\Documents\GitHub\SYS320Tiseo\Week11\homework\compromised-ips.txt','C:\Users\johnt\Documents\GitHub\SYS320Tiseo\Week11\homework\emerging-botcc.rules')
# Extract the IP Addreses
$regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

# Append the IP addresses to the temporary IP list
Select-String -Path $input_paths -Pattern $regex_drop | `
ForEach-Object { $_.Matches } | `
ForEach-Object { $_.Value }  | Sort-Object | Get-Unique | `
Out-File -FilePath "C:\Users\johnt\Documents\GitHub\SYS320Tiseo\Week11\homework\ips-bad.tmp"



# Get user input and store it in the $var varaible 
$var = Read-host -Prompt "Please enter Windows or IPTables: "

# The switch statement, the user has to enter either Windows or IPTables 
switch ($var)
{
   # If windows then Parse the bad IPs and create a ps1 script that has the firewall rules with the commands to block 
    Windows
   {
        # Get the IP addresses discovered, loop through and replace the beginning of the line with the IPTables syntax 
        # After the IP address, add the remaining IPTables syntax and save the results to a file 
        (Get-Content -Path "C:\Users\johnt\Documents\GitHub\SYS320Tiseo\Week11\homework\ips-bad.tmp") | ForEach-Object `
        {$_ -replace "^", "netsh advfirewall firewall add rule name='Bad IP Blocker' dir=in action=block remoteip=" -replace "$"} | `
        Out-File -FilePath "C:\Users\johnt\Documents\GitHub\SYS320Tiseo\Week11\homework\windows-firewall-rules.ps1"
        

        
   }
   # If IPTables is read, this parses the bad ip list add the IPTables syntax, then this uploads them to the remote server.
   IPTables
   {    
        # Get the IP addresses discovered, loop through and replace the beginning of the line with the IPTables syntax.
        # After the IP address, add the remaining IPTables syntax and save the results to a file.

       (Get-Content -Path "C:\Users\johnt\Documents\GitHub\SYS320Tiseo\Week11\homework\ips-bad.tmp") | ForEach-Object `
       {$_ -replace "^", "iptables -A INPUT -s " -replace "$", " -j DROP"} | `
       Out-File -FilePath "C:\Users\johnt\Documents\GitHub\SYS320Tiseo\Week11\homework\iptables.bash"

        # Login to the remote SSH server.
        New-SSHSession -ComputerName '192.168.6.71' -Credential (Get-Credential 'john.tiseo@cyber.local') -Port '2222'

        # Upload the firewall rules to the remote system.
        Set-SCPItem -ComputerName '192.168.6.71' -Credential (Get-Credential 'john.tiseo@cyber.local') -Path 'C:\Users\johnt\Documents\GitHub\SYS320Tiseo\Week11\homework\iptables.bash' -Destination '/home/john.tiseo/' -Port '2222'

        # Check to see if file was moved over, and print the results
        if ((Invoke-SSHCommand -index 0 'dir iptables.bash').ExitStatus -eq 0 )
        {
            Write-Host -BackgroundColor "Green" -ForegroundColor "white" "Firewall rules file was uploaded!"
        } 
        else
        {
            Write-Host -BackgroundColor "Red" -ForegroundColor "white" "Firewall rules file was not uploaded!"
        }

   }
    
}