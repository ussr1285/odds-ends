import os

def count_files(directory):
    """특정 디렉토리의 파일 수를 계산"""
    try:
        # os.listdir()을 사용하여 디렉토리 내의 파일 및 폴더 목록을 가져옴
        return len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])
    except Exception as e:
        print(f"Error: {e}")
        return 0

def print_directory_tree(startpath):
    """디렉토리 트리와 각 디렉토리의 파일 수를 출력, .jpg 파일 제외"""
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        # 디렉토리와 해당 디렉토리의 파일 수 출력
        print(f'{indent}{os.path.basename(root)}/ ({count_files(root)})')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if not f.endswith('.jpg'):
                print(f'{subindent}{f}')

# 사용 예시
print_directory_tree("경로")
