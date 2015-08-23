@echo off

title Toontown Rewritten [Injector Collection]

set /P PYTHON_PATH=<PYTHON_PATH

echo Choose your injector!
echo.

echo #1 - CMD Injector
echo #2 - Test TTR Injector
echo #3 - TTR Injector [Chan's Version]
echo.

:selection

set INPUT=-1
set /P INPUT=Selection: 

if %INPUT%==1 (
    %PYTHON_PATH% -m CmdTTRHack
) else if %INPUT%==2 (
    %PYTHON_PATH% -m TestTTRInjector
) else if %INPUT%==3 (
    %PYTHON_PATH% -m ChansInjector
) else (
	goto selection
)

pause
goto selection