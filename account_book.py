import csv

income = 0
expense = 0

records = []

while True:
    print("\n=== 가계부 ===")
    print("1. 수입 추가")
    print("2. 지출 추가")
    print("3. 내역 조회")
    print("4. 저장")
    print("5. 종료")

    menu = input("선택 : ")

    if menu == "1":
        money = int(input("수입 금액 : "))
        income += money
        records.append(["수입", money])

    elif menu == "2":
        money = int(input("지출 금액 : "))
        expense += money
        records.append(["지출", money])

    elif menu == "3":
        print("\n내역")

        for r in records:
            print(r[0], r[1])

        print("\n총 수입 :", income)
        print("총 지출 :", expense)
        print("잔액 :", income - expense)

    elif menu == "4":

        with open("account_book.csv",
                  "w",
                  newline="",
                  encoding="utf-8-sig") as f:

            writer = csv.writer(f)

            writer.writerow(["구분", "금액"])

            writer.writerows(records)

        print("저장 완료")

    elif menu == "5":
        break

    else:
        print("잘못 입력")
