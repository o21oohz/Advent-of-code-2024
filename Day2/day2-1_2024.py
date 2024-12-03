"""

[DAY2] Part1

~안전한 데이터 규칙~
- if 숫자들이 모두 증가 or 감소하는 흐름, safe, unsafe
- if 이웃하는 숫자 사이의 차이가 1 <= 3, safe, unsafe

- true 데이터 개수 출력

(1) 각 행마다 이웃하는 숫자의 차이 도출
(2) 도출한 차이값들이 모두 양수(증가) OR 음수(감소)를 만족하는지 검사
(3) (2)를 통과한 차이값들이 1 <= 3 을 만족하는지 검사
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
def data_check(dataline):
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

# safe count
def safe_count(data):
    # if 검사한 행이 안전할 경우(data_check에서 true 반환), +1, pass
    count = sum(1 for dataline in data if data_check(dataline))
    return count

if __name__ == "__main__":

    file_path = "day2_2024_input.txt"
    data = read_data(file_path)
    result = safe_count(data)
    
    print(result)
