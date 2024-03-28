P="""Leo, also known and marketed as Leo: Bloody Sweet, is an upcoming Indian Tamil-language action thriller film[2] directed by Lokesh Kanagaraj, who co-wrote it with Rathna Kumar and Deeraj Vaidy. It is produced by S. S. Lalit Kumar of Seven Screen Studio while Jagadish Palanisamy serves as co-producer. The film stars Vijay and Trisha, alongside Sanjay Dutt, Arjun Sarja, Gautham Vasudev Menon, Mansoor Ali Khan and Mysskin.

"""
search=input("Enter the search word:").lower()
ps=P.lower().split(" ")
for i in ps:
    if (search in i.startswith(prefix)):
        print(i)
    
