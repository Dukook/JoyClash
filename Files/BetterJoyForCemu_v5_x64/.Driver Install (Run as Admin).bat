@echo off
:: Admin elevation script credit goes to BetaLeaf
setLocal EnableExtensions EnableDelayedExpansion
set "ScriptPath=%~dp0"
set "ScriptPath=%ScriptPath:~0,-1%"
set "ScriptName=%~n0.bat"
pushd "%ScriptPath%"

:: CHECK ADMIN RIGHTS
fltmc >nul 2>&1
if "%errorlevel%" NEQ "0" (goto:UACPrompt) else (goto:GotAdmin)

:UACPrompt
echo:
echo   Requesting Administrative Privileges...
echo   Press YES in UAC Prompt to Continue
echo:
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\GetAdmin.vbs"
echo args = "ELEV " >> "%temp%\GetAdmin.vbs"
echo For Each strArg in WScript.Arguments >> "%temp%\GetAdmin.vbs"
echo args = args ^& strArg ^& " "  >> "%temp%\GetAdmin.vbs"
echo Next >> "%temp%\GetAdmin.vbs"
echo UAC.ShellExecute "%ScriptName%", args, "%ScriptPath%", "runas", 1 >> "%temp%\GetAdmin.vbs"
cmd /u /c type "%temp%\GetAdmin.vbs">"%temp%\GetAdminUnicode.vbs"
cscript //nologo "%temp%\GetAdminUnicode.vbs"
del /f /q "%temp%\GetAdmin.vbs" >nul 2>&1
del /f /q "%temp%\GetAdminUnicode.vbs" >nul 2>&1
exit /B

:GotAdmin
if '%1'=='ELEV' shift /1
if exist "%temp%\GetAdmin.vbs" del /f /q "%temp%\GetAdmin.vbs"
if exist "%temp%\GetAdminUnicode.vbs" del /f /q "%temp%\GetAdminUnicode.vbs"

cd /d "%~dp0Drivers"

devcon.exe remove Root\ViGEmBus >nul 2>&1

echo Installing the ViGEm emulated gamepads driver..

call devcon.exe install ViGEmDriver\ViGEmBus.inf Root\ViGEmBus >nul 2>&1
if %ERRORLEVEL% == 0 goto :success
echo Installation failed; you need to right click the .bat and "run as admin".
pause 
exit

:success
echo Installation is successful; if you want to uninstall the driver, run "! Driver Uninstall (Run as Admin).bat"

devcon.exe install .\HidGuardian\HidGuardian.inf Root\HidGuardian
devcon.exe classfilter HIDClass upper -HidGuardian

cd .\HidCerberus.Srv
echo Installing HidCerberus.Srv...
HidCerberus.Srv.exe install

ping 127.0.0.1 -n 2 > nul

net start "HidCerberus Service"

ping 127.0.0.1 -n 2 > nul

echo Done

ECHO.
ECHO.
pause
