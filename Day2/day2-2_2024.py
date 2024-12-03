"""

[DAY2] Part2

~안전한 데이터 규칙~
- if 숫자들이 모두 증가 or 감소하는 흐름, safe, unsafe
- if 이웃하는 숫자 사이의 차이가 1 <= 3, safe, unsafe
- +(추가)+ 한 개의 값을 제거하여 위 2개의 규칙을 만족할 수 있는 경우, safe, unsafe 

- true 데이터 개수 출력

(1) 각 행마다 이웃하는 숫자의 차이 도출
(2) 도출한 차이값들이 모두 양수(증가) OR 음수(감소)를 만족하는지 검사
(3) (2)를 통과한 차이값들이 1 <= 3 을 만족하는지 검사
(4) (2), (3)을 만족하지 못한 데이터에서 한 개의 값을 제거했을 때 규칙을 만족하는지 검사
(4) 만족하는 데이터의 개수 출력

"""



# 파일을 숫자 리스트로 반환
def read_data(file_path):

    with open(file_path, 'r') as file:
        data = []
        for line in file: 
            dataline = list(map(int, line.split()))
            data.append(dataline)
    return data

# 데이터가 안전한지
def data_check_1(dataline):
    differences = []
    
    for i in range(len(dataline)-1):
        difference = dataline[i + 1] - dataline[i]
        differences.append(difference)
    
    # if 숫자들이 모두 증가 or 감소하는 흐름, safe, unsafe
    # all() : 모든 요소가 True인지 확인
    # 차이값이 모두 양수?
    increasing = all(num > 0 for num in differences)
    # 차이값이 모두 음수?
    decreasing = all(num < 0 for num in differences)
    if not (increasing | decreasing):
        # unsafe(false) data
        return False

    # if 이웃하는 숫자 사이의 차이가 1 <= 3, safe, unsafe
    safe_dataline = all(1 <= abs(num) <= 3 for num in differences)
    # safe(true) data
    return safe_dataline

# safe data 변환 가능 여부 (새로 적용된 규칙)
def data_check_2(dataline):

    # safe data
    if data_check_1(dataline):
        return True
    
    # unsafe data일 경우, 숫자를 하나씩 제거하여 safe data로 변환할 수 있는지 검사
    for i in range(len(dataline)):
        # !! 슬라이싱 순서에 따라서 값 달라짐, 순서에 유의 !!
        transeformation = dataline[:i] + dataline[i+1:]
        if data_check_1(transeformation):
            # safe(true) data
            return True
    # unsafe(false) data
    return False

def safe_count(data):
    # if 검사한 행이 안전할 경우(data_check에서 true 반환), +1, pass
    count = sum(1 for dataline in data if data_check_2(dataline))
    return count

if __name__ == "__main__":

    file_path = "day2_2024_input.txt"
    reports = read_data(file_path)
    result = safe_count(reports)

    print(result)
