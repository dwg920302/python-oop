from bs4 import BeautifulSoup
import urllib.request
import csv
from urllib.request import urlopen


class MelonMusicA(object):
    url = 'https://www.melon.com/chart/index.htm?dayTime=2021052508'
    header = {'User-Agent': 'Mozilla/5.0'}  # 저는 봇이 아닙니다 준비과정 01

    @staticmethod
    def do_csv():
        modifier01 = urllib.request.Request(MelonMusicA.url, headers=MelonMusicA.header)  # 저는 봇이 아닙니다 준비과정 02
        soup = BeautifulSoup(urlopen(modifier01), "lxml")
        lst50 = soup.select('.lst50,.lst100')

        melon_list = []
        for i in lst50:
            tmp = []
            tmp.append(i.select_one('.rank').text)
            tmp.append(i.select_one('.ellipsis.rank01').a.text)
            tmp.append(i.select_one('.ellipsis.rank02').a.text)
            tmp.append(i.select_one('.ellipsis.rank03').a.text)
            melon_list.append(tmp)

        with open('melon100.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['순위', '아티스트', '곡명', '앨범'])
            writer.writerows(melon_list)
            f.close()

            print('End')

    @staticmethod
    def get_ranking(category, ct_number):
        modifier01 = urllib.request.Request(MelonMusicA.url, headers=MelonMusicA.header)  # 저는 봇이 아닙니다 준비과정 02
        soup = BeautifulSoup(urlopen(modifier01), "lxml")
        cnt = 0
        print(f'----------[{category} RANKING]----------')
        for i in soup.find_all(name='div', attrs=({"class": f"ellipsis rank0{ct_number}"})):
            cnt += 1
            print(f'[{str(cnt)}위] : {i.find("a").text}')

    @staticmethod
    def main():
        melon = MelonMusicA()
        while 1:
            menu = input('[MENU]\n1 = get Ranking / 2 = ??? / 0 = Exit')
            if menu == '1':
                MelonMusicA.get_ranking("SONG", 1)
                MelonMusicA.get_ranking("ARTIST", 2)
            elif menu == '2':
                MelonMusicA.do_csv()
            elif menu == '0':
                print('By2By2~')
                break
            else:
                print('Error')


MelonMusicA.main()
