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
    %PYTHON_PATH% -m TTR Cmd Hack.py
) else if %INPUT%==2 (
    %PYTHON_PATH% -m TestTTRInjector.py
) else if %INPUT%==3 (
    %PYTHON_PATH% -m TTR Injector [Chan].py
) else (
	goto selection
)

pause