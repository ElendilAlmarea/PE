import pkg_resources

import pyautogui as auto
from python_imagesearch.imagesearch import imagesearch as search
from python_imagesearch.imagesearch import imagesearcharea as searcharea
import random
import time
from printy import printy
from printy import inputy
from dataclasses import dataclass


auto.FAILSAFE = False

global t1
t1 = 0.1
global t2
t2 = 0.2
global prec
prec = 0.8

# Start utility methods
def onscreen(path, precision=prec):
    return search(path, precision)[0] != -1


def search_to(path):
    pos = search(path)
    if onscreen(path):
        auto.moveTo(pos, duration=random.uniform(t1, t2))
        return pos


def click_key(key):
    auto.keyDown(key)
    time.sleep(random.uniform(0.05, 0.1))
    auto.keyUp(key)


def click_left():
    auto.mouseDown(duration=random.uniform(t1, t2))
    time.sleep(random.uniform(t1, t2))
    auto.mouseUp(duration=random.uniform(t1, t2))


def click_right():
    auto.mouseDown(button="right", duration=random.uniform(t1, t2))
    time.sleep(random.uniform(t1, t2))
    auto.mouseUp(button="right", duration=random.uniform(t1, t2))


def click_to(path, button="left"):
    if onscreen(path):
        auto.moveTo(search(path), duration=random.uniform(t1, t2))
        if button == "left":
            click_left()
        elif button == "right":
            click_right()
# End utility methods


# Start main process
def queue():
    click_to("./captures/find match ready.png")
    while not onscreen("./captures/accept.png"):
        time.sleep(1)
    click_to("./captures/accept.png")
    print("Loading!")
    loading()


def loading():
    while not onscreen("./captures/1-1.png"):
        time.sleep(random.uniform(0.5, 1.5))

    print("Match starting!")
    start()


def start():
    while onscreen("./captures/1-1.png"):
        auto.moveTo(888, 376, duration=random.uniform(t1, t2))
        click_right()
        time.sleep(random.uniform(t1, t2))
    main()


def buy(data):
    for i in data.shop:
        count = 0
        while onscreen(i) and count < 5:
            count += 1
            # if searcharea("./captures/empty_bench_8.png", data.scan_bench_pos[8][0], data.scan_bench_pos[8][1], data.scan_bench_pos[8][2], data.scan_bench_pos[8][3], prec)[0] != -1:
            #     sell(data.board_pos[8][0], data)
            # click_to(i)


def scan_bench(data, bench):
    capt = ["./captures/empty_bench_0.png", "./captures/empty_bench_1.png", "./captures/empty_bench_2.png", "./captures/empty_bench_3.png", "./captures/empty_bench_4.png", "./captures/empty_bench_5.png", "./captures/empty_bench_6.png", "./captures/empty_bench_7.png", "./captures/empty_bench_8.png"]
    for i in bench:
        if searcharea(capt[i], data.scan_bench_pos[i][0], data.scan_bench_pos[i][1], data.scan_bench_pos[i][2], data.scan_bench_pos[i][3], prec)[0] == -1:
            bench[i] = 1


def sell_loot(data):
    new_bench = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    scan_bench(data, new_bench)
    new_bench[0] = 0
    for i in range(0, len(data.bench)):
        if data.bench[i] != new_bench[i]:
            sell(data.bench_pos[i], data)


def search_loot(data):
    auto.moveTo(data.board_pos[3][0], duration=random.uniform(t1, t2))
    click_right()
    time.sleep(1)
    auto.moveTo(data.board_pos[3][6], duration=random.uniform(t1, t2))
    click_right()
    time.sleep(1)
    auto.moveTo(data.board_pos[2][0], duration=random.uniform(t1, t2))
    click_right()
    time.sleep(1)
    auto.moveTo(data.board_pos[2][6], duration=random.uniform(t1, t2))
    click_right()
    time.sleep(1)
    auto.moveTo(data.board_pos[1][0], duration=random.uniform(t1, t2))
    click_right()
    time.sleep(1)
    auto.moveTo(data.board_pos[1][6], duration=random.uniform(t1, t2))
    click_right()
    time.sleep(1)
    auto.moveTo(data.board_pos[0][0], duration=random.uniform(t1, t2))
    click_right()
    time.sleep(1)
    auto.moveTo(data.board_pos[0][6], duration=random.uniform(t1, t2))
    click_right()
    time.sleep(1)
    auto.moveTo(data.opp_board_pos[3][0], duration=random.uniform(t1, t2))
    click_right()
    time.sleep(1)
    auto.moveTo(data.opp_board_pos[3][6], duration=random.uniform(t1, t2))
    click_right()
    time.sleep(1)
    auto.moveTo(data.opp_board_pos[2][0], duration=random.uniform(t1, t2))
    click_right()
    time.sleep(1)
    auto.moveTo(data.opp_board_pos[2][6], duration=random.uniform(t1, t2))
    click_right()
    time.sleep(1)
    auto.moveTo(data.opp_board_pos[1][0], duration=random.uniform(t1, t2))
    click_right()
    time.sleep(1)
    auto.moveTo(data.opp_board_pos[1][6], duration=random.uniform(t1, t2))
    click_right()
    time.sleep(1)
    auto.moveTo(data.opp_board_pos[0][0], duration=random.uniform(t1, t2))
    click_right()
    time.sleep(1)
    auto.moveTo(data.opp_board_pos[0][6], duration=random.uniform(t1, t2))
    click_right()
    time.sleep(1)
    
def sell(pos, data):
    auto.moveTo(pos, duration=random.uniform(t1, t2))
    auto.mouseDown(duration=random.uniform(t1, t2))
    auto.moveTo(data.shop_pos[2], duration=random.uniform(t1, t2))
    auto.mouseUp(duration=random.uniform(t1, t2))

