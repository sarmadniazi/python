# O
def app(): 
    print("TYPE 1 FOR COMPUTER SCIENCE")
    print("TYPE 2 FOR DIGITAL WORD")
    print("TYPE 3 FOR DATA SCIENCE")
    print()
    x = int(input("ENTER YOUR CHOICE: "))
    if x == 1:
        cs = int(input(""" COMPUTER SCIENCE :  Principal areas of study within Computer Scienceinclude artificial intelligence, computer systems 
            and networks, security, database systems,human computer, interaction, vision and graph,
            numerical analysis, programming languages,
            software engineering, bioinformatics and theory of computing."""))
    elif x == 2:
      dw = int(input("""DIGITAL WORD : SEO, Content Marketing, PPC, Social Media Marketing,
            Email Marketing, Social Media Advertising, Video Marketing,
            Web Design & Web Development."""))
    elif x == 3:
      dc = int(input("""DATA SCIENCE : python,excel.sql,power bi,r,
            mongo db,macine learning """))
      
    else:
        print("PLEASE TYPE 1,2 OR 3 ")
        print()
        print("""WELCOME TO THE PYTHON APP   COURCES
          PRESS 1 FOR ENGLISH
         हिंदी के लिए 2 दबाएँ""")
        print()

def calcy():
    print("पायथन ऐप कोर्स में आपका स्वागत है")
    print("कंप्यूटर विज्ञान के लिए 1 दबाएँ")
    print("डिजिटल वर्ड के लिए 2 दबाएँ")
    print("डेटा विज्ञान के लिए 3 दबाएँ")
    x = int(input("अपनी पसंद दर्ज करें: "))
    if x2 == 1:
        cs = int(input("कंप्यूटर विज्ञान: "))
        print("""कंप्यूटर विज्ञान के भीतर अध्ययन के प्रमुख क्षेत्र
            कृत्रिम बुद्धिमत्ता, कंप्यूटर सिस्टम शामिल हैं
            और नेटवर्क, सुरक्षा, डेटाबेस सिस्टम,
            मानव कंप्यूटर इंटरेक्शन, विज़न और ग्राफिक्स,
            संख्यात्मक विश्लेषण, प्रोग्रामिंग भाषाएँ,
            सॉफ्टवेयर इंजीनियरिंग, जैव सूचना विज्ञान और कंप्यूटिंग का सिद्धांत।""")
    elif x2 == 2:
        dw = int(input("डिजिटल शबद: "))
        print(""" एसईओ, कंटेंट मार्केटिंग, पीपीसी, सोशल मीडिया मार्केटिंग,
            ईमेल मार्केटिंग, सोशल मीडिया     विज्ञापन, वीडियो मार्केटिंग,
            वेब डिज़ाइन और वेब विकास।""")
    elif x3 == 3:
        ds = int(input("डेटा विज्ञान: "))
        print("""पायथन, एक्सेल.एसक्यूएल, पावर बाय, आर,
            मोंगो डीबी, मैकिन लर्निंग """)   
    else:
        print("कृपया 1,2 या 3 टाइप करें")    
          
o1=app()
w1=calcy()
calcy()    
app()