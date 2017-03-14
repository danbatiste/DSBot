import pip

dependencies = [
    'pillow',
    'lxml',
    'requests',
    'pillow',
]

def install(package):
    pip.main(['install', package])

if __name__ == '__main__':
    try:
        for pkg in dependencies:
            install(pkg)
        print('\nSetup succeeded!')
    except:
        print('Error, please contact bot dev')