from PIL import Image

import glob

    
bgs = []
for filename in glob.glob('./layers/bgs/*.png'):
    bgs.append(Image.open(filename))
    
bodys = []
for filename in glob.glob('./layers/bodys/*.png'):
    bodys.append(Image.open(filename))
    
heads = []
for filename in glob.glob('./layers/heads/*.png'):
    heads.append(Image.open(filename))

tops = []
for filename in glob.glob('./layers/tops/*.png'):
    tops.append(Image.open(filename))

imgNum=0
for bg in bgs:
    for body in bodys:
        for head in heads:
            for top in tops:
#                 display(bg)
#                 display(body)
#                 display(head)
#                 display(top)
                # compose
                img = bg.copy()
                img.paste(body,(0,0), body)
                img.paste(head,(0,0), head)
                img.paste(top,(0,0),top)
#                 display(img)
                img.save("./layers/{}.png".format(imgNum))
                imgNum=imgNum+1
                
                
