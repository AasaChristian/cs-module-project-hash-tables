

def word_count(s):
    store = {}
    lettrs = s.split()
    count = 1
    if s:
        for x in lettrs:
            low = x.lower().replace('"', '').replace('.', '').replace(',', '')
            if low not in store:
                store[low] = count
            else:
                store[low] +=count

    return store
        
     
            
    




if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))