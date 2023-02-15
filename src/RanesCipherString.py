# Encrypt
    def encrypt(self):
        plaintext = self.plain.get()
        key = self.key.get()

        if len(plaintext) == 0:
            messagebox.showerror("Error", "Please input plaintext / file")
        elif len(key) == 0:
            messagebox.showerror("Error", "Please input key / file")
        else :   
            ksa_key = self.KSA(key)
            prga_ksakey_plaintext = self.PRGA(ksa_key, plaintext)
            xor_plaintext_prgaksakey = self.XOR(plaintext, prga_ksakey_plaintext)
            result_string = self.ascii_to_text(xor_plaintext_prgaksakey)
            result_base64 = self.text_to_base64(result_string)
            self.cipher_string.set(result_string)
            self.cipher_base.set(result_base64)
    
    # Decrypt (Masih salah)
    def decrypt(self):
        plaintext = self.plain.get()
        key = self.key.get()

        if len(plaintext) == 0:
            messagebox.showerror("Error", "Please input plaintext / file")
        elif len(key) == 0:
            messagebox.showerror("Error", "Please input key / file")
        else :  
            ksa_key = self.KSA(key)
            prga_ksakey_plaintext = self.PRGA(ksa_key, plaintext)
            xor_plaintext_prgaksakey = self.XOR(plaintext, prga_ksakey_plaintext)
            result_string = self.ascii_to_text(xor_plaintext_prgaksakey)
            result_base64 = self.text_to_base64(result_string)
            self.cipher_string.set(result_string)
            self.cipher_base.set(result_base64)
