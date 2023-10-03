from tkinter import *
window = Tk()
window.title("Miniproject 2.1.0")
window.wm_iconbitmap("c:/012/.vscode/Project/icon_minecraft.ico")
window.geometry("925x530+250+100")

def menuExit():
    window.destroy() 

bg = PhotoImage(file="c:/012/.vscode/Project/MINIPROJECT.png")
label = Label(window, image=bg) 
label.place(x=0, y=0, relwidth=1, relheight=1)  # ให้ Label มีขนาดเท่ากับหน้าต่าง

text = Label(window, text="MINIPROJECT", font=("Minecraft Ten", 45),bg="lightgray")
text.place(relx=0.52, rely=0.05, anchor="n")  # จัดวางข้อความตรงกลางของหน้าต่าง

def Organizer():
    Organizer = Toplevel(window)
    Organizer.title("Organizer")

    Organizer.mainloop()
    
def menuSorting():
    Sorting = Toplevel(window)
    Sorting.title("Sorting")
    Sorting.geometry("925x530+250+100") 
    bg = PhotoImage(file="c:/012/.vscode/Project/M.png")
    label = Label(Sorting, image=bg) 
    label.place(x=0, y=0, relwidth=1, relheight=1)
    
    def menuExit():
        Sorting.destroy()

    def clear_button_clicked():
        entry.delete(0, 'end')
        result_label.config(text="")    

    def bubble_sort(array):
        for i in range(1, len(array)):
            flag = 0
            for j in range(len(array) - i):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    flag = 1
            if flag == 0:
                break
        return array

    def bubble_array():
        input_array = list(map(int, entry.get().split()))
        sorted_array = bubble_sort(input_array)
        result_label.config(text="จากสูตร bubblesort ผลลัพธ์: " + " ".join(map(str, sorted_array)))

    def insertion_sort(array):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1       
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = key
        return array    

    def insertion_array():
        input_array = list(map(int, entry.get().split()))
        sorted_array = insertion_sort(input_array)
        result_label.config(text="จากสูตร insertionsort ผลลัพธ์: " + " ".join(map(str, sorted_array)))


    def selection_sort(array):
        size = len(array)
        for i in range(size):
            min_index = i
            for j in range(i + 1, size):
                if array[j] < array[min_index]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]
        return array
    
    def selection_array():
        input_array = list(map(int, entry.get().split()))
        sorted_array = selection_sort(input_array)
        result_label.config(text="จากสูตร selectionsort ผลลัพธ์: " + " ".join(map(str, sorted_array)))

    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            merge_sort(left_half)
            merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        return arr        

    def merge_array():
        input_array = list(map(int, entry.get().split()))
        sorted_array = merge_sort(input_array)
        result_label.config(text="จากสูตร mergesort ผลลัพธ์ : " + " ".join(map(str, sorted_array)))                

    entry = Entry(Sorting, font=("Helvetica", 14))
    entry.place(relx=0.5, rely=0.2, anchor="n")

    result_label = Label(Sorting, text="", font=("Helvetica", 14))
    result_label.place(relx=0.5, rely=0.5, anchor="n") 

    sort_var = StringVar()
    sort_var.set(" ")

    buttonBubble = Button(Sorting, text="  Bubble Sort ", font=("Minecraft", 14), fg="white", bg="#93908F", command=bubble_array)
    buttonBubble.place(relx=0.18, rely=0.8, anchor="n")

    buttonInsertion = Button(Sorting, text="  Insertion Sort  ", font=("Minecraft", 14), fg="white", bg="#93908F", command=insertion_array)
    buttonInsertion.place(relx=0.40, rely=0.8, anchor="n")

    buttonSelection = Button(Sorting, text=" Selection Sort ", font=("Minecraft", 14), fg="white", bg="#93908F", command=selection_array)
    buttonSelection.place(relx=0.64, rely=0.8, anchor="n")

    buttonMerge = Button(Sorting, text="  Merge Sort  ", font=("Minecraft", 14), fg="white", bg="#93908F", command=merge_array)
    buttonMerge.place(relx=0.85, rely=0.8, anchor="n")

    buttonDelSe = Button(Sorting, text="   Reset Data   ", font=("Minecraft", 14), fg="white", bg="#93908F", command=clear_button_clicked)
    buttonDelSe.place(relx=0.64, rely=0.9, anchor="n")

    buttonOutSe = Button(Sorting, text="     Cancel    ", font=("Minecraft", 14), fg="white", bg="#93908F", command=menuExit)
    buttonOutSe.place(relx=0.85, rely=0.9, anchor="n")

    Sorting.mainloop()

