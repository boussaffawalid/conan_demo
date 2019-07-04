
## running the script python build.py works as expected

## Build locally does not work

For example

```
mkdir build
cd build
conan install ..
```

I got this error

ERROR: conanfile.py (demo/1.0.0@None/None): Error in requirements() method, line 32
	versions = tools.load('deps.cmake')
	FileNotFoundError: [Errno 2] No such file or directory: 'deps.cmake'