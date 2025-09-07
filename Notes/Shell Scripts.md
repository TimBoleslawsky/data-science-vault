Shell scripts are a way to collect shell commands and execute them like a script in UNIX. In Windows these scripts are called *batch scripts*. A simple shell script could look like this:

``` sh
#!/bin/bash

for i in {1..5}; do
    if [ $i -eq 3 ]; then
        echo "This is number 3!"
    else
        echo "Current number: $i"
    fi
done
```

Important is the *shebang* (`#!`) and the name of the interpreter (`/bin/bash`).

