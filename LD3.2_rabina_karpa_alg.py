#____________________________________________________
def areEqual(s1:str,s2:str) -> bool:
  lenS1 = len(s1)
  lenS2 = len(s2)
  if(lenS1 != lenS2):
    return False
  for i in range(0,lenS1-1):
    if s1[i] != s2[i]:
      return False
  return True

B = 256
Q = 256
# no lekcijas piemeers (neizmantojam)___________________
def get_hash_(word: str) -> int:
  global B, Q
  lenWord = len(word)
  result = 0
  for i in range(lenWord):
    result = (B * result + ord(word[i])) % Q
  return result
#_______________________________________________________
def get_hash(word: str) -> int:
  global B, Q
  lenWord = len(word)
  result = ord(word[0])
  for i in range(1,lenWord):
    # result = (B * result + ord(word[i])) % Q
    result = (result * B) + ord(word[i])
  return result
#_______________________________________________________
def get_hash2(previousHash: int, spareChar: str, newChar: str, baze: int) -> int:
  global B
  result = 0
  result = ( previousHash - (ord(spareChar)*baze) )*B + ord(newChar)
  return result
#_______________________________________________________  
def search_word_in_text(text:str,word:str) -> None:
  global B, Q
  lenWord = len(word)
  lenText = len(text)
  hashWord = get_hash(word)
  # kontrolei testaa, lai saliidzinaatu, vai pareizi straadaa Rabina-Karpa algoritms
  #for i in range(0,lenText-lenWord+1):
  #  if (get_hash(text[i:i+lenWord]) == hashWord):
  #    if (areEqual(text[i:i+lenWord],word)):
  #      print(i,end=" ")
  print()
  if (get_hash(text[0:0+lenWord]) == hashWord):
    if (areEqual(text[0:0+lenWord],word)):
      print(0,end=" ")
  
  hashWordPrevious = get_hash(text[0:0+lenWord])
  baze = pow(B,lenWord-1)
  
  for i in range(1,lenText-lenWord+1):
    y = get_hash2(hashWordPrevious,text[i-1],text[i+lenWord-1],baze)
    if (y == hashWord):
      if (areEqual(text[i:i+lenWord],word)):
        print(i,end=" ")
    hashWordPrevious = y
#_________________________________________________________________________    
def main():

    apstradePabeigta = False
    while not(apstradePabeigta):
        IevadesVeids = input("Izvēlieties veidu, kā ievadīt datus - no ekrāna vai faila (I/F): ")
        if "I" in IevadesVeids:
            virkne = input("Ievadiet tekstu, kurā būs jāmeklē vārds: ")
            if ((len(virkne.strip()) < 1) or 
                (len(virkne.strip()) > 5*1000000) or 
                not(virkne.strip().isalpha())):
                print("Kļūda datu ievadē")
                return
            vards = input("Ievadiet meklējamo vārdu tekstā: ")
            if ((len(vards.strip()) < 1) or 
                (len(vards.strip()) > len(virkne.strip())) or 
                not(vards.strip().isalpha())):
                print("Kļūda datu ievadē")
                return
              
            search_word_in_text(virkne,vards)
            apstradePabeigta = True
        elif "F" in IevadesVeids: 
            #failaNos = input("Ievadiet faila nosaukumu: ")
            #failaNos = "tests/" + failaNos
            failaNos = "Dti.txt"
            if "a" not in failaNos:
                with open(failaNos, 'r') as f:
                #with open('dati.txt', 'r') as f:
                    vards =f.readline().strip()
                    virkne = f.readline().strip()
                    if ((len(virkne.strip()) < 1) or 
                      (len(virkne.strip()) > 5*1000000) or 
                      not(virkne.strip().isalpha())):
                      print("Kļūda datu ievadē")
                      return
                    if ((len(vards.strip()) < 1) or 
                      (len(vards.strip()) > len(virkne.strip())) or 
                      not(vards.strip().isalpha())):
                      print("Kļūda datu ievadē")
                      return
                  
                    search_word_in_text(virkne,vards)
                    apstradePabeigta = True
        else:
            print("Šādu simbolu ievadīt nav paredzēts")
            print("Ievadiet kādu no (I/F)")
            apstradePabeigta = False
         
    
if __name__ == '__main__':
     main()   
  