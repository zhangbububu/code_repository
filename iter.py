class data:
    list: list = [1, 2, 3, 4, 5, 6]
    index = 0

    def __call__(self, *args, **kwargs):
        item = self.list[self.index]
        self.index += 1
        return item

    def __iter__(self):
        self.i = iter(self.list)
        return self.i


for item in iter(data(), 3):  # 每一次迭代都会调用一次__call__方法,当__call__的返回值等于3是停止迭代
    print(item)