def refresh(data):
    auto.moveTo(data.refresh_pos[0], data.refresh_pos[1], duration=random.uniform(t1, t2))
    click_left()

def buy_xp(data):
    auto.moveTo(data.buy_xp_pos[0], data.buy_xp_pos[1], duration=random.uniform(t1, t2))
    click_left()

def main():
    @dataclass
    class Data:
        bench:          list
        shop:           list
        lanterne_pos:   tuple
        buy_xp_pos:     tuple
        refresh_pos:    tuple
        interest_pos:   list
        bench_pos:      list
        scan_bench_pos: list
        shop_pos:       list
        board_pos:      list
        opp_board_pos:  list
        item_pos:       list
        item_hover_pos: tuple

    count = 0
    bench = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    shop = ["./captures/tristana_shop.png", "./captures/nidalee_shop.png", "./captures/diana_shop.png", "./captures/teemo_shop.png", "./captures/sivir_shop.png", "./captures/yuumi_shop.png"]
    # loot = ["./captures/blue_orb.png", "./captures/gold_orb.png", "./captures/white_orb.png"]
    lanterne_pos = (943, 252)
    buy_xp_pos = (378, 959)
    refresh_pos = (383, 1040)
    item_pos = [(374, 772), (340, 745), (315, 703), (354, 677), (332, 644), (339, 615), (395, 605), (406, 679), (442, 647), (395, 651)]
    item_hover_pos = (207, 271)
    interest_pos = [[371, 509, 447, 579], [386, 445, 460, 515], [400, 381, 478, 458], [418, 326, 486, 396], [433, 273, 503, 336]]
    bench_pos = [(450, 777), (570, 777), (690, 777) , (810, 777), (930, 777), (1050, 777), (1170, 777), (1290, 777), (1410, 777)]
    scan_bench_pos = [[370, 721, 478, 851], [479, 729, 598, 837], [592, 729, 719, 837], [716, 735, 841, 837], [828, 737, 961, 838], [947, 735, 1080, 840], [1062, 736, 1198, 837], [1177, 735, 1320, 837], [1294, 733, 1440, 842]]
    shop_pos = [(575, 980), (780, 980), (985, 980), (1180, 980), (1380, 980)]
    board_pos = [[(560, 440), (680, 440), (800, 440), (920, 440), (1040, 440), (1160, 440), (1280, 440)], [(610, 510), (730, 510), (850, 510), (970, 510), (1090, 510), (1210, 510), (1330, 510)], [(540, 590), (660, 590), (780, 590), (910, 590), (1040, 590), (1160, 590), (1280, 590)], [(580, 670), (710, 670), (840, 670), (970, 670), (1100, 670), (1230, 670), (1360, 670)]]
    opp_board_pos = [[(590, 194), (680, 440), (800, 440), (920, 440), (1040, 440), (1160, 440), (1243, 194)], [(574, 248), (730, 510), (850, 510), (970, 510), (1090, 510), (1210, 510), (1293, 252)], [(563, 308), (660, 590), (780, 590), (910, 590), (1040, 590), (1160, 590), (1304, 299)], [(549, 383), (710, 670), (840, 670), (970, 670), (1100, 670), (1230, 670), (1314, 361)]]
    #opp_board_pos are bs, used to retrive loot
    data = Data(bench, shop, lanterne_pos, buy_xp_pos, refresh_pos, interest_pos, bench_pos, scan_bench_pos, shop_pos, board_pos, opp_board_pos, item_pos, item_hover_pos)
    while not onscreen("./captures/2-4.png"):
        if count == 0 and onscreen("./captures/1-3.png"):
            count = 1
            auto.moveTo(shop_pos[0], duration=random.uniform(t1, t2))
            click_left()
            auto.moveTo(shop_pos[1], duration=random.uniform(t1, t2))
            click_left()
        if count == 1 and onscreen("./captures/1-4.png"):
            count = 2
            time.sleep(25)
            scan_bench(data, data.bench)
            search_loot(data)
            sell_loot(data)
        if count == 2 and onscreen("./captures/2-1.png"):
            count = 3
            sell(data.board_pos[3][3], data)
            sell(data.board_pos[2][3], data)
            sell(data.board_pos[1][3], data)
        buy(data)
        time.sleep(1)
    while onscreen("./captures/2-4.png"):
        auto.moveTo(928, 396, duration=random.uniform(t1, t2))
        click_right()
        time.sleep(random.uniform(t1, t2))
    while not onscreen("./captures/2-7.png"):
        buy(data)
        time.sleep(1)
    while not onscreen("./captures/3-4.png"):
        buy(data)
        while not onscreen("./captures/3-2.png") and searcharea("./captures/orb_interest.png", data.interest_pos[0][0], data.interest_pos[0][1], data.interest_pos[0][2], data.interest_pos[0][3], prec)[0] != -1:
            refresh(data)
            buy(data)
        exit("Success")
    exit("Ah")


def surrender():
    time.sleep(15)

    time.sleep(1)

    while onscreen("./captures/missions ok.png"):
        click_to("./captures/missions ok.png")
        time.sleep(2)
    while onscreen("./captures/skip waiting for stats.png"):
        click_to("./captures/skip waiting for stats.png")
    time.sleep(5)
    while onscreen("./captures/play again.png"):
        click_to("./captures/play again.png")

    time.sleep(10)
    print("Queuing up again!")
    queue()
# End main process


# Start auth + main script
while (1):
    time.sleep(5)
    auto.alert(auto.position())
auto.alert("Press OK when you're in a TFT lobby!\n")
print("Bot started, queuing up!")
queue()

# End auth + main script