def menuSearching():#สร้างหน้าต่างSearching
    Searching = Toplevel(window)
    Searching.title("Searching")
    Searching.geometry("925x530+250+100")
    bg = PhotoImage(file="c:/012/.vscode/Project/M.png")
    label = Label(Searching, image=bg)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    def menuExit():
        Searching.destroy()

    def sequential_search():
        target = int(entry.get())
        found = False

        for i in range(len(numbers)):
            if numbers[i] == target:
                result_label.config(text=f"พบ {target} ที่ตำแหน่ง {i}")
                found = True
                break

        if not found:
            result_label.config(text=f"{target} ไม่พบในรายการ")

    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search_button_clicked():
        target = int(entry.get())
        index = binary_search(numbers, target)
        if index != -1:
            result_label.config(text=f"ค้นพบค่า {target} ที่ตำแหน่ง {index} ในฐานข้อมูล")
        else:
            result_label.config(text=f"ไม่พบค่า {target} ในฐานข้อมูล")

    def clear_button_clicked():
        entry.delete(0, 'end')
        result_label.config(text="")

    # สร้างอาเรย์ตัวอย่าง
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    entry = Entry(Searching, font=("Helvetica", 18))
    entry.pack(padx=20,pady=100)

    result_label = Label(Searching, text="", font=("Helvetica", 16))
    result_label.pack(pady=10)           

    buttonSeq = Button(Searching, text=" SequentialSearch ", font=("Minecraft", 14),command=sequential_search,fg="white", bg="#93908F")
    buttonSeq.place(relx=0.39, rely=0.8, anchor="n")
    buttonSeq.bind("<Enter>", lambda event, btn=buttonSeq: btn.config(bg="gray"))
    buttonSeq.bind("<Leave>", lambda event, btn=buttonSeq: btn.config(bg="#93908F"))

    buttonBin = Button(Searching, text="  BinarySearch  ", font=("Minecraft", 14),command=search_button_clicked,fg="white", bg="#93908F")
    buttonBin.place(relx=0.65, rely=0.8, anchor="n")
    buttonBin.bind("<Enter>", lambda event, btn=buttonBin: btn.config(bg="gray"))
    buttonBin.bind("<Leave>", lambda event, btn=buttonBin: btn.config(bg="#93908F")) 

    buttonDelSe = Button(Searching, text="     Reset Data     ", font=("Minecraft", 14),fg="white", bg="#93908F",command=clear_button_clicked)
    buttonDelSe.place(relx=0.39, rely=0.9, anchor="n")
    buttonDelSe.bind("<Enter>", lambda event, btn=buttonDelSe: btn.config(bg="gray"))
    buttonDelSe.bind("<Leave>", lambda event, btn=buttonDelSe: btn.config(bg="#93908F")) 

    buttonCancel = Button(Searching, text=" Cancel ", font=("Minecraft", 14),command=menuExit,fg="white", bg="#93908F")
    buttonCancel.place(relx=0.69, rely=0.9, anchor="n")
    buttonCancel.bind("<Enter>", lambda event, btn=buttonCancel: btn.config(bg="gray"))
    buttonCancel.bind("<Leave>", lambda event, btn=buttonCancel: btn.config(bg="#93908F"))

    Searching.mainloop() 

button1 = Button(window, text="           Sorting           ", font=("Minecraft", 18),fg="white",command=menuSorting, bg="#93908F")
button1.place(relx=0.52, rely=0.5, anchor="n")
button1.bind("<Enter>", lambda event, btn=button1: btn.config(bg="gray"))
button1.bind("<Leave>", lambda event, btn=button1: btn.config(bg="#93908F"))

button2 = Button(window, text="          Searching         ", font=("Minecraft", 18),fg="white",command=menuSearching, bg="#93908F")
button2.place(relx=0.52, rely=0.61, anchor="n")
button2.bind("<Enter>", lambda event, btn=button2: btn.config(bg="gray"))
button2.bind("<Leave>", lambda event, btn=button2: btn.config(bg="#93908F"))

button3 = Button(window, text=" Organizer ", font=("Minecraft", 17),fg="white", bg="#93908F",command=Organizer)
button3.place(relx=0.43, rely=0.75, anchor="n")
button3.bind("<Enter>", lambda event, btn=button3: btn.config(bg="gray"))
button3.bind("<Leave>", lambda event, btn=button3: btn.config(bg="#93908F"))

button4 = Button(window, text=" Quit game ", font=("Minecraft", 17),fg="white",command = menuExit, bg="#93908F")
button4.place(relx=0.62, rely=0.75, anchor="n")
button4.bind("<Enter>", lambda event, btn=button4: btn.config(bg="gray"))
button4.bind("<Leave>", lambda event, btn=button4: btn.config(bg="#93908F"))

window.grid_rowconfigure(2, weight=1)  

window.mainloop()