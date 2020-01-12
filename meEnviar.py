from tkinter import *
import tkinter.messagebox as tkMessagebox
import sqlite3
import tkinter.ttk as ttk

#Criando formulario principal
root = Tk()
#Criando o titulo
root.title("Locadora")

#Configurando o tamanho do formulario principal
width = 600
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2)-(width/2)
y = (screen_height/2)-(height/2)
root.geometry("%dx%d+%d+%d" % (width,height,x,y))
root.resizable (0,0) # bloqueia maximinizar 
root.configure(bg = "lightSteelBlue3")

#criando as variaveis do sistema, cadastro do usuario
USERNAME = StringVar()
PASSWORD = StringVar()
CLIENTE_ID = IntVar()
CLIENTE_NOME = StringVar()
CLIENTE_CIDADE = StringVar()
CLIENTE_ESTADO = StringVar()
CLIENTE_NASCIMENTO = StringVar()
CLIENTE_CPF = StringVar()
CLIENTE_TELEFONE = StringVar()
CLIENTE_EMAIL = StringVar()
CLIENTE_ID_FILME1 = IntVar()
CLIENTE_ID_FILME2 = IntVar()
CLIENTE_ID_FILME3 = IntVar()
SEARCH = StringVar()

#Criando Metodo dos botoes sair
def Exit():
    result = tkMessagebox.askquestion("Cadastro de clientes","Tem certeza?", icon="warning")
    if result == "Sim":
        root.destroy()
    exit()


def Exit2():
    result = tkMessagebox.askquestion("Cadastro de clientes","Tem certeza?", icon="warning")
    if result == "Sim":
        root.destroy()
    exit()

# criando o formulario login
def showLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Sistema de Locadora/Login")
    width = 700
    height = 370
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2)-(width/2)
    y = (screen_height/2)-(height/2)
    loginform.geometry("%dx%d+%d+%d" % (width,height,x,y))
    loginform.resizable (0,0) # bloqueia maximinizar 
    loginform

# criando campos do formulario de login
def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform,width = 50,height = 50,bd =1, relief = SOLID)
    TopLoginForm.pack(side = TOP, pady = 2)
    lbl_text = Label(TopLoginForm,text = "Seja bem vindo ao sistema da locadora",fg = "blue",font =( "arial",10,"bold"),width = 100)
    lbl_text.pack(fill = x )
    MidLoginForm = Frame(loginform, width = 600)
    MidLoginForm.pack(side = TOP, pady = 50)

    ldl_username = Label(MidloginForm, text = "Usuario:", font=('arial',15,"bold"), fg = "blue", bd = 18)
    ldl_username.grid(row=0)
    
    ldl_password = Label(MidloginForm, text = "Password:", font=('arial',15,"bold"), fg = "blue", bd = 18)
    ldl_password.grid(row=1)
    
    ldl_result = Label(MidloginForm, text = "", font=('arial',18))
    ldl_result.grid(row=3,columnspan = 2)

    username = Entry(MidLoginForm, textvariable = USERNAME, font = ("arial",15),width = 30)
    ldl_username.grid(row=0,column = 1)

    password = Entry(MidLoginForm, textvariable = PASSWORD, font = ("arial",15),width = 30,show = "*")
    password.grid(row=1,column = 1)

    # criando o botao
    btn_login = Button(MidLoginForm, text = "Login",font=('arial',18), width = 30, command = Login)
    btn_login.grid(row = 2, columnspan = 2, pady = 20)
    btn_login.bind('<Return>', Login)

# criando o formulario Home/Cadastro cliente.
def Home():
    global home
    home = Tk()
    Home.title("Cadastro de clientes")
    width = 1024
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2)-(width/2)
    y = (screen_height/2)-(height/2)
    Home.geometry("%dx%d+%d+%d" % (width,height,x,y))
    Home.resizable (0,0) # bloqueia maximinizar 
    Title = Frame(home, bd = 1, relief = SOLID)
    Title.pack(pady=10)

    lbl_display = Label(Title,text = "Cadastro de clientes", bg = 'orange', font=('arial',45))
    lbl_display.pack()

    menubar = Menu(home)
    filemenu=Menu(menubar, tearoff = 0)                       
    filemenu2=Menu(menubar, tearoff = 0)
    filemenu.add_command(Label = "Logout", command = Logout)
    filemenu.add_command(Label = "Sair", command = Exit2)
    filemenu2.add_command(Label = "Novo cadastro",command = ShowAddNew)
    filemenu2.add_command(Label = "Visualizar", command = ShowView)
    menubar.add_cascade(Label = "Conta", menu=filemenu)
    menubar.add_cascade(Label = "Cadastro", command = filemenu2)
    home.configure(menu = menubar)
    home.configure(bg = "orange")


#criando o metodo adicionar novo cadastro de clientes.
def ShoAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Cadastro Cliente/Adicionando novo cliente")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2)-(width/2)
    y = (screen_height/2)-(height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width,height,x,y))
    addnewform.resizable (0,0) # bloqueia maximinizar 
    addnewform
    
#Criando os campos do formulario novo cadastro de produtos.

def LoginForm():   
    global lbl_result
    TopAddNew = Frame(addnewform,width = 600,height = 100,bd =1, relief = SOLID)
    TopAddNew.pack(side = TOP, pady = 20)

    
    lbl_text = Label(TopAddNew,text = "Cadastrar novo cliente",fg = "blue",font =( "arial",18,"bold"),width = 100)
    lbl_text.pack(fill = x )
    
    TopAddNew = Frame(addnewform, width = 600)
    TopAddNew.pack(side = TOP, pady = 50)

    #cadastrando somente o nome, por enquanto
    ldl_nome_cliente = Label(MidAddNew, text = "Nome", font=('arial',15,"bold"), fg = "blue", bd = 18)
    ldl_nome_cliente.grid(row=0,sticky = w)
    

    #CAIXA
    nome_cliente = Entry(MidLoginForm, textvariable = CLIENTE_NOME, font = ("arial",15),width = 30)
    ldl_username.grid(row=0,column = 1)

   
    # criando o botao
    btn_add = Button(MidAddNew, text = "Salvar",font=('arial',18), width = 30, command = AddNew)
    btn_add.grid(row = 3, columnspan = 2, pady = 50)

    

# Criando o menu dropdown/menubar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)    
filemenu.add_command(label = "Entrar",command =  showLoginForm)
filemenu.add_command(label = "Sair",command = Exit)
menubar.add_cascade(label = "Arquivos",menu = filemenu)
root.configure(menu=menubar)



# Fechando o root do sistema
if __name__== " __main__":
    root.mainloop()

