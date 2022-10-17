sensitive_character = '你好' #敏感词库
test_sentence = input('请输入一段话：')
#遍历输入的字符是存在敏感词库中
for i in sensitive_character:
    if i in test_sentence:   #判断是否包含敏感词
        test_sentence = test_sentence.replace(i,'*')
print(test_sentence)