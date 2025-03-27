class RadiationExposureRecord:
    def __init__(self):
        self.records = []  

    def add_record(self, date, exposure_level):
        self.records.append({'date': date, 'exposure_level': exposure_level})
        print(f"기록 추가: 날짜={date}, 노출 수준={exposure_level} mSv")

    def get_exposure_history(self):
        return self.records

    def calculate_average_exposure(self):
        if not self.records:
            return 0
        total_exposure = sum(record['exposure_level'] for record in self.records)
        average_exposure = total_exposure / len(self.records)
        return average_exposure

def main():
    exposure_manager = RadiationExposureRecord()
    
    while True:
        print("\n방사선 노출 기록 관리 프로그램")
        print("1. 기록 추가")
        print("2. 기록 조회")
        print("3. 평균 노출 수준 계산")
        print("4. 종료")
        
        choice = input("원하는 작업을 선택하세요 (1-4): ")
        
        if choice == '1':
            date = input("날짜를 입력하세요 (YYYY-MM-DD): ")
            exposure_level = float(input("노출 수준을 입력하세요 (mSv): "))
            exposure_manager.add_record(date, exposure_level)
        
        elif choice == '2':
            history = exposure_manager.get_exposure_history()
            print("방사선 노출 기록:")
            for record in history:
                print(f"날짜: {record['date']}, 노출 수준: {record['exposure_level']} mSv")
        
        elif choice == '3':
            average_exposure = exposure_manager.calculate_average_exposure()
            print(f"평균 방사선 노출 수준: {average_exposure:.2f} mSv")
        
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()