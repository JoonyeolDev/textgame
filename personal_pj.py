import random
import time
from rich.console import Console
from rich.table import Table
import os

# 타이핑치는 효과 str
def typing(text):
    for i in range(len(text)):
        print(text[i], end='', flush=True)
        time.sleep(0.03)
    print('')

# 타이핑치는 효과 list
def list_typing(list):
    for item in list:
        typing(item)

def ui_main(text):
    console = Console()
    table = Table(show_header=False, width=53)
    for i in text:
        table.add_row(i)
    return console.print(table)

def ui(user,monster):
    console = Console()
    table = Table(show_header=True)
    table.add_column("Round "+str(round),width=10)
    table.add_column("H P",justify="center",width=10)
    table.add_column("M P",justify="center",width=10)
    table.add_column("Speed",justify="center",width=10)
    table.add_column("Power",justify="center",width=10)
    table.add_column("Magic",justify="center",width=10)

    table.add_row(
        user.name,
        str(user.hp)+" / "+str(user.max_hp),
        str(user.mp)+" / "+str(user.max_mp),
        str(user.speed),
        str(user.power),
        str(user.m_power),

    )
    table.add_row(
        monster.name,
        str(monster.hp)+" / "+str(monster.max_hp),
        "",
        str(monster.speed),
        str(monster.power),
        ""
    )
    return console.print(table)

shape = """
                                                                                                                                
                                                                                                                            ╞╬╖         ╬╗    
                                                                                                                            ╘╬╢║╣╣╕     ╬╣╞╕
                                                                                                                          ╬╬╬╬╬╬╬╬╝    ╬╣╞╞╞╣
                                                                                                                        │╣╬╬╬╝╚┴        │╣╣╬╣
                                                                                                                        ╠╬╬╣┌╓╬╬╬╬╬╬╬╝╫╣╣╬╬
                                                                                                                        └╩╬╬╬╬╬╬╬╬╬╬╬╣╬╬╬╩┴
                                                                                                                            ┴╚╬╬╬╬╬╬╬╬╬╬╬╬╬╗╖╖╖
                                                                                                                            ┤╬╬╬╬╬╬╣╞╠╬╬╬╬╬╬╬╬╬╗
                                                        ╓╦╗╖                                                                └╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╦╗
                                                    ╓╬╣╬╣╣╣╬╬╗                                                            ┌╔╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬┌
                                                    ╣╞╬╬╬╬╬╣╬╬╬╖                                                        ┌╦╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╖
                                                    ╞╬╬╬╬╬╬╬╣╬╣╝                                                        ╠╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╣
                                                    ╘╞╣╬╬╬╬╬╬╬╝                                                        ┌╠╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╣
                                                ┌╓╦╬╬╬╬╬╬╬╬╣╬╬╫╖╖                                                        │╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╣
                                            ┌╦╬╬╣╬╬╬╬╬╬╬╬╬╬╬╣╣╣╬╬╬╫╖                                                    ╚╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╣
╒╖                                          ╓╬╬╣╣╣╬╬╬╬╬╬╬╬╬╬╣╣╬╬╬╬╬╬╖                                                   └╠╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╕
╬╣╬╫╦╦╦╦╦╦╗╗╗╦╦╦╦╦╗╗╗╗╥╥╥╥╥╥╖╖╖╖╖╖╖╖╖╖╖╓╖╬╬╖╫╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╛                                                    ╞╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╗
╘╩╩╩╩╩╬╬╬╬╬╬╬╬╬╬╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╬╝╚╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬                                                     ╞╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╛
                                            ╚╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╛                                                    ╘╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╕
                                                ╠╬╬╬╬╬╬╬╬╬╬╬╣└╬╬╬╬╬╝                                                     ╠╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╣─
                                                ┌╬╬╬╬╬╬╬╬╬╬╬╬╬╬ ╘╚╬╬╝                                                     ┌╬╬╬╬╣╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╣
                                            ┌╦╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬                                                           ╠╬╬╬╣╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╕
                                            ╬╬╬╬╬╬╬╬╬╬╣╬╬╬╬╬╬╬╗                                                          ╞╬╬╬╣╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╣╛
                                            ╔╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╖                                                        └╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╡╠╬╬╬╣
                                            ┌╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╗                                                       ┌╬╬╣╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╣╬╬╬╬╣
                                        ┌╦╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬                                                      ╞╬╬╬╬╬╬╬╬╬╣╩╩╩╬╬╬╬╬╬╬╬╣╞╬╬╬╡
                                        ╓╬╬╬╬╬╬╬╬╬╬╬╝╚╘┴╚╚╬╬╬╬╬╬╬╬╬╬╬╬╖                                                    ╘╬╬╬╬╬╬╬╣║╦╖   ╚╬╬╬╬╬╬╣╬╬╬╣
                                        ╒╬╬╬╬╬╬╬╬╬╬╝        ┴╚╩╬╬╬╬╬╬╬╬╬                                                     ╚╬╬╬╬╬╬╝ ┴╚╩╣╜╫╞╬╬╬╬╬╬╬╬╬╡                     ┌╖
                                    ┤╬╬╣╬╬╬╬╬╬╬              ╚╬╬╬╬╬╬╬╦╬                                                   │╬╬╬╬╝       ╘╩╣╗╖║╝╬╬╬╬╬╣ ┌               │╞╗ ╣╠╖│╫╗
                                    └╠╬╬╬╬╬╬╬╝                 └╚╬╬╬╣╬╬╗                                                  │╬╬╬╣╛          └╞╬╬╬╬╦╗╠╣╫╩╩╬╕╔╤╖      ╔╬╬╣╞╖╬╣╞╬╣┤╬└╒╬╬  ┌╓╢╝╘╗
                                        └╬╬╬╬╬╝                    └╩╬╬╬╬╬╬╫                                                  ┴╬╬╬╗           │╬╬╬╣┴╚╬╝╚╬╬╗╣╖║║╡╚╦╖╒╦╣┤╠╣╞╬╬╣╞╬╣╞╣┌╪╡╬╛╒╬╝┤│││╬
                                        └╬╬╬╣                         ╚╬╬╬╬╬╗                                                 ┴╬╬╬┐           ╘╬╬╝     ╘╚┴╚╩╬╝╝╩╪╗╖╞╢╞╞╢╞╝╞╞╬╝╞╬╬╣╞╣╠╬╝╚╒╗┤││╠─
                                        ╠╬╬╛                            ╚╬╬╬╬╣                                                 ╠╬╬┌          ┤╬╣               ┴╝ ╚╬╝╝╝╚╬╝╗╬╖╦╣║╣╞║║╬╣┤╝┤┤┤╦╝
                                        ┌╦╬╬╬╣                             ╞╬╬╬╣                                             ╔╬╬╬╬╬╬╣        ┌╓╬╬╣╖                              ┴┴╝╝╩╣╖╖╖╥╝╝
                                    ╚╚╚╚╘╘                             ╔╬╬╬╬╝                                             ┴╚╝  └           ╚╝╝╩╬╛
                                                                        ╘╝╝╝╝
"""

