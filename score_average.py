print("-- 시험 평균점수 프로그램 --")
# 시험 과목 입력
amount = int(input("과목(0:quit): "))
if amount == 0:
    print("-- 종료 --")
    exit()

# 과목 점수 입력
for i in range(1, amount+1):
    print("-- %d 번째 과목 -- "%i)
    score_all = int(input("문제: "))
    score_true = int(input("맞춘 문제: "))
    # 과목 평균점수
    score_average = (score_all / score_true) * 100

all_average = score_average / amount

def Rank(result):
    if result == 100:
        return "A"
    elif 90 <= result < 100:
        return "B"
    elif 80 <= result < 90:
        return "C"
    elif 70 <= result < 80:
        return "D"
    else:
        return "E"
rank = Rank(all_average)
print("-- 시험 결과 --")
print("과목: {}".format(amount))
print("평균점수: {}".format(all_average))
print("등급: {}".format(rank))