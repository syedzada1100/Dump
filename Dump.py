import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from dump import main
    main()
elif bit == '32bit':
    from dump32 import main
    main()
else:
    print('\n YOUR DEVICE IS NOT SUPPORT THIS TOOL')
    os.system('exit')
