#121910313028
#implementing the parenthesis matching algorithm using stack
open_list = ["[","{","("] 
close_list = ["]","}",")"] 
  
def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
    else: 
        return "Unbalanced"
  
  
string = "{[]{()}}"
print(string,"-", check(string))