def scale_image(size, scale):
    a=size.split('x')
    return f"{int(a[0])*scale:n}x{int(a[1])*scale:n}"

scale_image("800x600", 2) #"1600x1200".
scale_image("100x100", 10) #"1000x1000".
scale_image("1024x768", 0.5) # "512x384".
scale_image("300x200", 1.5) # "450x300".