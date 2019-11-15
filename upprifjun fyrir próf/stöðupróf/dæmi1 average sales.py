def open_file(filename):
    fileobject = open(filename, "r")
    my_list = []            ## breyta filenum í lista
    for line in (fileobject):
        my_list.append([int(x) for x in line.strip().split(" ")]) ## breyta öllu í integer og splitta á milli bila,, list comprehension
    return my_list

def organize(my_list):
    print("Average sales:")
    for nr, line in enumerate(my_list):    ## hérna er ég að enumeratea hverja línu í my_list og passa að allt sé ekki í einni linu með forlykkjunni
        nr += 1                             ## passa að enumerateið byrji ekki á 0
        average = sum(line) /len(line)       ## summa hverjar línu deilt með lengdinni af hverri línu
        print("Department no.",str(nr)+":",round(average,1))  ##nota plús þegar ég vil losna við bilin milli lína, því komma gefur mér bil á milli.





def main():
    filename = input("Enter file name: ")
    my_list = open_file(filename)
    organize(my_list)

main()