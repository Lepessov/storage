import random

from tkinter import *
from tkinter import messagebox

def pass_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    password_input.insert(0, password)

    return password


def save_password():
    website = website_input.get()
    username = username_input.get()
    pas = password_input.get()


    if len(username) < 1 or len(website) < 1 or len(pas) < 1:
        warning = messagebox.showinfo(title='Invalid input', message='Input area is empty')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'Email: {username}\n Password: {pas}')
        if is_ok:
            with open('pas.txt', 'a') as file:
                file.write(f'{website} | {username} | {pas}\n')

            website_input.delete(0, END)
            password_input.delete(0, END)




window = Tk()
window.title('Password Manager')
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text='Website')
website_label.grid(row=1, column=0)
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

username_label = Label(text='Email/Username')
username_label.grid(row=2, column=0)
username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, 'fhrhrhhrueuu@gmail.com')

password_label = Label(text='Password')
password_label.grid(row=3, column=0)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

gen_pass =  Button(text='Generate Password', command=pass_generate)
gen_pass.grid(row=3, column=2)

add_but = Button(text='Add', width=36, command=save_password)
add_but.grid(row=4, column=1, columnspan=2)


window.mainloop()

