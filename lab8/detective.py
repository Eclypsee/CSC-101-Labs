ransom_note = "AppleBe es"
magazine = "es eB Ap p le AAA"

ransom_note_1 = "AppleBees"
magazine_1 = "ApleBes"

def can_make_note_out_of_magazine(r:str, m:str)->bool:
    if len(r)>0 and len(m)>0:
        rls = []
        for el in r:
            if not el == " ":
                rls.append(el)
        mls = []
        for el in m:
            if not el == " ":
                mls.append(el)
        for i in range(len(rls)):
            found = False
            for j in range(len(mls)):
                if rls[i]==mls[j]:
                    mls[j] = -1
                    found = True
                    break # out of inner loop
            if not found == True:
                return False
        return True
    else:
        return False

print(can_make_note_out_of_magazine(ransom_note, magazine))#true, we can make the ransome note out of the letters
print(can_make_note_out_of_magazine(ransom_note_1, magazine_1))#false, we cannot do it.