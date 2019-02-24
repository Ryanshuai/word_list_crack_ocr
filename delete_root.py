from autocorrect import spell


# with open('word_list1.txt', 'r') as f:
#     data = f.readlines()
#
# with open('word_list1_no_root.txt', 'w') as f:
#     for i, line in enumerate(data):
#         if i%2 == 1:
#             print(line)
#         else:
#             f.write(line)


# with open('word_list2.txt', 'r') as f:
#     data = f.readlines()
#
# with open('word_list2_no_root.txt', 'w') as f:
#     for i, line in enumerate(data):
#         if i%3 == 2:
#             print(i, line)
#         else:
#             f.write(line)


# with open('word_list3.txt', 'r') as f:
#     data = f.readlines()
#
# with open('word_list3_no_root.txt', 'w') as f:
#     for i, line in enumerate(data):
#         if i%4 == 3:
#             print(i, line)
#         else:
#             f.write(line)


# with open('word_list4.txt', 'r') as f:
#     data = f.readlines()
#
# with open('word_list4_no_root.txt', 'w') as f:
#     for i, line in enumerate(data):
#         if i%5 == 4:
#             print(i, line)
#         else:
#             f.write(line)


with open('word_list5.txt', 'r') as f:
    data = f.readlines()

with open('word_list5_no_root.txt', 'w') as f:
    counter = 0
    for i, line in enumerate(data):
        for c in ' :0123456789':
            if c in line:
                counter += 1
                print(counter, i, line)
                break
        else:
            f.write(line)

