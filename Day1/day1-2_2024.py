"""

[DAY1] Part2

(1) left의 숫자가 right에서 등장하는 횟수 계산
(2) 해당(left) 숫자 * 등장횟수 누적 합산

"""

from collections import Counter

# 파일을 각각의 리스트로 반환
def read_data(file_path):

    left_list = []
    right_list = []

    # 파일 읽어오기
    with open(file_path, 'r') as file:
        for line in file:
            # map : line.split()로 얻은 문자열 int로 반환
            left, right = map(int, line.split()) 
            # 왼, 오 리스트에 추가
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

# left의 숫자가 right에서 등장하는 횟수 계산 후, 해당(left) 숫자 * 등장횟수 누적 합산
def count_result(left_list, right_list):
    """왼쪽 리스트와 오른쪽 리스트의 유사도 점수를 계산."""

    # 등장횟수 계산
    count = Counter(right_list)

    # 해당(left) 숫자 * 등장횟수
    result = sum(num * count[num] for num in left_list)
    return result

if __name__ == "__main__":

    file_path = "day1_2024_input.txt"
    left_list, right_list = read_data(file_path)
    result = count_result(left_list, right_list)

    print(result)
