function [udpStr] = py_udp_receive(port)
%
% py_udp_receive.m--Receives a single UDP packet containing a string from
% the specified port using Python's TCP/UDP utilities.
%
% Note that the specified port must be open in the computer's firewall.
%
% This program and py_udp_receive.m are workarounds for a problem with
% sending UDP packets using Peter Rydesäter's TCP/UDP/IP Toolbox under
% Windows. Because they open a new Python session for every packet sent,
% they place heavy demands on a computer; sending and/or receiving more
% than about 1 packet per second will probably cause your computer to
% become very sluggish.
%
% How to install py_udp_send.m and py_udp_receive.m: 
%
% (1) Install Python on your computer (go to www.python.org). Linux
% computers probably already have Python installed. Windows users will also
% need to download and install the Python for Windows extensions (go to
% sourceforge.net and search for "pywin32"). Python is available for Macs,
% but these programs have not been tested on Apple systems.
%
% (2) Put py_udp_send.m and py_udp_receive.m on your Matlab
% path. 
%
% (3) Put the Python programs udp_send.py and udp_receive.py somewhere on
% your computer.
%
% (4) Edit py_udp_send.m and py_udp_receive.m to reflect the location of
% the udp_send.py and udp_receive.py programs on your computer and the
% location of the Python executable.
% 
% Syntax: udpStr = py_udp_receive(port)
%
% e.g.,   udpStr = py_udp_receive(3333)

% Developed in Matlab 7.8.0.347 (R2009a) on GLNX86.
% Kevin Bartlett (kpb@uvic.ca), 2009-06-11 11:11
%-------------------------------------------------------------------------

% Edit the following variables to reflect the location of python and of the
% udp_receive.py script on your computer.
if isunix == true
    pythonExecutable = '/usr/local/bin/python2.6';
    pythonScript = '/home/bartlett/bin/udp_receive.py';
else
    pythonExecutable = 'C:\Python25\python.exe';
    pythonScript = 'D:\Programming\py_udp\udp_receive.py';
end % if

% Convert port number to a string if necessary.
if ~ischar(port)
    port = num2str(port);
end % if

cmd = [pythonExecutable ' ' pythonScript ' ' port];
[status,result] = system(cmd);

if status ~= 0
    errorStrPart = [mfilename '.m--Call to udp_receive.py failed. Error message follows:'];
    errorStr = sprintf('%s\n%s',errorStrPart,result);
    error(errorStr);
else
    udpStr = result;
end % if
