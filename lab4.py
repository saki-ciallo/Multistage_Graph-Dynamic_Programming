class Note:
    def __init__(self, number):
        self.number = number
        self.next = []
        self.cost = []


print("请输入创建节点的数量：")
n = int(input())  # 用于创建节点的循环判断
print(n)
node_list = []  # 保存Note节点指针，同时可len()计算结点数

for i in range(0, n):
    node_list.append(Note(i))
    print("请输入节点%d的出度数量：" % i)
    out_degree = int(input())

    if out_degree != 0:
        # 只允许有出度的节点执行以下生成代码
        print("确认出度数：%d" % out_degree)
        print("节点%d的出度对应节点：" % i)
        vertex = input().split()
        if vertex != 0:
            node_list[i].next = [int(vertex[p]) for p in range(len(vertex))]
        print("请输入权值：")
        weight = input().split()
        if weight != 0:
            node_list[i].cost = [int(weight[p]) for p in range(len(weight))]


path = [0] * n
cost = [0] * n  # 新的开销都默认为0

# 自底向上
for i in range(n - 2, -1, -1):  # 10个节点，9号节点是目标，从8号开始计算
    # 计算最短路径长度
    k = len(node_list[i].next)  # 用作循环判断次数
    temp_cost_list = []
    for x in range(k):
        # 节点出度数量的循环
        next2count = node_list[i].next[x]  # 记录当前节点的对应下个节点的值
        temp_cost = node_list[i].cost[x] + cost[next2count]  # cost使用值可确保开销对应计算
        temp_cost_list.append(temp_cost)
    temp_cost = min(temp_cost_list)  # 当节点i最小开销
    cost[i] = temp_cost  # 将当节点最低开销记录到cost列表，其下标i是节点号
    # 最短计算值的NODE
    a = temp_cost_list.index(temp_cost)  # 开销的下标对应next的节点下标
    temp_cost_node = node_list[i].next[a]  # 获得next下标的值
    temp_cost_index = node_list[i].next.index(temp_cost_node)  # 节点i最小开销的下标
    temp_next = node_list[i].next[temp_cost_index]  # 保存最小开销指向的节点
    path[i] = temp_next

print(cost)
print(path)


def show_path():
    temp_list = [0]  # 默认从节点0开始
    i = 0
    while i < n - 1:
        temp = path[i]
        temp_list.append(temp)
        i = temp
    print(temp_list)
    print("%d" % temp_list[0], end="")
    for i in range(len(temp_list)):
        print("->%d" % temp_list[i], end="")
    print("")  # 空一行好看用


def main():
    show_path()


if __name__ == "__main__":
    main()
