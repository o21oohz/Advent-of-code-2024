"""

[DAY1] Part1

(1) left, right 각자 오름차순 정렬
(2) 행마다 차이(절대값) 값 도출
(3) 도출된 값 모두 합산

"""

# 파일을 각각의 리스트로 반환
def read_data(file_path):

    left_list = []
    right_list = []

    # 파일 읽어오기
    with open(file_path, 'r') as file:
        for line in file:
            # map : line.split()로 얻은 문자열 int로 반환
            left, right = map(int, line.split()) 
            # left, right 리스트에 추가
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list

# 두 리스트 간의 총 거리 차이를 계산.
def SortAndDistance_result(left_list, right_list):

    # 정렬
    left_list.sort()
    right_list.sort()

    # zip() : 리스트에서 동일한 인덱스 요소 튜플로 묶어 반환
    # left - right 절대값(abs())를 누적 합산(sum()) 
    result = sum(abs(left - right) for left, right in zip(left_list, right_list))
    return result

if __name__ == "__main__":

    file_path = "day1_2024_input.txt"
    left_list, right_list = read_data(file_path)
    result = SortAndDistance_result(left_list, right_list)

    # 결과 출력
    print(result)
