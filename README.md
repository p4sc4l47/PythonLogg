## PythonLogg - Simple Color and Logging Library

### Simple Example

Add the logg.py file into your project and import it using

```
import logg
```

Print colorfull text using logg.Fore/Back

```
print(f"{logg.Fore.GREEN}This message is Green!{logg.Fore.RESET}")
```

Log a message

### INFO
```
logg.Log.Info("This is an info text!")
```

### WARNING
```
logg.Log.Warning("This is an warning!")
```

### ERROR
```
logg.Log.Info("This is an error!")
```
