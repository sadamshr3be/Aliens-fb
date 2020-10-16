import os
os.system('clear')
os.system('printf "\033[3;32m" ')
print('''     ___       __       __   _______ .__   __.      _______.
    /   \     |  |     |  | |   ____||  \ |  |     /       |
   /  ^  \    |  |     |  | |  |__   |   \|  |    |   (----`
  /  /_\  \   |  |     |  | |   __|  |  . `  |     \   \    
 /  _____  \  |  `----.|  | |  |____ |  |\   | .----)   |   
/__/     \__\ |_______||__| |_______||__| \__| |_______/    
                                                            
 __       __  .___________.                                 
|  |     |  | |           |                                 
|  |     |  | `---|  |----`                                 
|  |     |  |     |  |                                      
|  `----.|  |     |  |                                      
|_______||__|SS   |__|                                      
                                                            
sadam alshrabi
https://t.me/termuxalsharabi
                                            ''') 
aaa=input('\033[93m\033[4mﺺﻧ ﺔﻐﻴﺻ ﻲﺴﻨﺗ ﻻ ﺔﻤﺋﺎﻗ ﻢﺳﺍ ﻞﺧﺩﺍ =============== ===========>>>>')
print('-'*29)
file=open(aaa,'w') 
aa=set([]) 
oio=set([])
#iio=set([112233,332211,000,445566,'$'*1,'$'*2,'$'*3,'@'*1,'@'*2,'@'*3,'€'*1,'€'*2,'€'*3,'&'*1,'&'*2,'&'*3,'¥'*1,'¥'*2,'¥'*3,'*'*1,'*'*2,'*'*3,'+'*1,'+'*2,'+'*3])
kk=1
while True :
    b=input('ﺔﻣﻮﻠﻌﻣ\033[24m ============================ > {} : '.format(kk))
    if b=='Pro' :
        print('\033[3;36m')
        file.close()
        qq=open(aaa, 'r' )
        ll=len(qq.readlines())
        os.system('printf "\033[3;31m"')
        print('''\033[1m ﺡﺎﺠﻨﺑ ﺩﺭﻮﺳﺎﺑ ﺀﺎﺸﻧﺍ ﻢﺗ
HACKER BY MOHAMED LKAMILI PRO ''')
        print('-'*60) 
        break ;
    aa.add(b)
    for i in aa:
        if len(i) >= 6 and i not in oio :
            oio.add(i)
            file.write(i)
            file.write('\n')
            #for o in iio:
             #   uau='{}{}'.format(i,o) 
              #  ubu='{}{}{}'.format(o,i,o)
               # ucu='{}{}{} '.format(i,o,i)
                #if len(uau)>= 6:
                   # file.write(uau)
                  #  file.write('\n')
               # if len(ubu) >= 6 and ubu != uau :
                   # file.write(ubu)
                   # file.write('\n')
                #if len(ucu) >= 6 and ucu != uau and ucu != ubu:
                  #  file.write(ucu)
                  #  file.write('\n')

        c=b+i
        d=i+b
        if len(c) >= 6 :
            file.write(c)
            file.write('\n') 
        if c != d and len(d) >= 6:
            file.write(d)
            file.write('\n')
    kk=int(kk)+1
    print('\033[95m========== \033[27m=Pro ===\033[1m ﻭﺍ ==\033[0;96m ﺔﻴﻟﺎﺗ ﺔﻣﻮﻠﻌﻤﻟ ﺕﻸﻣﺍ')
