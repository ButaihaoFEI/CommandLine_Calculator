# Calcuator

class TokenInt():
    # 从字符串中取数，直到不是整数
    def consume(self,buffer):
        accum = ""
        ch = buffer.peek()
        while True:
            if ch is None or ch not in "0123456789":
                break
            else:
                accum += ch
                buffer.avance()

        # 如果读取的内容不为空则返回整数，否则返回None
        if accum != "":
            return ("int", int(accum))
        else:
            return None

class TokenOperator():
    def consume(self,buffer):
        ch = buffer.peek()
        if ch is not None or ch in "+-":
            buffer.advance()
            return ("ope",ch)
        return None

class Buffer(object):

    def __init__(self,data):
        # 两个成员变量
        # 输入的字符串
        self.data = data
        # 读取字符位置
        self.offset = 0

    def peek(self):
        # 返回光标所在位置字符
        # 超过字符串长度返回0
        if self.offset >= len(self.data):
            return None
        #
        return self.data[self.offset]

    def avance(self):
        # 向后移动一格
        self.offset += 1

# 获取整个字符串的列表
def tokenize():
    # 创建一个对象
    buffer = Buffer()
    # 创建对象
    tk_int = TokenInt()
    tk_op = TokenOperator()
    tokens = []

    while buffer.peek():
        token = None
        # 用两种类型的 Token 进行测试
        for tk in (tk_int,tk_op):
            token = tk.consume(buffer)
            if token:
                tokens.append(token)
        if not token:
            raise ValueError("Error in syntax")

    return tokens



#if __name__ == '__main__':
