from PIL import Image
import sys
#print(sys.argv)
ico_size=256
fn=sys.argv[1]
img=Image.open(fn)
(x_ori,y_ori)=img.size
mult_factor=float(ico_size)/max(x_ori,y_ori)
(x_scaled,y_scaled)=(int(round(mult_factor*x_ori)),int(round(mult_factor*y_ori)))
#print(x_scaled)
#print(y_scaled)
img_scaled=img.resize((x_scaled,y_scaled))
ico=Image.new('RGBA',(ico_size,ico_size))



x_rest_left=int(round((ico_size-x_scaled)/2))
y_rest_up=int(round((ico_size-y_scaled)/2))
x_rest_rigth=ico_size-x_scaled-x_rest_left
y_rest_down=ico_size-y_scaled-y_rest_up
#print(x_scaled)
#print(x_rest_left)
#print(x_rest_rigth)
#print(y_scaled)
#print(y_rest_up)
#print(y_rest_down)

def is_in_valid_place(x,y):
	return x>=x_rest_left and x<=(ico_size-1-x_rest_rigth) and y>=y_rest_up and y<=(ico_size-1-y_rest_down)

def ico_pos_to_scaled_pos(x,y):
	return(x-x_rest_left,y-y_rest_up)

for x in range(ico_size):
	for y in range(ico_size):
		if is_in_valid_place(x,y):
			(x2,y2)=ico_pos_to_scaled_pos(x,y)
			pix=img_scaled.getpixel((x2,y2))
			(r,g,b)=(pix[0],pix[1],pix[2])
			ico.putpixel((x,y),(r,g,b,255))
		else:
			ico.putpixel((x,y),(0,0,0,0))
		
ico.save("icon.ico")