class Inform:

    def __init__(self,name=None,job_select=None):
        self.name = name
        self.job_select = job_select

    def input_id(self):
        print("-"*53)
        typing("안녕하세요, 무지성 탑에 어서오세요 !")
        typing("콘솔 창을 최대한 키워주시기 바랍니다.")
        time.sleep(1)
        self.name = input("당신의 이름을 알려주세요 : ")
        while True:
            typing("전사, 마법사, 도적 세가지 직업이 있습니다")
            time.sleep(1)

            console = Console()
            table = Table(show_header=True)
            table.add_column("Class",justify="center",width=10)
            table.add_column("H P",justify="center",width=10)
            table.add_column("M P",justify="center",width=10)
            table.add_column("Power",justify="center",width=10)
            table.add_column("Magic",justify="center",width=10)
            table.add_column("Speed",justify="center",width=10)

            table.add_row("전사","200","10","15","15","10")
            table.add_row("마법사","100","100","5","30","5")
            table.add_row("도적","150","20","10","20","20")

            console.print(table)
            typing("전사는 1, 마법사는 2, 도적는 3으로 선택해주세요")
            self.job_select = input("직업을 정해주세요 : ")
            if self.job_select in ["1", "2", "3"]:
                break
            else: typing("다시 입력해주세요")

    def job(self):
        if self.job_select == "1":
            name = self.name
            lv = 1
            hp = 200
            mp = 10
            power = 15
            m_power = 15
            speed = 10
            user = Character(name, lv, hp, mp, power, m_power, speed)
            return user

        if self.job_select == "2":
            name = self.name
            lv = 1
            hp = 100
            mp = 100
            power = 5
            m_power = 30
            speed = 5
            user = Character(name, lv, hp, mp, power, m_power, speed)
            return user

        if self.job_select == "3":
            name = self.name
            lv = 1
            hp = 100
            mp = 20
            power = 10
            m_power = 20
            speed = 20
            user = Character(name, lv, hp, mp, power, m_power, speed)
            return user

