import sys, hashlib, itertools, threading, time

str_sha1=sys.argv[1]
mulai=int(sys.argv[2])
sampai=int(sys.argv[3])
str_kata=str(sys.argv[4])
stsLoop = True
def animated_loading():
    global stsLoop
    while(stsLoop):
        chars = "/—\|" 
        for char in chars:
            sys.stdout.write('\r'+'[-] loading... ' + char)
            time.sleep(.1)
            sys.stdout.flush() 
    sys.stdout.flush() 

def crackSha1(str_kata, u, str_sha1):
    global stsLoop
    sts = False
    print("[!] Starting from " + str(u) + " digits")
    for kata in itertools.product(str_kata,repeat=u) :
        if hashlib.sha1(''.join(kata).encode()).hexdigest() == str_sha1 :
            sts = True
            stsLoop = False
            print("[+] Found => " + ''.join(kata))
    if not sts:
        print("[x] Done, Not found in " + str(u) + " digits")
        sys.exit()

if __name__ =="__main__":
    for u in range(mulai,sampai+1) :
        if not u :
            continue
        threading.Thread(target=crackSha1, args=(str_kata,u,str_sha1)).start()    
    threading.Thread(name='loading', target=animated_loading).start()

# a9993e364706816aba3e25717850c26c9cd0d89d abc
