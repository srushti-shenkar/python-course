#create window
root=Tk()
root.title('Login App')
root.geometry('400x400')
#create a frame to organize elements better
frame=Frame(master=root,height=200,width=360,bg="#d0efff")
#add widgets
#add labels
lbl1=Label(frame,text="Full Name",bg="#3895D3",fg='white',width=12)
lbl2=Label(frame,text="Email Id",bg="#3895D3",fg='white',width=12)
lbl3=Label(frame,text="Enter Password",bg="3895D3",fg='white',width)