The UNIX Shell is a command-line interpreter that: 1. reads commands from the user. 2. executes other programs. 3. passes the output back to the user. The Unix Shell is usually accessed through a terminal emulator which derived from old terminals.

The shell contains a full programming language, including variables, subroutines, loops etc. The basic idea is that everything is modeled as a text stream and therefore everything is a file and follows a directory hierarchy. Everything happens with respect to the current working directory. 

Multiple different shells available:
- bash (default on most GNU/Linux distributions)  
-  zsh (default on MacOS since 10.15 Catalina)  
## The Prompt
The prompt of a UNIX Shell looks like this `timbol@minerva:~$`. 
- Username: `timbol`
- Hostname: `minerva`
- Current working directory: `~`
## The Standard Streams
The streams can be connected to the console (keyboard and monitor), other programs,  
files, network, or some other kind of hardware via the standard streams:  
- #0: standard input (stdin), where the program reads its input, by default connected to the keyboard  
- #1: standard output (stdout), where the program writes its desired output, by default to the screen, often line-buffered for efficiency by default  
- #2: standard error (stderr), where the program writes other auxiliary output, such as error messages that are not part of its desired output, often unbuffered so that the message is directly available  
### Redirecting or Piping of Streams
The streams can be redirected to a file (redirecting stdin causes a file to be read, redirecting stdout a file to be written), or piped to another program.

