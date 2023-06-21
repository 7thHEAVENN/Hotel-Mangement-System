from tkinter import *
import os
import tkinter.font as font


w=0
f=0
def Main_page():
     root = Tk()
     root.title("Hotel Management")
     root.config(bg = "#559CAD")
     root.geometry("500x420")
     f1=font.Font(family='Arial Black',size=15)
     f2=font.Font(family='Boulder',size=12)


     def booking():
          root.destroy()
          global f
          Booking()
          print(f)
         
     def room_info():
          root.destroy()
          Room_info()
     
     def restaurant():
          root.destroy()
          global w
          Restaurant()
          print(w)
          
     def payment():
          root.destroy()
          Payment()
          
     frame = LabelFrame(root,text = "Welcome To Dinesh's Hotel",padx=10,pady=20,bg = "#FFFFFF",font=f1)
     frame.pack(padx=20,pady=30)
     label1 = Label(frame,text = "Welcome To Your Python Hotel Manager",padx = 15,pady = 10,bg="#FFFFFF",font=f2,fg='red').pack()
     button2 = Button(frame,text = "Room Info",command = room_info,bg = "#F3DFBF",font=f2).pack()
     button1 = Button(frame,text = "Booking",command = booking,bg = "#F3DFBF",font=f2).pack()
     button3 = Button(frame,text = "Restaurant",command = restaurant,bg = "#F3DFBF",font=f2).pack()
     button4 = Button(frame,text = "Payment And Checkout",command = payment,bg = "#F3DFBF",font=f2).pack()
     root.mainloop()
def Room_info():
     root = Tk()
     root.title("Hotel Management")
     root.config(bg = "#559CAD")
     root.geometry("600x700")
     def continue1():
          root.destroy()
          Main_page()

     f=font.Font(family='Arial Black',size=18)
     f1=font.Font(family='Boulder',size=12)

     frame3 = LabelFrame(root,text = "Cheap", padx = 15,pady = 15,font=f)
     frame3.pack(padx = 25,pady = 15)
     label1 = Label(frame3, text = "single bedroom \n breakfast included(free) \n swimming pool and spa facilities \n price-$2000",fg='red').grid(row = 1)

     frame1 = LabelFrame(root,text = "Deluxe", padx = 15,pady = 15,font=f)
     frame1.pack(padx = 25,pady = 15)
     label1 = Label(frame1, text = "double bedroom \n breakfast and lunch included(free) \n swimming pool and spa facilities \n price-$3000",fg='red').grid(row = 1)

     frame2 = LabelFrame(root,text = "Supreme", padx = 15,pady = 15,font=f)
     frame2.pack(padx = 25,pady = 15)
     label1 = Label(frame2, text = "triple bedroom \n breakfast and lunch included(free) \n swimming pool and spa facilities \n seaside view \n price-$4000",fg='red').grid(row = 1)
     frame = LabelFrame(root,text = "Main", padx = 15,pady = 15,font=f)
     frame.pack(padx = 25,pady = 15)
     button5 = Button(frame,text = "Continue",command = continue1,bg = "#F3DFBF").pack()
     root.mainloop()


