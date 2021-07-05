'''ここの中身を書き換える'''
inputpass = 'input.txt'   #入力ファイル名
outputname = 'output.txt' #出力ファイル名
shift = 3                 #ずらす文字数

'''ここより下はいじる必要はありません'''
encryption = ''

textdata = open(inputpass)
lines = textdata.readlines()
textdata.close()

with open (outputname, 'x') as output:
    for data in lines:
        for f in data:
            encryption = chr(ord(f) + shift)
            output.write(encryption)