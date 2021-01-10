import functools as func
import operator

'''
For example, consider just the first seven characters of FBFBBFFRLR:

    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.
'''
row_start_number=0
row_end_number=127

seat_start_number=0
seat_end_number=7


ticket_code = 'FBFBBFFRLR'

static_row = len('FBFBBFF')

def get_row_seat_details(passcode):
    counter=0
    s_start_number=0
    s_end_number=7
    row_start_number=0
    row_end_number=127
    seat_start_number=0
    seat_end_number=7
    rownumber=0
    seat_number=0
    start_number=0
    end_number=0
    for code in passcode:

        counter +=1

        if code == 'F':
            end_number = row_start_number + round((row_end_number-row_start_number)/2)-1
            start_number = row_start_number
        elif code == 'B':
            start_number =row_end_number - round((row_end_number-row_start_number)/2)+1
            end_number =row_end_number

        if static_row == counter:
            if code == 'F':
                rownumber=start_number
            elif code == 'B':
                rownumber= end_number

        if code == 'L':
            s_end_number = seat_start_number + round((seat_end_number-seat_start_number)/2)-1
            s_start_number = seat_start_number
            #print(s_start_number,s_end_number,seat_start_number,seat_end_number)
        elif code == 'R':
            s_start_number =seat_end_number - round((seat_end_number-seat_start_number)/2)+1
            s_end_number =seat_end_number
           # print(s_start_number,s_end_number,seat_start_number,seat_end_number)

        if counter == 10:
            if code =='L':
                seat_number = s_start_number
            elif code == 'R':
                seat_number = s_end_number

        row_start_number=start_number
        row_end_number=end_number
        seat_start_number=s_start_number
        seat_end_number=s_end_number

    return (rownumber * 8) + seat_number

#print(get_row_seat_details('FBFBBFFRLR'))

inputfile=open(r'D:\Learning\python\AdventofCode\Day5\input.txt').read()


def main():
    final_list=[]
    inputfile=open(r'D:\Learning\python\AdventofCode\Day5\input.txt').read()

    for res in inputfile.split('\n'):
        ticket_number= get_row_seat_details(res)
        final_list.append(ticket_number)

    return max(final_list)

if __name__=="__main__":
    max_value=main()
    print(max_value)

