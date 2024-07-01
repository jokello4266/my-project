# get system information 

$osInfo = Get-CimInstance Win_OperatingSystem 
$osName = $osInfo.Caption
$osArchitecture = $osInfo.OsArchitecture
$osUptime = (Get-Date) - $osInfo.LastBootUpTime

Write-Output "Operating system : $osName"
Write-Output "Architecture: $osArchitecture"
Write-Output "Uptime: $osUptime"