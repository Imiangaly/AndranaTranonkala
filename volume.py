def volume():
    volumes = [24.5,5,87978,66666,20]
    for name in volumes:
        if name < 10:
            print(str(name) + " c'est trop bas")
        if name > 10000:
            print(str(name) + " c'est trop fort")
        else:
            print(str(name) + " c'est bon")
volume()