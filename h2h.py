from bpc import BaseballPlayer
from ps import Pitcher
from stadium import Stadium

#example batters and picthers
JamesJuanos = BaseballPlayer('r', .312, .541, .310, 56)
FrankScud = BaseballPlayer('l', .260, .412, .155, 70)
JamesReyes = Pitcher('r', 3.70, .301, .241, 71, 12)
DudThrower = Pitcher('l', 4.26, .110, .290, 80, 16)
MillerPark = Stadium(344, 400, 345, 1)


def playerImpact(batter, pitcher, ballpark):
    bhanded = batter.handed
    ba = batter.ba
    slg = batter.slg
    lsba = batter.lsba
    bso = batter.so
    phanded = pitcher.handed
    era = pitcher.era
    lhb = pitcher.lhb
    rhb = pitcher.rhb
    pso = pitcher.so
    hra = pitcher.hr
    lff = ballpark.lff
    cff = ballpark.cff
    rff = ballpark.rff
    ovf = ballpark.ovf
    stadiumImpact = 0
    batterImpact = 0

    if bhanded == phanded:
        batterImpact -= 1
    else:
        batterImpact +=1

    if slg >= .430:
        batterImpact += 1

    if ba >= .300:
        batterImpact += 1
    else:
        batterImpact -= 1

    if era <= 3.50:
        batterImpact -= 1
    else:
        batterImpact += 1

    if pso >= 80:
        batterImpact -= 1
    else:
        batterImpact += 1

    if bso >= 50:
        batterImpact -= 1
    else:
        batterImpact += 1

    if lsba >= .270:
        batterImpact += 1

    elif lsba >= .300:
        batterImpact += 2

    elif lsba >= .330:
        batterImpact += 3

    else:
        batterImpact -= 2

    if phanded == 'r' and rhb >= .270:
        batterImpact += 1
        
    elif phanded == 'l' and lhb >= .270:
        batterImpact += 1
        
    else:
        batterImpact -= 1

    if hra > 11:
        batterImpact += 1

    if lff <= 332.5:
        stadiumImpact += 1
    else:
        stadiumImpact -= 1

    if cff <= 413:
        stadiumImpact += 1
    else:
        stadiumImpact -= 1

    if rff <= 327.5:
        stadiumImpact += 1
    else:
        stadiumImpact -= 1

    stadiumImpact += ovf
    
    batterImpact += stadiumImpact

    return batterImpact


#print(playerImpact(JamesJones, JamesReyes, MillerPark))

#Shows how well a hitter might perform.
