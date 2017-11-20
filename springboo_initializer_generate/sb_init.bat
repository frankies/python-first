@echo off
set "b=%cd%"
set "sdir=%~dp0"
Pushd %b%
cd /d %sdir%  
python springboot_main.py --prog %~nx0 %*
popd
@echo on