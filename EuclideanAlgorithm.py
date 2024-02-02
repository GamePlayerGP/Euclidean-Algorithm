import tkinter as tk

# GCD Calculation
def gcd(firstNumber, secondNumber):
    while secondNumber != 0:
        firstNumber, secondNumber = secondNumber, firstNumber % secondNumber
    return firstNumber


def main():
    global message
    try:
        result = gcd(int(firstEntry.get()), int(secondEntry.get()))
        message.set("The gcd is " + str(result))
    except ValueError:
        message.set("Need a number")


# UI
window = tk.Tk()
window.title("Euclidean Algorithm")
window.geometry("500x200")

welcomeLabel = tk.Label(window, text="Calculate the gcd of two numbers using the Euclidean algorithm",
                        font=("calibre", 12, "bold"))
welcomeLabel.grid(row=0, column=0, columnspan=2, pady=10)

firstLabel = tk.Label(window, text="Insert the first value: ", font=("calibre", 10))
firstLabel.grid(row=1, column=0, padx=10)

firstEntry = tk.Entry(window)
firstEntry.grid(row=1, column=1, padx=10)

secondLabel = tk.Label(window, text="Insert the second value: ", font=("calibre", 10))
secondLabel.grid(row=2, column=0, padx=10)

secondEntry = tk.Entry(window)
secondEntry.grid(row=2, column=1, padx=10)

calculateButton = tk.Button(window, text="Calculate GCD", command=main)
calculateButton.grid(row=3, column=0, columnspan=2, pady=10)

message = tk.StringVar()
message.set(" ")

resultLabel = tk.Label(window, textvariable=message, font=("calibre", 10, "bold"))
resultLabel.grid(row=4, column=0, columnspan=2)

window.mainloop()
