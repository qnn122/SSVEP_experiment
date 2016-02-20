function [] = py_udp_send(targetIP,port,data)
%
% py_udp_send.m--Sends a UDP packet containing a string to the specified
% host using Python's TCP/UDP utilities.  
%
% Input arguments are target host name or IP address (in string form),
% numeric port number and the string to be sent. The specified port number
% must be open in the target computer's firewall if the packet is to be
% received there.
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
% Syntax: py_udp_send(targetIP,port,data)
%
% e.g.,   py_udp_send('www.example.com',3333,'A B C 1.1 2.2 3.3')
% e.g.,   py_udp_send('192.0.34.166',3333,'3.14 2.7183')

% Developed in Matlab 7.6.0.324 (R2008a) on GLNX86.
% Kevin Bartlett (kpb@uvic.ca), 2009-03-30 11:08
%-------------------------------------------------------------------------

% Edit the following variables to reflect the location of python and of the
% udp_send.py script on your computer.
if isunix == true
    pythonExecutable = '/usr/local/bin/python2.6';
    pythonScript = '/home/bartlett/bin/udp_send.py';
else
    pythonExecutable = 'C:\Python25\python.exe';
    pythonScript = 'D:\Programming\py_udp\udp_send.py';
end % if

% Data must be a string. This is because data is passed as part of a
% "system" command as an argument to the Python script. 
if ~ischar(data)
    error([mfilename '.m--Data must be a string variable.']);
end % if

% Convert port number to a string if necessary.
if ~ischar(port)
    port = num2str(port);
end % if

cmd = [pythonExecutable ' ' pythonScript ' ' targetIP ' ' port ' "' data '"'];
[status,result] = system(cmd);

if status ~= 0
    errorStrPart = [mfilename '.m--Call to udp_send.py failed. Error message follows:'];
    errorStr = sprintf('%s\n%s',errorStrPart,result);
    error(errorStr);    
end % if

