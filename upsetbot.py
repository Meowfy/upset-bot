from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_path = r"/usr/bin/chromedriver"
driver = webdriver.Chrome(chrome_path)
driver.get("https://mugen.saltybet.com/authenticate?signin=1")


loginEmail = open("/home/meowfy/Coding/upsetbot/loginemail", "r")
loginPass = open("/home/meowfy/Coding/upsetbot/loginpass", "r")

#twitchUser = open("twitchuser.txt", "r")
#twitchPass = open("twitchpass.txt", "r")

emailInput = driver.find_element_by_xpath("""//*[@id="email"]""")
emailInput.send_keys(loginEmail.read())

passwordInput = driver.find_element_by_xpath("""//*[@id="pword"]""")
passwordInput.send_keys(loginPass.read())

findStats = WebDriverWait(driver, 90000).until(EC.text_to_be_present_in_element((By.XPATH, """//*[@id="bettors1"]/p[2]"""), "Win rate"))

player1 = driver.find_element_by_xpath("""//*[@id="bettors1"]/p[2]""")
player2 = driver.find_element_by_xpath("""//*[@id="bettors2"]/p[2]""")

player1Winrate = player1.text
player2Winrate = player2.text

matchCounter = 0

#mode = WebDriverWait(driver, 900).until(EC.text_to_be_present_in_element(By.XPATH, """//*[@id="tournament-note"]"""))


#For some reason commenting this out makes it work???????????????????????
#signin = driver.find_element_by_xpath("""//*[@id="signinform"]/div[3]/div/span/input""")
#signin.click()

"""TWITCH LOGIN, FIX LATER"""

#this logs me into twitch, then enables dark mode
#twitchChat = driver.find_element_by_xpath("""//*[@id="ember1157"]/div[3]/button""")
#twitchLogin = driver.find_element_by_xpath("""//*[@id="loginForm"]/div[3]/button/span""")
#twitchChat.click()
#nvm its broken

#twitchUinput = driver.find_element_by_xpath("""//*[@id="username"]""")
#twitchUinput.send_keys(twitchUser.read())

#twitchPinput = driver.find_element_by_xpath("""//*[@id="password"]/input""")
#twitchPinput.send_keys(twitchPass.read())

#twitchLogin.click()

"""AUTO VOLUME MUTE"""

#isnt working, not sure why
#driver.implicitly_wait(5)
#volume = driver.find_element_by_xpath("""//*[@id="js-player-volume"]/div/button""")
#volume.click()

#right as i began to test this out, evo happened. this switches to the mugen servers
#cog = driver.find_element_by_xpath("""//*[@id="header"]/div/div[2]/ul/li[8]/div/span""")
#cog.click()

#mugen = driver.find_element_by_xpath("""//*[@id="header"]/div/div[2]/ul/li[8]/div/ul/li[16]/a""")
#mugen.click()

#checks mode to determine which logic to run
mode = driver.find_element_by_xpath("""//*[@id="footer"]/div[3]""")
modeCheck = mode.text
exhibsChecker = modeCheck.find("exhibition" or "Exhibition")
mmChecker = modeCheck.find("until")
#exhibsChecker1 = driver.find_element_by_xpath("""//*[@id="footer-alert"]""")
#exhibsChecker2 = driver.find_element_by_xpath("""//*[@id="footer-alert"]""")
#exhib checker
if exhibsChecker != -1:
    exhibs = True
else:
    exhibs = False

if mmChecker != -1:
    exhibs = False
else:
    exhibs = True

