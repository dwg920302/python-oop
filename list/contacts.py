''' 이름, 전화번호, 이메일, 주소를 받아서연락처 입력, 출력, 삭제하는 프로그램을 완성하시오. '''


class Contacts(object):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def get_contact(self):
        return f'[주소록] 이름:{self.name}, 전화번호:{self.phone}, 이메일:{self.email}, 주소:{self.address}'

    @staticmethod
    def main():
        ls = []
        while 1:
            systm = input('[Main] 주소록 작성 -> 1 / 모든 주소록 출력 -> 2 / 삭제 -> 3 / 수정 -> 4 / 종료 -> 0]')
            if systm == '0':
                break
            elif systm == '1':
                ls.append(Contacts(input('이름 입력 -> '), input('연락처 입력 -> '), input('이메일 입력 -> '), input('주소 입력 -> ')))
            elif systm == '2':
                for i in ls:
                    print(i.get_contact())
            elif systm == '3':
                del_name = input('주소록을 삭제할 사용자의 이름을 입력 -> ')
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]
            elif systm == '4':
                # 지워버리고 해당 내용물을 다시 추가하는 것으로 수정
                edit_name = input('주소록의 내용물을 변경할 사용자 이름을 입력 -> ')
                for i, j in enumerate(ls):
                    if j.name == edit_name:
                        del ls[i]
                        ls.append(Contacts(edit_name, input('연락처 입력 -> '), input('이메일 입력 -> '), input('주소 입력 -> ')))
            else:
                print('[System] 잘못된 접근')


Contacts.main()
