import argparse
import sys


def eval_string(string):
        start_number = int(string[:string.find('-')].strip())
        end_number = int(string[string.find('-') + 1:string.find(' ')].strip())
        chars = string[string.find(' '):string.find(':')]
        password = string.split(' ')[2]
        return start_number <=password.count(chars.strip()) <= end_number


def eval_string_upd(string):
    start_number = int(string[:string.find('-')].strip())
    end_number = int(string[string.find('-') + 1:string.find(' ')].strip())
    chars = string[string.find(' '):string.find(':')]
    password = string.split(' ')[2]
    return (password[start_number-1] == chars.strip() and password[end_number-1] != chars.strip()) or \
        (password[start_number-1] != chars.strip() and password[end_number-1] == chars.strip())

def main():
    # create the parser
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--file', help='filename to parse')
    ap.add_argument('-p', '--pathname', help='path to parse')

    opts = ap.parse_args()
    print(opts)
    if opts.file:
        file_path = str(opts.pathname) + str(opts.file)
        lines = open(file_path, encoding='utf8').read().strip().split('\n')
        #input = [line.strip() for line in lines ]
        print(sum(eval_string(line) for line in lines))
        print(sum(eval_string_upd(line) for line in lines))

if __name__ == '__main__':
     main()
