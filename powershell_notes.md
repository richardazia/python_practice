# Powershell and Python

# tree hierarchy, starting from root

* pwd - print working directory
* ls
* cd .. 
* cd c:\Users etc
* tab will autocomplete when we are typing. We can press it more than once to cycle through options. 
* echo $null >> hello.txt is one way to make an empty file creates the file in utf-16
* New-Item -ItemType file another_solution.txt
- Temp solution
* function touch {New-Item -ItemType File -Name ($args[0])} followed by
* touch cyclist.py

- Permanent
* C:\Users\USERSNAMEHERE\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1

- Removing directories
* rm -r -fo duck.txt where r = recursive, fo = force. Use with caution