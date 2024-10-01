



# draw_quare('*', 4)
#
#        ****
#        *  *
#        *  *
#        ****


def draw_square(sign, number_of_signs):
    print(sign*number_of_signs)
    count=number_of_signs
    while count>2:
        spaces=' '*(number_of_signs-2)
        print(sign + spaces + sign)
        count=count-1
    print(sign * number_of_signs)




# draw_rhombus(7)

#   .
#  / \
# /   \
#.     .
# \   /
#  \ /
#   .

def draw_rhombus(diameter):
    # draw top dot
    spaces_before_top_dot=int((diameter-1)/2)
    print(spaces_before_top_dot*' ' + '.')

    spaces_before_slash=spaces_before_top_dot-1
    spaces_before_backslash=1
    while spaces_before_slash>0:
        print(spaces_before_slash*' ' + '/' + spaces_before_backslash*' ' + '\\')
        spaces_before_slash-=1    # spaces_before_slash=spaces_before_slash-1
        spaces_before_backslash+=2

    spaces=(diameter-2)*' '
    print('.' + spaces + '.')
    spaces_before_backslash=1
    spaces_before_slash=diameter-4
    while spaces_before_slash>0:
        print(spaces_before_backslash*' ' + '\\' + spaces_before_slash*' ' + '/')
        spaces_before_slash-=2    # spaces_before_slash=spaces_before_slash-1
        spaces_before_backslash+=1
    print(spaces_before_top_dot * ' ' + '.')
draw_square('*', 8)
draw_rhombus(11)



