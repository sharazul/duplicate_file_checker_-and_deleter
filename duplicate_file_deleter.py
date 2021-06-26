# write your code here
import sys
import os
import hashlib


# function to delete duplicates files
def files_delete(numbering_dict, serial):
    size_list = []
    for serial_no in serial:
        for key, value in numbering_dict.items():
            if int(serial_no) == key:
                path = numbering_dict[key]
                size_of_file = os.path.getsize(path)
                size_list.append(size_of_file)
                os.remove(path)
    total = sum(size_list)
    print('Total freed up space: {} bytes'.format(total))

# check for same hash in files
def hash_check(full_dict):
    s = 0
    sum_list = []
    delete_dict = {}
    for key, value in full_dict.items():
        if len(value) > 1:
            print('')
            print(str(key) + ' ' + 'bytes')
            hash_dict = {}
            # iterating over the list of path in the dictionary
            for i in value:
                path = i[0]
                # getting hash value by entering the path of file
                h = hashlib.md5()
                with open(path, 'rb') as file:
                    chunk = file.read()
                    h.update(chunk)
                    insert = h.hexdigest()
                    # hexdigest() function returns hash in hex format
                    # insert hash with path in dictionary
                    hash_dict[path] = insert
            # getting all hash values in a list
            hash_lst1 = [val for val in hash_dict.values()]
            # remove the duplicate from hash_list1
            hash_lst2 = []
            for i in hash_lst1:
                if i not in hash_lst2:
                    hash_lst2.append(i)
            # compare every hash from list in dictionary
            for i in hash_lst2:
                # hash_list3 gets empty after each iteration
                hash_list3 = []
                for paths, values in hash_dict.items():
                    # compare hash in the dictionary
                    if i == hash_dict[paths]:
                        hash_list3.append(paths)
                if len(hash_list3) > 1:
                    print('Hash: {}'.format(i))
                    for only_path in hash_list3:
                        s = s + 1
                        sum_list.append(str(s))
                        delete_dict[s] = only_path
                        print('{}. {}'.format(s, only_path))
            print('')
    q_bool = True
    print('Delete files?')
    conformation = input()
    if conformation == 'yes':
        while q_bool:
            print('')
            print('Enter file numbers to delete:')
            file_input = [x for x in input().split()]
            if len(file_input) == 0:
                print('Wrong format')
                print('')
            else:
                for i in file_input:
                    if i not in sum_list:
                        print('Wrong format')
                        print('')
                        break
                    elif i == file_input[-1] and i in sum_list:
                        q_bool = False
                        files_delete(delete_dict, file_input)
    else:
        print('Wrong option')
        exit()


# function to check duplicate file
def duplicate_checker(path_0, sort, format, bool_0):
    check = 'yes'
    file_dict = {}
    for (root, dirs, files) in os.walk(path_0, topdown=bool_0):
        for x in files:
            extensions = os.path.splitext(x)
            # if format is provided
            if format == 1:
                if input_format == extensions[1]:
                    file_path = os.path.join(root, x)
                    size_in_bytes = os.path.getsize(file_path)
                    if size_in_bytes not in file_dict.keys():
                        file_dict[size_in_bytes] = [[file_path]]
                    else:
                        file_dict[size_in_bytes].append([file_path])
            # if format is not provided
            else:
                file_path = os.path.join(root, x)
                size_in_bytes = os.path.getsize(file_path)
                if size_in_bytes not in file_dict.keys():
                    file_dict[size_in_bytes] = [[file_path]]
                else:
                    file_dict[size_in_bytes].append([file_path])
    # sort the dictionary in Ascending order
    if sort == 2:
        new_dic1 = {k: v for k, v in sorted(file_dict.items())}
        for k, v in new_dic1.items():
            if len(v) > 1:
                print('{} bytes'.format(k))
                for only_path in v:
                    print(only_path[0])
                print('')

        while check == 'yes':
            print("")
            print("Check for duplicates?")
            check = input()
            if check == 'yes':
                hash_check(new_dic1)
            else:
                exit()
    # sorted dictionary in descending order
    elif sort == 1:
        new_dic2 = {k: v for k, v in sorted(file_dict.items(), reverse=True)}
        for k, v in new_dic2.items():
            if len(v) > 1:
                print('{} bytes'.format(k))
                for only_path in v:
                    print(only_path[0])
                print('')

        while check == 'yes':
            print("")
            print("Check for duplicates?")
            check = input()
            if check == 'yes':
                hash_check(new_dic2)
            else:
                exit()


# start from here
arg = sys.argv
arg_1 = ' '.join(arg[1:])
sorting_option = 1
if len(arg) < 2:
    print("Directory is not specified")
else:
    print(' ')
    print("Enter file format:")
    input_format = '.' + input(">")
    print('')
    print("Size sorting options:")
    print("1. Descending")
    print("2. Ascending")
    while sorting_option == 1 or sorting_option == 2:  # check here
        print('')
        print("Enter a sorting option:")
        sorting_option = int(input(">"))
        if sorting_option == 1:
            if len(input_format) > 1:
                duplicate_checker(arg_1, sorting_option, 1, False)
            else:
                duplicate_checker(arg_1, sorting_option, 0, False)
        elif sorting_option == 2:
            if len(input_format) > 1:
                duplicate_checker(arg_1, sorting_option, 1, True)
            else:
                n = 2
                duplicate_checker(arg_1, sorting_option, 0, True)
        else:
            print('')
            print("Wrong option")
