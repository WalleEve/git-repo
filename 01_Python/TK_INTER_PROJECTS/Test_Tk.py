# toplevel

from tkinter import *

root = Tk()
root.geometry("300x300")

rootLabel = Label(root, text="This is root Lable").pack(padx=10, pady=10)

chdLabel1 = Toplevel(root)
chdLabel1 = Label(chdLabel1, text="This is child Label").pack(padx=10, pady=10)
chdLabel1.transient(root)
root.mainloop()



def tri_recursion(k):
    if ( k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(2)



#incluse <stdio.h>

int fun(int n)
{
    if (n == 0){
        return 1;
    }
    else
        return 7 + fun(n - 2);
}


int main(){
    printf("%d", fun(4));
    return 0;
}