def Booking():
     root = Tk()
     root.title("Hotel Management")
     root.config(bg = "#559CAD")
     root.geometry("500x420")
     f1=font.Font(family='Arial Black',size=15)
     f2=font.Font(family='Boulder',size=12)

     def book():
          a=entry1.get()
          z = r.get()
          global f
          if z == 1:
               f=2000
               root.destroy()
               root1 = Tk()
               root1.title("Hotel Management")
               root1.config(bg = "#559CAD")
               root1.geometry("500x420")

               def cont():
                    root1.destroy()
                    Main_page()
                    
               frame = LabelFrame(root1,text = "Cheap", padx = 15,pady = 20,font=f1,fg='red')
               frame.pack(padx = 5,pady =5 )
               label1 = Label(frame, text = "Your room has been booked successfully\n\nHope u enjoy your stay "+a,font=f2).grid(row = 1)
               button1 = Button(frame,text = "Back to Main page",command = cont,bg = "#F3DFBF",font=f2).grid(row = 2,)
               return f
               
          elif z == 2:
               f=3000
               root.destroy()
               root1= Tk()
               root1.title("Hotel Management")
               root1.config(bg = "#559CAD")
               root1.geometry("500x420")

               def cont():
                    root1.destroy()
                    Main_page()
     
               frame = LabelFrame(root1,text = "Deluxe", padx = 15,pady = 20,font=f1,fg='red')
               frame.pack(padx = 5,pady = 5)
               label1 = Label(frame, text = "Your room has been booked successfully\n\nhope u enjoy your stay Mr/Mrs "+a,font=f2).grid(row = 1)
               button1 = Button(frame,text = "Back to Main page",command = cont,bg = "#F3DFBF",font=f2).grid(row = 2,)
               return f
               

          elif z == 3:
               f=4000
               root.destroy()
               root1 = Tk()
               root1.title("Hotel Management")
               root1.config(bg = "#559CAD")
               root1.geometry("500x420")
               
               def cont():
                    root1.destroy()
                    Main_page()
               
               
               frame = LabelFrame(root1,text = "Supreme", padx = 15,pady = 20,font=f1,fg='red')
               frame.pack(padx = 5,pady = 5)
               label1 = Label(frame, text = "Your room has been booked successfully\n\nhope u enjoy your stay Mr/Mrs "+a,font=f2).grid(row = 1)
               button1 = Button(frame,text = "Back to Main page",command = cont,bg = "#F3DFBF",font=f2).grid(row = 2,)
               return f
               
     r=IntVar()
     frame = LabelFrame(root,text = "main", padx = 20,pady = 20,font=f1,)
     frame.pack(padx = 10,pady = 10)
     label1 = Label(frame, text = "Enter Customers Name:",font=f2,fg='red').grid(row = 1)
     label12= Label(frame,text = "Enter your Phone number",font=f2,fg='red').grid(row=2)
     entry1 = Entry(frame,font=f2)
     entry2 = Entry(frame,font=f2)
     
     label2 = Label(frame, text = "Select Package:    ",font=f2).grid(row = 3)
     Radiobutton(frame ,text = "cheap($2000)",variable = r, value = 1,font=f2).grid(row = 3,column = 2)
     Radiobutton(frame ,text = "deluxe($3000)",variable = r, value = 2,font=f2).grid(row = 4,column = 2)
     Radiobutton(frame ,text = "supreme($4000)",variable = r, value = 3,font=f2).grid(row = 5,column = 2)
     button1 = Button(frame,text = "book",command = book,font=f2,bg = "#F3DFBF").grid(row = 5,column = 1)
     entry1.grid(row = 1,column = 2)
     entry2.grid(row = 2,column = 2)
     root.mainloop()


def Restaurant():
     def Restaurant1():
          root = Tk()
          root.title("Hotel Management")
          root.config(bg = "#559CAD")
          root.geometry("650x800")
          f1=font.Font(family='Arial Black',size=12)
          f2=font.Font(family='Boulder',size=10)
          def sum1():
               a = r.get()
               b = s.get()
               c = u.get()
               z=0
               x=0
               y=0
               global w
               if a == 1:
                    x = x+1200
               if a == 2:
                    x=x+1300
               if a == 3:
                    x=x+1500
               if b == 1:
                    y = y+1000
               if b == 2:
                    y=y+1400
               if b == 3:
                    y=y+1100
               if c == 1:
                    z= z+120
               if c == 2:
                    z = z+130
               if c == 3:
                    z = z+150
               w = x+y+z
               
               frame = LabelFrame(root,text = "You Have To Pay", padx = 5,pady = 10)
               label1 = Label(frame, text = w).pack()
               button1 = Button(frame,text = "Continue",command=exit1,font=f2,fg='red').pack()
               frame.pack(padx = 5,pady = 5)
               return w
          def exit1():
               root.destroy()
               Main_page()


        
          r=IntVar()
          frame1 = LabelFrame(root,text = "Main Course", padx = 5,pady = 10,font=f1)
          frame1.pack(padx = 5,pady = 5)
          Radiobutton(frame1 ,text = "Soupe à l'oignon-$1200",variable = r, value = 1,font=f2,fg='red').grid(row = 2,column = 2)
          Radiobutton(frame1 ,text = "Boeuf bourguignon-$1300",variable = r, value = 2,font=f2,fg='red').grid(row = 3,column = 2)
          Radiobutton(frame1 ,text = "Cassoulet-$1500",variable = r, value = 3,font=f2,fg='red').grid(row = 4,column = 2)

          s=IntVar()
          frame2 = LabelFrame(root,text = "Starters", padx = 5,pady = 10,font=f1)
          frame2.pack(padx = 5,pady = 5)
          Radiobutton(frame2 ,text = "Steak frites-$1000",variable = s, value = 1,font=f2,fg='red').grid(row = 2,column = 2)
          Radiobutton(frame2 ,text = "Chicken confit-$1400",variable = s, value = 2,font=f2,fg='red').grid(row = 3,column = 2)
          Radiobutton(frame2 ,text = "Quiche-$1100",variable = s, value = 3,font=f2,fg='red').grid(row = 4,column = 2)

          u=IntVar()
          frame3 = LabelFrame(root,text = "Desert", padx = 5,pady = 10,font=f1)
          frame3.pack(padx = 5,pady = 5)
          Radiobutton(frame3 ,text = "Ice Cream-$120",variable = u, value = 1,font=f2,fg='red').grid(row = 2,column = 2)
          Radiobutton(frame3,text = "Cake-$130",variable = u, value = 2,font=f2,fg='red').grid(row = 3,column = 2)
          Radiobutton(frame3 ,text = "Ice Cream Cake-$150",variable = u, value = 3,font=f2,fg='red').grid(row = 4,column = 2)


          frame = LabelFrame(root,text = "Pay", padx = 5,pady = 10,font=f1)
          frame.pack(padx = 5,pady = 5)
          button1 = Button(frame,text = "You have to pay",command=sum1,font=f2,fg='red').pack()
          root.mainloop()
     Restaurant1()
     return w

