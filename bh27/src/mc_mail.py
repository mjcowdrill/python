
import email
import os

def pack_mail(source_dir, **headers):
    ''' Given source_dir, a string that is a path to an existing, 
        readable directory, and arbitrary header name/value pairs 
        passed in as named arguments, packs all the files directly 
        under source_dir (assumed to be plain text files) into a 
        mail message returned as a string.
    '''
    
    msg = email.Message.Message()
    
    for name, value in headers.items():
        msg[name] = value
        
    msg['Content-type'] = 'multipart/mixed'
    
    filenames = os.walk(source_dir).next()[-1]
    
    for filename in filenames:
        print filename

        m = email.Message.Message()
        m.add_header("Content-type", 'text/plain', name=filename)

        with open(os.path.join(source_dir, filename), "r") as f:
            m.set_payload(f.read())
        msg.attach(m)
        
    return msg.as_string()

if __name__ == "__main__":
    s = pack_mail(r"c:\temp", name1="value1")
    print "This is s..."
    print s
