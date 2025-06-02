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

ECHO Uninstalling ViGEm emulated Gamepads driver

devcon.exe remove Root\ViGEmBus

cd HidCerberus.Srv
echo Uninstalling HidCerberus.Srv...

HidCerberus.Srv.exe uninstall

cd /d "%~dp0\Drivers"

echo Removing system drivers...

devcon.exe remove Root\HidGuardian
devcon.exe classfilter HIDClass upper !HidGuardian

pause 