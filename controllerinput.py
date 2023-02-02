from inputs import *
from tkinter import *
from tkinter import PhotoImage

window = Tk()

controller = PhotoImage(file='controller.png').zoom(2)

c = Canvas(window,width=492,height=358,bg='black')
c.pack()

c.create_image(0,0, image=controller, anchor='nw')
c.create_oval(93,78,162,145, fill='black', outline='white')
c.create_oval(267,148,333,213, fill='black', outline='white')
c.create_rectangle(2,0,42,64)
c.create_rectangle(452,0,493,64)
c.create_line(127.5,78,127.5,145,fill='white')
c.create_line(93,111,162,111,fill='white')
c.create_line(300,148,300,213,fill='white')
c.create_line(267,180,333,180,fill='white')

y = c.create_oval(341,69,369,96,fill='black')
b = c.create_oval(374,99,401,126,fill='black')
x = c.create_oval(313,99,340,126,fill='black')
a = c.create_oval(342,130,369,156,fill='black')
start = c.create_oval(266,105,281,120,fill='black')
select = c.create_oval(202,105,217,119,fill='black')
dup = c.create_rectangle(179,159,190,176,fill='black')
ddown = c.create_rectangle(179,192,190,209,fill='black')
dleft = c.create_rectangle(159,179,176,189,fill='black')
dright = c.create_rectangle(192,180,209,189,fill='black')
rb = c.create_polygon(306,33,318,24,337,24,366,32,386,40,394,47,397,50,399,58,372,45,342,36,fill='black')
lb = c.create_polygon(178,33,166,24,147,24,118,32, 98,40, 90,47, 87,50, 85,58,112,45,142,36,fill='black')
lstickline = c.create_line(127.5,111,127.5,111,fill='white')
lstick = c.create_oval(102.5,85.5,152.5,135.5,fill='black',outline='white')
rstickline = c.create_line(300,180,300,180,fill='white')
rstick = c.create_oval(275,155,325,205,fill='black',outline='white')
lt = c.create_rectangle(0,0,40,0,fill='black')
rt = c.create_rectangle(452,0,493,0,fill='black')

#stolen block
def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
window.bind('<Motion>', motion)

def check_button(code,col,obj, check = 1):
    if event.code == code:
            if event.state == check:
                c.itemconfig(obj,fill=col)
            else:
                c.itemconfig(obj,fill='black')

# map -32768<=x<32767 to -75<=x<75 =/437

def check_joystick(codex,codey,obj,defaultx,defaulty,radius,line):
    x1,y1,x2,y2 = c.coords(obj)
    cx = (x1+x2) / 2
    cy = (y1+y2) / 2
    if event.code == codex:
        cx = defaultx + (event.state / 1000)
    elif event.code == codey:
        cy = defaulty - (event.state / 1000)
    c.coords(obj,cx-radius,cy-radius,cx+radius,cy+radius)
    c.coords(line,defaultx,defaulty,cx,cy)

def check_trigger(code,obj,topleft):
    if event.code == code:
        c.coords(obj,topleft,0,topleft+40,event.state / 4)


while True:
    events = get_gamepad()
    for event in events:
        check_button('BTN_NORTH','yellow',y)
        check_button('BTN_EAST','red',b)
        check_button('BTN_WEST','blue',x)
        check_button('BTN_SOUTH','green',a)
        check_button('BTN_SELECT','white',start)
        check_button('BTN_START','white',select)
        check_button('ABS_HAT0Y','white',dup,-1)
        check_button('ABS_HAT0Y','white',ddown)
        check_button('ABS_HAT0X','white',dleft,-1)
        check_button('ABS_HAT0X','white',dright)
        check_button('BTN_TR','white',rb)
        check_button('BTN_TL','white',lb)
        check_button('BTN_THUMBL','white',lstick)
        check_button('BTN_THUMBR','white',rstick)

        check_joystick('ABS_X','ABS_Y',lstick,127.5,111,25,lstickline)
        check_joystick('ABS_RX','ABS_RY',rstick,300,180,25,rstickline)

        check_trigger('ABS_Z',lt,0)
        check_trigger('ABS_RZ',rt,452)

        #print(event.ev_type)
        print(event.code)
        print(event.state)
    window.update()