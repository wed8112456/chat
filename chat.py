# 讀取檔案
def read_file(filename):
    chat = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            chat.append(line.strip())
    return chat
    
# 處理檔案
def process(chat):
    newchat = []
    preson = None
    for i in chat:
        if i == 'Allen':
            preson = 'Allen'
            continue
        elif i == 'Tom':
            preson = 'Tom'
            continue
        if preson:
            newchat.append(preson + ': ' + i)
    return newchat

# 寫入新檔案
def write_file(chat):
    with open('output.txt', 'w', encoding='utf-8-sig') as f:
        for i in chat:
            f.write(i+'\n')

# 主main
def main():
    chat = read_file('input.txt')
    chat = process(chat)
    write_file(chat)
    print('輸出完畢')

main()

