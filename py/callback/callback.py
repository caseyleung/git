class taskautotest():
    def __init__(self, task_id):
        self.task_id = task_id
        self.task_info = {}

    def get_debuginfo(self, task_id, task_info):
        task_info = {'task_id': task_id, 'task_info': task_info}
        self.task_info.update(task_info)
        # 回调完成时的标志
        self.callback_completed = True

    async def run(self):
        self.callback_completed = False  # 标记回调未完成
        Game.Player.Task.RegisterDebugInfoCallback(self.get_debuginfo)  # 注册回调函数
        Con.send("$task_getdebuginfo {}".format(self.task_id))  # 调用回调函数

        # 等待回调函数完成
        while not self.callback_completed:
            await asyncio.sleep(0.1)  # 等待一段时间再检查标志

# 创建 taskautotest 实例
async def main():
    tt = taskautotest(123)  # 假设任务 ID 为 123
    await tt.run()
    print(tt.task_info)  # 打印任务信息

# 执行异步函数
import asyncio
asyncio.run(main())
