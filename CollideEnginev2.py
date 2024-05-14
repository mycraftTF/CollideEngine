import math
import copy
# 전체 픽셀 배열을 설정해놓고, 공간으로 간주
# 해당 공간이 차지되어있는지에 대한 정보를 저장
# 물체 이동시 공간에 대해 충돌 체크
# 충돌시 벡터 등 정보에 대한 정보 

class Space():
    #구성요소로 x,y 그리고 정보를 담을 3번째 리스트 필요
    #3번째 리스트에 뭘 넣지? 개체ID? if none-> ID=0
    # 생각해보니까 충돌을 차례대로 진행하면, 먼저 체크한 개체가 우선순위를 가지게 됨
    # 에비로 미래공간을 생성해서, 1번은 충돌이 업었는데, 2번이 새로 이동한 1번에 충돌할 경우, 미리 충돌판정 생성
    
    #애초에 충돌판정이 생기면 어케할거냐?
    #이후 행동에 대해선 나중에
    #이동은 벡터를 사용하여 이동
    AllEntity = []
    AllEntityid = []
    Collision = False

    def __init__(self,x,y):
        self.coord = [[0 for col in range(x)] for row in range(y)] #x,y 좌표에 모든 위치의 id를 0으로 초기화

        self.xLen = x
        self.yLen = y

    def setSpace(self):
        collide = False

        self.coord = [[0 for col in range(self.xLen)] for row in range(self.yLen)] #x,y 좌표에 모든 위치의 id를 0으로 초기화
    

        for x in self.AllEntity:
            collide = self.setEntityMask(x)
            if collide == True:
                self.Collision = True

                print("collide")
                break
        

        
    def setEntityMask(self, entity):
        if entity.id not in self.AllEntityid:
            self.AllEntity.append(entity)
            self.AllEntityid.append(entity.id)

        chk = False
        for x in range (len(entity.mask)):
            for y in range (len(entity.mask[0])):
                
                if entity.mask[x][y] == 1:
                    if self.coord[entity.locateX + x][entity.locateY + y] == 0:
                        self.coord[entity.locateX + x][entity.locateY + y] = entity.id
                    else:
                        chk = True
                        break
                
            if chk == True:
                break
        return chk
    
    
class Vector():
    def __init__(self,deg,len):    
        self.x = int(math.cos(math.radians(deg))*len)
        self.y = int(math.sin(math.radians(deg))*len)     
    def addVec(self, vec):
        self.x += vec.x
        self.y += vec.y
    def setZero(self):
        self.x=0
        self.y=0

class Entity():
    # 해당 개체가 차지하는 영역의 마스크를 모양으로 저장.
    # 어케하지?
    id = 0 #기본적인 id를 아무것도 없는  id인 0으로 초기화


    def __init__(self,id,xLength,yLength, locateX = 10, locateY = 10):
        self.id = id
        self.mask = [[id for col in range(xLength)] for row in range(yLength)] #x,y 좌표에 모든 위치의 id를 0으로 초기화
        self.locateX = locateX
        self.locateY = locateY 

    def setMask(self, mask):
        self.mask = mask
         
    def move(self, vector):
        self.locateX += vector.x
        self.locateY += vector.y

class Entity2(Entity):
    def __init__(self,id, mask,locateX = 10, locateY = 10, ):
        self.id = id
        self.mask = mask
        self.locateX = locateX
        self.locateY = locateY 


    def move(self, vector):
        self.locateX += vector.x
        self.locateY += vector.y
    
    


# adEntity는 mask가 다양하게 가능. 기본은 2차원 배열 리스트로, 공백은 0, 차지하는 공간은 1로 표시하여 마스크 생성



        


  
    