def Payment():
     root=Tk()
     root.title("hotel management")
     root.config(bg="#559CAD")
     root.geometry("600x500")
     f1=font.Font(family='Arial Black',size=15)
     f2=font.Font(family='Boulder',size=13)
     f3=font.Font(family='Boulder',size=20)
     def payment1():
          global w
          global f
          z = r.get()
          
          if z == 1:
               root.destroy()
               global w
               global f
               total=w+f
               def Exit():
                    root2.destroy()
                    root = Tk()
                    root.title("Hotel Management")
                    root.config(bg = "#559CAD")
                    root.geometry("600x500")
                    def exit1():
                         root.destroy()
                    
                    frame = LabelFrame(root,text = "CHECKOUT", padx = 60,pady = 50,font=f1,fg='red')
                    frame.pack(padx = 20,pady = 20)     
                    label1 = Label(frame,text="Thank You For Visiting ",font=f2,fg='blue').pack()
                    label2 = Label(frame,text="Hope u Enjoyed your stay",font=f2,fg='blue').pack()
                    label3 = Label(frame,text="Please give us your feedback before exitting",font=f2,fg='blue').pack()
                    entry=Entry(frame,font=f3).pack()
                    button1 = Button(root,text = "Exit",command = exit1,font=f2,bg="#F3DFBF").pack()
                    root.mainloop()


               root2 = Tk()
               root2.title("Hotel Management")
               root2.config(bg ="#559CAD")
               root2.geometry("500x420")
               frame = LabelFrame(root2,text = "Payment Method : Cash",font=f1,padx=10,pady=20)
               frame.pack(padx=20,pady=30)
               label1 = Label(frame,text =total,padx = 50,pady = 30,font=f2,fg='red').pack()
               button1 = Button(frame,text = "checkout",command = Exit,font=f2,bg="#F3DFBF").pack()
               root2.mainloop()

               
          if z == 2:
               root.destroy()
               total=w+f
               def Exit():
                    root2.destroy()
                    root = Tk()
                    root.title("Hotel Management")
                    root.config(bg = "#559CAD")
                    root.geometry("600x500")
                    def exit1():
                         root.destroy()
                    
                    frame = LabelFrame(root,text = "CHECKOUT", padx = 60,pady = 50,font=f1,fg='red')
                    frame.pack(padx = 20,pady = 20)     
                    label1 = Label(frame,text="Thank You For Visiting ",font=f2,fg='blue').pack()
                    label2 = Label(frame,text="Hope u Enjoyed your stay",font=f2,fg='blue').pack()
                    label3 = Label(frame,text="Please give us your feedback before exitting",font=f2,fg='blue').pack()
                    entry=Entry(frame,font=f3).pack()
                    button1 = Button(root,text = "Exit",command = exit1,font=f2,bg="#F3DFBF").pack()
                    root.mainloop()



               root2 = Tk()
               root2.title("Hotel Management")
               root2.config(bg ="#559CAD")
               root2.geometry("500x420")
               frame = LabelFrame(root2,text = "Payment Method : Card",padx=10,pady=20,font=f1)
               frame.pack(padx=20,pady=30)
               label1 = Label(frame,text =total,padx = 50,pady = 30,font=f2,fg='red').pack()
               button1 = Button(frame,text = "checkout",command = Exit,font=f2,bg="#F3DFBF").pack()
               root2.mainloop()

               

               
     r = IntVar()                         
     frame = LabelFrame(root,text = "PAYEMENT", padx = 5,pady = 10,font=f1)
     frame.pack(padx = 10,pady = 20)          
     label2 = Label(frame, text = "Enter mode of payement:    ",font=f2,fg='red').grid(row = 1)
     Radiobutton(frame ,text = "cash",variable = r, value = 1,font=f2).grid(row = 1,column = 2)
     Radiobutton(frame ,text = "credit/card",variable = r, value = 2,font=f2).grid(row = 2,column = 2)
     button1 = Button(frame,text = "continue to pay",command = payment1,font=f2,bg="#F3DFBF").grid(row = 3,column = 2)
     root.mainloop()


Main_page()


