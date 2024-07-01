# get system information 

$osInfo = Get-CimInstance Win_OperatingSystem 
$osName = $osInfo.Caption
