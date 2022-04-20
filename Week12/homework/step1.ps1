<# 
    Task 1:
    Storyline: Powershell is copied over from user directory and placed in desktop, then comes out with a message to whether it worked or not.
#>

# Powershell Location 
$file = "C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe" 

# User Dir 
$user_dir = "C:\Users\johnt\Desktop\"

# Copy file to User Dir
Copy-Item $file -Destination $user_dir

# Random Number Generator 
$rand = Get-Random -Minimum 1000 -Maximum 9876

# The location of the powershell file 
$fileLocation = $user_dir + "powershell.exe"

# Name of file made
$newName = "EnNoB-" + $rand + ".exe"

# Var that stores file 
$newFile = $user_dir + $newName

# Rename Powershell
Rename-Item -Path $fileLocation -NewName $newName

# Checks for success and prints confirmation, or error.

if (Test-Path $newFile)
{
    Write-Host -BackgroundColor "Green" -ForegroundColor "white" "File Created!"
} 
else
{
    Write-Host -BackgroundColor "Red" -ForegroundColor "white" "File not created!"
}

<# 
    Task 2
    Storyline: In this task a README with text is created and placed on user's desktop.
#>

# Message
$msg = "If you want your files restored, please contact me at dunston@champlain.edu. I look forward to doing business with you."

# Create a README.READ file and save it to the desktop
$ReadMEfile = "C:\Users\johnt\Desktop\Readme.READ"
Write-Output $msg | out-file -FilePath $ReadMEfile

# Checks for README and prints anything it finds that meets critera
if (Test-Path $ReadMEfile)
{
    Write-Host -BackgroundColor "Green" -ForegroundColor "white" "README file was created!"
} 
else
{
    Write-Host -BackgroundColor "Red" -ForegroundColor "white" "README file was not created!"
}

<# 
    Week 12 task 4
    Storyline: In this task it creates a file called update.bat, and writes the file out 
#>

# create the contents update.bat file,  
$writeUpdateFile = @'
del "C:\Users\johnt\Documents\GitHub\SYS320Tiseo\Week12\homework\step2.ps1"
'@

# Write to a file
$writeUpdateFile | out-file -FilePath ".\update.bat"