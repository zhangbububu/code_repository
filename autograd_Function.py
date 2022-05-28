import torch
from torch.autograd import Function


class EEEEExp(Function):  # 此层计算e^x
    '''

    实现了手动额对两个数的加法进行反向求梯度

    '''

    @staticmethod
    def forward(ctx, i, j):  # 模型前向

        result = i + j

        ctx.save_for_backward(
            result)  # 保存所需内容，以备backward时使用，所需的结果会被保存在saved_tensors元组中；此处仅能保存tensor类型变量，若其余类型变量（Int等），可直接赋予ctx作为成员变量，也可以达到保存效果
        return result

    @staticmethod
    def backward(ctx, grad_output):  # 模型梯度反传

        # result= ctx.saved_tensors     # 取出forward中保存的result

        # print('##back = ',grad_output * result*10)

        return torch.tensor([1.]), torch.tensor([2.])
        # return grad_output * result*10     # 计算梯度并返回


# 尝试使用
x = torch.tensor([1.], requires_grad=True)  # 需要设置tensor的requires_grad属性为True，才会进行梯度反传
y = torch.tensor([2.], requires_grad=True)
ret = EEEEExp.apply(x, y)  # 使用apply方法调用自定义autograd function

print("ret = ", ret)

print(ret.grad_fn.next_functions)
# tensor([2.7183], grad_fn=<ExpBackward>)
ret.backward(torch.tensor([1.]))  # 反传梯度
# print(x.grad)                               # tensor([2.7183])

print(x.grad, y.grad)