class Character:
    def __init__(self, name, lv, hp, mp, power, m_power, speed):
        self.name = name
        self.lv = lv
        self.max_hp = hp + lv*50
        self.hp = hp + lv*50
        self.max_mp = mp + lv*5
        self.mp = int((mp + lv*5)/2)
        self.power = power + lv
        self.m_power = m_power + lv
        self.speed = speed + lv*10

    def attack(self, other):
        miss = max((other.speed-self.speed*2)/20,0)
        result = random.choices(range(0,2), weights =[miss,1-miss])
        if result == [1]:
            damage = random.randint(self.power -3, self.power +3)
            # self.speed()
            other.hp = max(other.hp - damage, 0)
            text = [f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다."]
            if other.hp == 0:
                text.append(f"{other.name}이(가) 쓰러졌습니다.")
        else :
            text = ["이런 !! 당신의 공격을 몬스터가 피했습니다"]
        return text
    
    def m_attack1(self, other):
        damage = random.randint(self.m_power -2, self.m_power +5)
        other.hp = max(other.hp - damage, 0)
        self.mp = self.mp - 5
        text = [f"{self.name}의 마법 공격! {other.name}에게 {damage}의 데미지를 입혔습니다."]
        if other.hp == 0:
            text.append(f"{other.name}이(가) 쓰러졌습니다.")
        return text

class Monster:

    def __init__(self, lv):
        self.name = "Lv"+str(lv) + " 몬스터"
        self.lv = lv
        self.max_hp = 50 + lv*5
        self.hp = 50 + lv*5
        self.power = 10 + int(lv/5)
        self.speed = 4 + int(lv/2)

    def attack(self, other):
        miss = max((other.speed-self.speed*2)/20,0)
        result = random.choices(range(0,2), weights=[miss,1-miss])
        if result == [1]:
            damage = random.randint(self.power -3, self.power +3)
            # self.speed()
            other.hp = max(other.hp - damage, 0)
            text = [f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다."]
            if other.hp == 0:
                text.append(f"{other.name}이(가) 쓰러졌습니다.")
        else :
            text = ["당신은 몬스터의 공격을 피했습니다 !!"]
        return text

count = 0
while count<=30:
    # 층
    count+=1
    # 1층일 경우 유저정보를 받음
    if count == 1: 
        player = Inform()
        player.input_id()
        user = player.job()
    time.sleep(1)
    os.system('cls')
    # 10층마다 유저 레벨 업
    if count > 20: user.lv = 2
    if count > 30: user.lv = 3
    # 층마다 랩업하는 몬스터 정의
    monster = Monster(count)
    typing("당신은 조심해서 층을 올라갑니다")
    time.sleep(2)
    os.system('cls')
    typing("왠지 불길한 기운이 앞에 있습니다")
    time.sleep(2)
    os.system('cls')
    typing("이런 !! 몬스터를 만났습니다 !")
    typing("전투가 시작됩니다 준비해주세요 !")
    typing("3  .   .   2  .   .   1  .   .   ")
    time.sleep(1)
    os.system('cls')
    # 전투 라운드 정의
    round = 0
    while True:
        round += 1
        print(shape)
        print("-"*36+" %2s 층 "% count +"-"*36)
        ui(user,monster)
        print("-"*79)
        text = ["공격 타입은 물리, 마법이 있습니다",
                "마법공격은 피할 수 없습니다",
                "물리공격은 1, 마법공격은 2을 입력해주세요"
        ]
        list_typing(text)
        # 공격 타입
        while True:
            type = str(input("공격 타입을 선택해주세요 : "))
            if type == "1": 
                if user.speed>=monster.speed:
                    typing(user.attack(monster))
                    if monster.hp>0:
                        typing(monster.attack(user))
                    break
                else : 
                    list_typing([monster.attack(user), user.attack(monster)])
            if type == "2": 
                if user.mp>=5:
                    typing(user.m_attack1(monster))
                    if monster.hp>0:
                        typing(monster.attack(user))
                    break
                else : 
                    typing("MP가 부족합니다 !!")
            typing("다시 입력해주세요")
        # 라운트 끝
        typing(f"마나가 {user.lv}만큼 회복 됩니다")
        time.sleep(1.5)
        user.mp += user.lv
        # 전투 끝
        if user.hp == 0:
            typing("당신은 패배했습니다")
            time.sleep(3)
            break
        if monster.hp == 0:
            os.system('cls')
            typing("전투가 끝났습니다! 당신은 남은 mp를 모두 소비해 체력을 회복했습니다")
            user.hp += int(user.mp/2)
            if user.hp > user.max_hp: user.hp = user.max_hp
            time.sleep(2)
            typing(f"당신의 hp가 {user.mp*2}만큼 회복되었습니다")
            user.mp = int(user.max_mp/2)
            time.sleep(2)
            typing("당신은 다음층으로 올라갑니다...")
            time.sleep(1)
            break
        time.sleep(1)
        os.system('cls')
typing("You Died")