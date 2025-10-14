# to-do list python (2)

# 24/9/2024 day-1 # viết code
# 25/9/2024 day-2 # viết code + thêm tính năng (mới)
# 26/9/2024 day-3 # (mốc đánh dấu hoàn thành) vào lúc 22:18 PM

# thời gian: 8 tiếng 31 phút (coding + fix bug)

from termcolor import colored # pyright: ignore[reportMissingImports]
import emoji # pyright: ignore[reportMissingImports]
import time

run=True
list_name=['',]
add_things_to_do=['',]

S=0
mark_done=emoji.emojize(":check_mark_button:")

while run:
    
    one='1.tạo list'
    two='2.xem list'
    example='3.xem mẫu'
    four='4.thoát'

    name='1.đặt tên'
    add='2.add việc để làm'


    print("{:-^30}".format(""))
    print("|{:^28}{:<0}".format("TO-DO LIST",'|'))
    print("{:-^30}".format(""))
    print("|{:^28}{:<0}".format(f"{one}","|"))
    print("|{:^28}{:<0}".format(f"{two}","|"))
    print("|{:^28}{:<0}".format(f"{example}",'|'))
    print("|{:^28}{:<0}".format(f"{four}","|"))
    print("{:-^30}".format(""))

    choose=str(input('chọn:'))
    time.sleep(0.25)

    # tạo list
    if choose =='1':
        print(colored("tip:",'light_blue')+'thoát (X)')
        
        while run:
            
            name='1.đặt tên'
            add='2.add việc để làm'
            delete_all='3.xóa danh sách'
            
            color='green'
            
            print('{:-^30}'.format(""))
            print("|{:<1}{:>19}".format(colored(f"-{one[2:None]}-",f'{color}'),"|"))
            print("|{:^28}{:<0}".format(f"{name}",'|'))
            print("|{:^28}{:<0}".format(f"{add}",'|'))
            print("|{:^28}{:<0}".format(f"{delete_all}",'|'))
            print("{:-^30}".format(""))

            option=str(input('chọn:'))
            time.sleep(0.25)

            # đặt tên
            if option =='1':
                
                if S==1:
                    
                    limit='vượt quá số lần đặt'
                    
                    for i in range(len(limit)):
                        print(limit[i],flush=True,end='')
                        time.sleep(0.02)
                    print()
                    time.sleep(0.4)
                
                if S < 1:
                    
                    print(colored("tip:",'light_blue')+"để có thể đặt list mới thì xóa list cũ")
                    print("đặt tên cho list:")
                    
                    name_for_list=str(input())
                    list_name.append(name_for_list)
                    S+=1
            
            # add việc cần làm
            if option=='2':
                
                if list_name==[""]:
                    print("bạn chưa nhập tên list")
                
                elif len(list_name) >=2:
                    
                    print(colored("Tip:",'light_blue') +"dừng bấm (x)")
                    print('add việc cần làm:')
                    
                    while run:
                        add_input=str(input())
                        if add_input != 'x':
                            add_things_to_do.extend([add_input])
                        elif add_input == 'x':
                            break
                                        
            # xóa tất cả tên và việc làm
            if option=='3':
                list_name.clear()
                add_things_to_do.clear()
                list_name.append("")
                add_things_to_do.append("")
                print("Your list has been deleted !")
                S-=1
            
            # thoát
            if option =='x':
                time.sleep(0.25)
                break
    
    # xem list          
    if choose =="2":
        if add_things_to_do ==['']:
            print("bạn chưa add việc làm")
        
        elif list_name ==['']:
            print('bạn chưa đặt tên cho list')

        elif list_name ==[''] and add_things_to_do==['']:
            print('bạn chưa đặt tên và add việc cần làm')

        else:
            print(colored("tip:",'light_blue')+"thoát (x)")
            while run:
                print(colored("tip:",'light_blue')+"xóa (delete) / đánh dấu hoàn thành (done)")
                
                print("{:-^30}".format(""))
                for i in range(1,len(list_name)):
                    print("|{:^28}{:<10}".format(list_name[i],'|'))
                print("{:-^30}".format(""))
                for i in range(1,len(add_things_to_do)):
                    print("{:<0}".format("•"+add_things_to_do[i]))
                print("{:-^30}".format(""))
    
                choose2=str(input())
                
                # đánh dấu x
                if choose2=='delete':
                    
                    print(colored("tip:",'light_blue')+"thoát (x)")
                    
                    while run:
                        
                        print("{:-^30}".format(""))
                        for i in range(1,len(list_name)):
                            print("|{:^28}{:<0}".format(list_name[i],'|'))
                        print("{:-^30}".format(""))
                        for i in range(1,len(add_things_to_do)):
                            print("{:<0}".format(str(i)+"."+add_things_to_do[i]))
                        print("{:-^30}".format(""))
                        
                        choose3=(input('chọn:'))
                        
                        if choose3 != 'x':
                            add_things_to_do.remove(add_things_to_do[int(choose3)])
                        
                        elif str(choose3)=='x':
                            break 
                
                # đánh dấu hoàn thành
                elif choose2=='done':
                    print(colored("tip:",'light_blue')+"thoát (x)")
                    while run:
                        print("{:-^30}".format(""))
                        for i in range(1,len(list_name)):
                            print("|{:^28}{:<0}".format(list_name[i],"|"))
                        print('{:-^30}'.format(""))
                        for i in range(1,len(add_things_to_do)):
                            print("{:^0}".format(str(i)+"."+add_things_to_do[i]))
                        print("{:-^30}".format(""))
                        while run:
                            mark_done_choose=input("chọn:")
                            if mark_done_choose =="" or mark_done_choose ==" ":
                                continue
                            else:
                                break
                        if mark_done_choose != 'x':
                            if add_things_to_do[int(mark_done_choose)] in add_things_to_do[int(mark_done_choose)]:
                                    add_things_to_do.append(add_things_to_do[int(mark_done_choose)]+mark_done)
                                    add_things_to_do.remove(add_things_to_do[int(mark_done_choose)])
                            else:
                                 add_things_to_do.append(add_things_to_do[int(mark_done_choose)]+mark_done)
                        
                        elif str(mark_done_choose) =='x':
                            break

                elif choose2=='x':
                    break
    
    # xem mẫu                
    if choose == "3":
        while run:
            print("{:-^30}".format(""))
            print("|{:<1}{:>24}".format(colored(f"-{example[6:None].title()}-",f'{color}'),"|"))
            print("|{:^28}{:<0}".format(f"{name[2:]}",'|'))
            print("{:-^30}".format(""))
            for i in range(1,4):
                print("|{:^28}{:<0}".format(f"{add[2:]}","|"))
            print("{:-^30}".format(""))
            
            exit=str(input('nhấn x để thoát:'))
            if exit =='x':
                time.sleep(0.25)
                break
    
    # thoát
    if choose =='4':
        print("bạn có chắc chắn muốn thoát chứ?")
        exit=str(input('YES (y)/NO (n):'))
        if exit=='y':
            run=False
