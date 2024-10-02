from PIL import Image
image_paths = [ #GIF haline getirilecek resimlerin dosya yolu
    "C:/Users/DELL/Desktop/Animate/images/1.png",
    "C:/Users/DELL/Desktop/Animate/images/2.png",
    "C:/Users/DELL/Desktop/Animate/images/3.png",
    "C:/Users/DELL/Desktop/Animate/images/4.png", 
    "C:/Users/DELL/Desktop/Animate/images/5.png", 
    "C:/Users/DELL/Desktop/Animate/images/6.png",
    "C:/Users/DELL/Desktop/Animate/images/7.png", 
    "C:/Users/DELL/Desktop/Animate/images/8.png", 
    "C:/Users/DELL/Desktop/Animate/images/9.png"
]
images = [Image.open(image_path).convert("RGB") for image_path in image_paths]
base_image = images[0]
base_size = base_image.size
resized_images = [img.resize(base_size) for img in images]
paletted_images = [img.convert("P", palette=Image.ADAPTIVE) for img in resized_images]
paletted_images[0].save(
    "animated.gif",  # Çıkış dosya adı
    save_all=True,   
    append_images=paletted_images[1:],  
    optimize=True,   
    loop=0,          # Animasyonun sonsuz döngü yapması için 0
    duration=0.01     # Her bir resmin gösterim süresi (milisaniye cinsinden)
)
