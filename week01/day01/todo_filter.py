tasks = [
    {
        "title": "处理退货",
        "status": "pending",
        "priority": "high",
        "minutes": 30
    },
    {
        "title": "准备周报",
        "status": "pending",
        "priority": "low",
        "minutes": 10
    },
    {
        "title": "核对订单",
        "status": "pending",
        "priority": "high",
        "minutes": 15
    },
    {
        "title": "发送通知",
        "status": "done",
        "priority": "high",
        "minutes": 5
    }
]

# 1. 从任务列表中筛选出符合条件的任务
def filter_tasks(tasks):
    result = []

    for task in tasks:
        if task["status"] == "pending" and task["priority"] == "high":
            result.append(task)

    return result

# 2. 按照 minutes 从小到大排序
def sort_tasks(tasks):
    result = sorted(
        tasks,
        key = lambda task:task["minutes"]
    )
    return result

# 3. 提取每个任务的 title
def extract_tasks(tasks):
    result = [task["title"] for task in tasks]
    return result

# 4. 返回任务名称组成的列表
def pick_todo(tasks):
    # 第一步：筛选任务
    filtered_tasks = filter_tasks(tasks)

    # 第二步：任务排序
    sorted_tasks = sort_tasks(filtered_tasks)

    # 第三步：提取任务名称
    extracted_tasks = extract_tasks(sorted_tasks)

    # 第四步：返回最终结果
    return extracted_tasks

if __name__ == "__main__":
    filtered_tasks = filter_tasks(tasks)

    print("筛选结果：")
    print(filtered_tasks)

    sorted_tasks = sort_tasks(filtered_tasks)

    print("排序结果：")
    for task in sorted_tasks:
        print(task["title"], task["minutes"])

    extracted_tasks = extract_tasks(sorted_tasks)

    print("提取结果：")
    print(extracted_tasks)

    final_result = pick_todo(tasks)

    print("最终结果：", final_result)
    print("返回值类型：", type(final_result))

    # 测试1：正常任务列表
    assert pick_todo(tasks) == ["核对订单", "处理退货"]

    # 测试2：空任务列表
    assert pick_todo([]) == []

    # 测试3：没有符合条件的任务
    test_tasks = [
        {
            "title": "准备周报",
            "status": "pending",
            "priority": "low",
            "minutes": 10
        }
    ]

    assert pick_todo(test_tasks) == []

    print("W1D1 所有测试通过！")