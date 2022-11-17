import math as mt

class Projectile():
    xCoordinate=0
    yCoordinate=0
    vel:float=0
    xVel:float=0
    yVel:float=0
    ang:float=0

    def ProjectileGo(self,ang:float=0,v:float=0,x0:float=0,y0:float=0):
        self.xCoordinate=x0
        self.yCoordinate=y0
        self.vel=v
        self.ang=ang
        self.xVel=round(mt.cos(mt.radians(self.ang))*self.vel,6)
        self.yVel=round(mt.sin(mt.radians(self.ang))*self.vel,6)

    def ProjectileAng(self,x:float=0,y:float=0):

        if x==0:
            if y>=0:
                self.ang=0
            else:
                self.ang=180
        else:
            self.ang=mt.degrees(mt.atan(y/x))

    def ProjectileVel(self,x,y):
        self.vel=mt.sqrt(pow(x,2)+pow(y,2))

    def ProjectileMove(self,G:float=10,t:float=0):
        self.yVel-=(G*t)
        self.xCoordinate+=self.xVel
        self.yCoordinate+=self.yVel
        self.ProjectileAng(self,self.xVel,self.yVel)
        self.ProjectileVel(self,self.xVel,self.yVel)

if __name__ == "__main__":

    def DisplayInfo(obj:Projectile):
        print(f"Velocity:{obj.vel:*^10}")
        print(f"X velocity:{obj.xVel:*^10}")
        print(f"Y velocity:{obj.yVel:*^10}")
        print(f"Angle:{obj.ang:*^10} deg")
        print(f"Coordinate: [{obj.xCoordinate},{obj.yCoordinate}]")

    sample=Projectile

    sample.ProjectileGo(sample,90,100)
    DisplayInfo(sample)

    sample.ProjectileMove(sample,10,9)
    print("\n9s after apply gravity:")
    DisplayInfo(sample)

    ball=Projectile
    ball.ProjectileGo(ball,60,1000,0,0)
    print("\nBall:")
    print("Go:")
    DisplayInfo(ball)

    print("\nMove:")
    i:float=0
    while True:
        i+=0.001
        ball.ProjectileMove(ball,10,i)
        print(f"\nTime {i}second:")
        DisplayInfo(ball)
        if ball.yCoordinate<=0:
            break

    print("\nEnd:")
    DisplayInfo(ball)