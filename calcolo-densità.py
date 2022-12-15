# Calcolare la densità con python
from tkinter import ttk
from tkinter import * 

window = Tk()
window.geometry("600x600")
window.resizable(False, False)
window.title("Density Calculator")


welcome = ttk.Label(text="Welcome to the density calculator", font=12)
welcome.grid(column=2, row=1, padx=170, pady=20)

def density_calculation():
    m = float(input_massa.get())
    v = float(input_volume.get())
    d = m/v
    risultato = ttk.Label(text=(d), font=11)
    risultato.grid(column=2, row=5, padx=170, pady=40)
    if d <= 1000:
        floating = ttk.Label(text="The body floats on distilled water (kg/m³)", font=11)
        floating.grid(column=2, row=7, padx=170, pady=45)
    if d > 1000: 
        floating = ttk.Label(text="The body doesn't float on distilled water (kg/m³)", font=11)
    





input_massa = ttk.Entry(width=40)
input_massa.grid(column=2, row=3, padx=170, pady=50)

input_volume = ttk.Entry(width=40)
input_volume.grid(column=2, row=4, padx=170, pady=40)


calculate_button = ttk.Button(window, text="Calculate!!", command=density_calculation, width=25,)
calculate_button.grid(column=2, row=6, padx=170, pady=50)



# End of the code
if __name__ == "__main__":
    window.mainloop()

