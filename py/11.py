import subprocess
import time


def svn_deep_cleanup(svn_path):
    cleanup_command = f'svn cleanup --remove-unversioned {svn_path}'

    try:
        # 执行深度的SVN cleanup操作
        subprocess.run(cleanup_command, shell=True, check=True)
        print('SVN deep cleanup completed.')
    except subprocess.CalledProcessError as e:
        print(f'Error occurred during deep cleanup: {e}')


def svn_revert(svn_path):
    revert_command = f'svn revert -R {svn_path}'

    try:
        # 执行SVN revert回退操作
        subprocess.run(revert_command, shell=True, check=True)
        print('SVN reverted to initial state.')
    except subprocess.CalledProcessError as e:
        print(f'Error occurred during revert: {e}')


def svn_switch_to_branch(svn_path, branch_name):
    switch_command = f'svn switch ^/{branch_name} {svn_path}'
    print(switch_command)

    try:
        # 执行SVN切换分支的命令
        subprocess.run(switch_command, shell=True, check=True)
        print(f'Switched SVN project to branch: {branch_name}')
    except subprocess.CalledProcessError as e:
        print(f'Error occurred during switch: {e}')


if __name__ == '__main__':
    # SVN项目路径
    svn_project_path = r'F:\trunk'
    # 要切换的目标分支名称
    # target_branch_name = 'branches/rel1130'
    target_branch_name = 'trunk'

    # 执行深度的SVN cleanup操作
    svn_deep_cleanup(svn_project_path)

    # 等待Cleanup完成（你可以根据实际情况设定等待时间）
    time.sleep(5)  # 等待5秒钟

    # 执行SVN revert回退操作
    svn_revert(svn_project_path)

    # 切换到目标分支
    svn_switch_to_branch(svn_project_path, target_branch_name)

