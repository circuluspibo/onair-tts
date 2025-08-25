import requests

examples = [
    ("ar", "مرحباً، سعيد بلقائك."),          
    ("ar", "مرحباً، سعيد بلقائك."),          
    ("cs", "Ahoj, rád tě poznávám."),        
    ("cs", "Ahoj, rád tě poznávám."),        
    ("de", "Hallo, freut mich dich zu treffen."), 
    ("de", "Hallo, freut mich dich zu treffen."), 
    ("en", "Hello, nice to meet you."),       
    ("en", "Hello, nice to meet you."),       
    ("en", "Hello, nice to meet you."),       
    ("es", "Hola, encantado de conocerte."),  
    ("es", "Hola, encantado de conocerte."),  
    ("fa", "سلام، از دیدنت خوشوقتم."),        
    ("fa", "سلام، از دیدنت خوشوقتم."),        
    ("fi", "Hei, hauska tavata."),            
    ("fi", "Hei, hauska tavata."),            
    ("fil", "Kamusta, ikinagagalak kitang makilala."), 
    ("fil", "Kamusta, ikinagagalak kitang makilala."), 
    ("fr", "Bonjour, ravi de vous rencontrer."), 
    ("fr", "Bonjour, ravi de vous rencontrer."), 
    ("hi", "नमस्ते, आपसे मिलकर खुशी हुई।"),     
    ("hi", "नमस्ते, आपसे मिलकर खुशी हुई।"),     
    ("hu", "Szia, örülök, hogy találkoztunk."), 
    ("hu", "Szia, örülök, hogy találkoztunk."), 
    ("id", "Halo, senang bertemu denganmu."), 
    ("id", "Halo, senang bertemu denganmu."), 
    ("it", "Ciao, piacere di conoscerti."),   
    ("it", "Ciao, piacere di conoscerti."),   
    ("ja", "こんにちは、はじめまして。"),        
    ("ja", "こんにちは、はじめまして。"),        
    ("km", "សួស្តី សប្បាយใจដែលបានជួបអ្នក។"),    
    ("km", "សួស្តី សប្បាយใจដែលបានជួបអ្នក។"),    
    ("ko", "안녕하세요. 만나서 반갑습니다."),      
    ("ko", "안녕하세요. 만나서 반갑습니다."),      
    ("ko", "안녕하세요. 만나서 반갑습니다."),      
    ("mn", "Сайн байна уу, танилцсандаа таатай байна."), 
    ("mn", "Сайн байна уу, танилцсандаа таатай байна."), 
    ("ms", "Halo, gembira bertemu dengan anda."), 
    ("ms", "Halo, gembira bertemu dengan anda."), 
    ("nl", "Hallo, leuk je te ontmoeten."),   
    ("nl", "Hallo, leuk je te ontmoeten."),   
    ("pl", "Cześć, miło cię poznać."),        
    ("pl", "Cześć, miło cię poznać."),        
    ("pt", "Olá, prazer em conhecê-lo."),     
    ("pt", "Olá, prazer em conhecê-lo."),     
    ("ru", "Здравствуйте, рад вас видеть."),   
    ("ru", "Здравствуйте, рад вас видеть."),   
    ("si", "හෙලෝ, ඔබව දැකීමට සතුටුයි."),       
    ("si", "හෙලෝ, ඔබව දැකීමට සතුටුයි."),       
    ("sv", "Hej, trevligt att träffas."),      
    ("sv", "Hej, trevligt att träffas."),      
    ("ta", "வணக்கம், உங்களை சந்தித்ததில் மகிழ்ச்சி."), 
    ("ta", "வணக்கம், உங்களை சந்தித்ததில் மகிழ்ச்சி."), 
    ("te", "హలో, నిన్ను కలవడం ఆనందంగా ఉంది."),     
    ("te", "హలో, నిన్ను కలవడం ఆనందంగా ఉంది."),     
    ("th", "สวัสดีครับ ยินดีที่ได้พบคุณ."),         
    ("th", "สวัสดีครับ ยินดีที่ได้พบคุณ."),         
    ("tr", "Merhaba, tanıştığımıza memnun oldum."), 
    ("tr", "Merhaba, tanıştığımıza memnun oldum."), 
    ("uk", "Привіт, радий зустрічі."),          
    ("uk", "Привіт, радий зустрічі."),          
    ("ur", "ہیلو، آپ سے مل کر خوشی ہوئی۔"),        
    ("ur", "ہیلو، آپ سے مل کر خوشی ہوئی۔"),        
    ("vi", "Xin chào, rất vui được gặp bạn."),   
    ("vi", "Xin chào, rất vui được gặp bạn."),   
    ("zh", "你好，很高兴见到你。"),                 
    ("zh", "你好，很高兴见到你。")                 
]

base_url = "http://127.0.0.1:8000/tts"

for idx, (lang, text) in enumerate(examples, start=1):
    params = {
        "text": text,
        "voice": idx - 1,   # 중복 횟수만큼 voice 번호가 올라감
        "lang": lang,
        "static": 0,
        "isPlay": 0
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        filename = f"output/tts_{lang}_{idx - 1}.wav"
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"[OK] Saved {filename}")
    else:
        print(f"[FAIL] {lang} - {response.status_code}")