#turns on if exhibs are active
while exhibs == True:

    findStats = WebDriverWait(driver, 90000).until(EC.text_to_be_present_in_element((By.XPATH, """//*[@id="bettors1"]/p[2]"""), "Win rate"))


    player1 = driver.find_element_by_xpath("""//*[@id="bettors1"]/p[2]""")
    player2 = driver.find_element_by_xpath("""//*[@id="bettors2"]/p[2]""")

    player1Winrate = player1.text
    player2Winrate = player2.text

    salt = driver.find_element_by_xpath("""//*[@id="balancewrapper"]/span[1]""")
    salt = salt.text

    exhibsChecker1 = player1Winrate.find('/')
    exhibsChecker2 = player2Winrate.find('/')

    if exhibsChecker != -1:
        exhibs = True
    else:
        exhibs = False


    wager = driver.find_element_by_xpath("""//*[@id="wager"]""")
    wager.send_keys("5000")

    player1Bet = driver.find_element_by_xpath("""//*[@id="player1"]""")
    player2Bet = driver.find_element_by_xpath("""//*[@id="player2"]""")

    print("------------------------")
    matchCounter += 1
    print("Match " + str(matchCounter))
    print("Exhibs are ON")

    print(player1Winrate+ " - Red Team")
    print(player2Winrate+ " - Blue Team")
    print("------")


    if exhibsChecker1 != -1:
        t1p1 = float(player1Winrate[9:-6])
        t1p2 = float(player1Winrate[14:-1])
    else:
        t1p1 = float(player1Winrate[9:-1])

    if exhibsChecker2 != -1:
        t2p1 = float(player2Winrate[9:-6])
        t2p2 = float(player2Winrate[14:-1])
    else:
        t2p1 = float(player2Winrate[9:-1])

    if exhibsChecker1 != -1:
        avg1 = int(t1p1) + int(t1p2)
        avg1 = float(avg1) / 2
    else:
        avg1 = int(t1p1)

    if exhibsChecker2 != -1:
        avg2 = int(t2p1) + int(t2p2)
        avg2 = float(avg2) / 2
    else:
        avg2 = int(t2p1)

    if avg1 < avg2:
        print("Betting upset, RED TEAM")
        player1Bet.click()
    else:
        print("Betting upset, BLUE TEAM")
        player2Bet.click()

    print("You have " + str(salt))
    print("------------------------")


    if exhibsChecker != -1:
        exhibs = True
    else:
        exhibs = False

    time.sleep(60)


#later modified this to turn on if exhibs are NOT active
while exhibs == False:
#this took me hours to figure out how to do
    findStats = WebDriverWait(driver, 90000).until(EC.text_to_be_present_in_element((By.XPATH, """//*[@id="bettors1"]/p[2]"""), "Win rate"))

    mode = driver.find_element_by_xpath("""//*[@id="footer"]/div[3]""")
    modeCheck = mode.text

    #tourney checker
    tourneyMode = driver.find_element_by_xpath("""//*[@id="balancewrapper"]""")
    tourneyC = tourneyMode.text
    tourneyChecker = tourneyC.find('Tournament')
    if tourneyChecker != -1:
        tourney = True
    else:
        tourney = False

    exhibsChecker = modeCheck.find("exhibition" or "Exhibition")
    if exhibsChecker != -1:
        exhibs = True
    else:
        exhibs = False

    player1 = driver.find_element_by_xpath("""//*[@id="bettors1"]/p[2]""")
    player2 = driver.find_element_by_xpath("""//*[@id="bettors2"]/p[2]""")

    player1Winrate = player1.text
    player2Winrate = player2.text


    salt = driver.find_element_by_xpath("""//*[@id="balancewrapper"]/span[1]""")
    salt = salt.text

    #exhibsChecker1 = player1Winrate.find('/')
    #exhibsChecker2 = player2Winrate.find('/')

    #this is used for tourneys only
    AllIn = driver.find_element_by_xpath("""//*[@id="interval10"]""")

    wager = driver.find_element_by_xpath("""//*[@id="wager"]""")
    if tourney == False:
        wager.send_keys("8000")
    else:
        AllIn.click()

    player1Bet = driver.find_element_by_xpath("""//*[@id="player1"]""")
    player2Bet = driver.find_element_by_xpath("""//*[@id="player2"]""")


    print("------------------------")

    matchCounter += 1

    if tourney == False and exhibs == False:
        print("Match " + str(matchCounter))
        print("Exhibs are OFF")
    elif exhibs == True:
        print("Match " + str(matchCounter))
        print("Exhibs are ON")
    else:
        print("Match " + str(matchCounter))
        print("Tourney is ON")

    print(player1Winrate+ " - Red Team")
    print(player2Winrate+ " - Blue Team")
    print("------")

    #if driver.find_element_by_xpath("""//*[@id="tournament-note"]"""):
        #print("tourney mode. All in!")
        #AllIn.click()

#turns win rates into manageable integers
    p1int = float(player1Winrate[9:-1:])
    p2int = float(player2Winrate[9:-1:])

    if p1int < p2int:
        print("Betting upset, RED TEAM")
        player1Bet.click()
    else:
        print("Betting upset, BLUE TEAM")
        player2Bet.click()

    print("You have " + str(salt))
    print("------------------------")



    if exhibsChecker != -1:
        exhibs = True
    else:
        exhibs = False

    time.sleep(60)


#implement/fix if i want to use safe bets
""""elif p1int > 70:
    print("betting safe, red team")
elif p2int > 70:
    print("betting safe, blue team")
elif p1int < 30:
    print("betting safe, blue team")
elif p2int < 30:
    print("betting safe, red team")
else:
    print("betting upset, blue team")"""

#test to see if this commits? am i stupid?
