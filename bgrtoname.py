import webcolors
# def bgrtoname(bgr):
#     rgb=(bgr[0],bgr[1],bgr[2])
#     return webcolors.rgb_to_name(rgb)
# bgr=(0,0,255)
# print(bgrtoname(bgr))
def nametobgr(name):
    return webcolors.name_to_rgb(name)
n=str(input("enter name:"))
print(nametobgr(n))