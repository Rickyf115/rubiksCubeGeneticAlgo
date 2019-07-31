'''
Colors:
White = 0
Blue = 1
Orange = 2
Green = 3
Red = 4
Yellow = 5
'''
class Cube_2():
    def __init__(self, face1, face2, color1, color2):
        self.face1 = face1
        self.face2 = face2
        self.color1 = color1
        self.color2 = color2

class Cube_3():
    def __init__(self, face1, face2, face3, color1, color2, color3):
        self.face1 = face1
        self.face2 = face2
        self.face3 = face3
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3

class RubixCube():
    def __init__(self):
        self.cornerCubes = [
            Cube_3(0, 1, 2, 0, 1, 2),
            Cube_3(0, 2, 3, 0, 2, 3),
            Cube_3(0, 3, 4, 0, 3, 4),
            Cube_3(0, 4, 1, 0, 4, 1),
            Cube_3(5, 1, 2, 5, 1, 2),
            Cube_3(5, 2, 3, 5, 2, 3),
            Cube_3(5, 3, 4, 5, 3, 4),
            Cube_3(5, 4, 1, 5, 4, 1)
        ]

        self.innerCubes = [
            Cube_2(0, 1, 0, 1),
            Cube_2(0, 2, 0, 2),
            Cube_2(0, 3, 0, 3),
            Cube_2(0, 4, 0, 4),
            Cube_2(1, 2, 1, 2),
            Cube_2(2, 3, 2, 3),
            Cube_2(3, 4, 3, 4),
            Cube_2(4, 1, 4, 1),
            Cube_2(5, 1, 5, 1),
            Cube_2(5, 2, 5, 2),
            Cube_2(5, 3, 5, 3),
            Cube_2(5, 4, 5, 4)
        ]
        self.flag = False
        self.rightRotate(True)
        self.leftRotate(False)

    
    def getScore(self, color):
        totalScore = 1
        for cornerCube in self.cornerCubes:
            if cornerCube.face1 == color:
                if cornerCube.color1 == cornerCube.face1:
                    totalScore += 1
            elif cornerCube.face2 == color:
                if cornerCube.color2 == cornerCube.face2:
                    totalScore += 1
            elif cornerCube.face3 == color:
                if cornerCube.color3 == cornerCube.face3:
                    totalScore += 1

        for innerCube in self.innerCubes:
            if innerCube.face1 == color:
                if innerCube.color1 == innerCube.face1:
                    totalScore += 1
            elif innerCube.face2 == color:
                if innerCube.color2 == innerCube.face2:
                    totalScore += 1
        return totalScore

    def get3DCubes(self):
        for cube in self.cornerCubes:
            print("Cube: ")
            print(cube.face1, cube.face2, cube.face3)
            print(cube.color1, cube.color2, cube.color3)
            print("\n")
    
    def get2DCubes(self):
        for cube in self.innerCubes:
            print("Cube: ")
            print(cube.face1, cube.face2)
            print(cube.color1, cube.color2)
            print("\n")
    
    def do3DRotation(self, cube, color1, color2, newColor1, newColor2):
        if not self.flag:
            if cube.face1 == color1 and cube.face2 == color2:
                cube.face1 = newColor1
                cube.face2 = newColor2
                self.flag = True
            elif cube.face1 == color2 and cube.face2 == color1:
                cube.face1 = newColor2
                cube.face2 = newColor1
                self.flag = True
            elif cube.face2 == color1 and cube.face3 == color2:
                cube.face2 = newColor1
                cube.face3 = newColor2
                self.flag = True
            elif cube.face2 == color2 and cube.face3 == color1:
                cube.face2 = newColor2
                cube.face3 = newColor1
                self.flag = True
            elif cube.face1 == color1 and cube.face3 == color2:
                cube.face1 = newColor1
                cube.face3 = newColor2
                self.flag = True
            elif cube.face1 == color2 and cube.face3 == color1:
                cube.face1 = newColor2
                cube.face3 = newColor1
                self.flag = True
    
    def do2DRotation(self, cube, color, newColor):
        if not self.flag:
            if cube.face1 == color:
                cube.face1 = newColor
                self.flag = True
            elif cube.face2 == color:
                cube.face2 = newColor 
                self.flag = True

    #DONE
    def rightRotate(self, counterClockwise):
        for cornerCube in self.cornerCubes:
            if cornerCube.face1 == 2 or cornerCube.face2 == 2 or cornerCube.face3 == 2:
                if counterClockwise:
                    self.do3DRotation(cornerCube, 0, 1, 1, 5)
                    self.do3DRotation(cornerCube, 1, 5, 5, 3)
                    self.do3DRotation(cornerCube, 5, 3, 3, 0)
                    self.do3DRotation(cornerCube, 3, 0, 0, 1)

                    
                else:
                    self.do3DRotation(cornerCube, 0, 1, 3, 0)
                    self.do3DRotation(cornerCube, 1, 5, 0, 1)
                    self.do3DRotation(cornerCube, 5, 3, 1, 5)
                    self.do3DRotation(cornerCube, 3, 0, 5, 3)
            self.flag = False

        for innerCube in self.innerCubes:
            if innerCube.face1 == 2 or innerCube.face2 == 2:
                if counterClockwise:
                    self.do2DRotation(innerCube, 0, 1)
                    self.do2DRotation(innerCube, 1, 5)
                    self.do2DRotation(innerCube, 5, 3)
                    self.do2DRotation(innerCube, 3, 0)
                else:
                    self.do2DRotation(innerCube, 0, 3)
                    self.do2DRotation(innerCube, 1, 0)
                    self.do2DRotation(innerCube, 5, 1)
                    self.do2DRotation(innerCube, 3, 5)
            self.flag = False
     
    #DONE
    def leftRotate(self, counterClockwise):
        for cornerCube in self.cornerCubes:
            if cornerCube.face1 == 4 or cornerCube.face2 == 4 or cornerCube.face3 == 4:
                if counterClockwise:
                    self.do3DRotation(cornerCube, 0, 3, 3, 5)
                    self.do3DRotation(cornerCube, 3, 5, 5, 1)
                    self.do3DRotation(cornerCube, 5, 1, 1, 0)
                    self.do3DRotation(cornerCube, 1, 0, 0, 3)

                    
                else:
                    self.do3DRotation(cornerCube, 0, 3, 1, 0)
                    self.do3DRotation(cornerCube, 3, 5, 0, 3)
                    self.do3DRotation(cornerCube, 5, 1, 3, 5)
                    self.do3DRotation(cornerCube, 1, 0, 5, 1)
            self.flag = False

        for innerCube in self.innerCubes:
            if innerCube.face1 == 4 or innerCube.face2 == 4:
                if counterClockwise:
                    self.do2DRotation(innerCube, 0, 3)
                    self.do2DRotation(innerCube, 1, 0)
                    self.do2DRotation(innerCube, 5, 1)
                    self.do2DRotation(innerCube, 3, 5)
                else:
                    self.do2DRotation(innerCube, 0, 1)
                    self.do2DRotation(innerCube, 1, 5)
                    self.do2DRotation(innerCube, 5, 3)
                    self.do2DRotation(innerCube, 3, 0)
            self.flag = False

    #DONE
    def topRotate(self, counterClockwise):
        for cornerCube in self.cornerCubes:
            if cornerCube.face1 == 0 or cornerCube.face2 == 0 or cornerCube.face3 == 0:
                if counterClockwise:
                    self.do3DRotation(cornerCube, 1, 4, 2, 1)
                    self.do3DRotation(cornerCube, 1, 2, 2, 3)
                    self.do3DRotation(cornerCube, 2, 3, 3, 4)
                    self.do3DRotation(cornerCube, 3, 4, 4, 1)

                    
                else:
                    self.do3DRotation(cornerCube, 1, 2, 4, 1)
                    self.do3DRotation(cornerCube, 2, 3, 1, 2)
                    self.do3DRotation(cornerCube, 3, 4, 2, 3)
                    self.do3DRotation(cornerCube, 4, 1, 3, 4)
            self.flag = False

        for innerCube in self.innerCubes:
            if innerCube.face1 == 0 or innerCube.face2 == 0:
                if counterClockwise:
                    self.do2DRotation(innerCube, 1, 2)
                    self.do2DRotation(innerCube, 2, 3)
                    self.do2DRotation(innerCube, 3, 4)
                    self.do2DRotation(innerCube, 4, 1)
                else:
                    self.do2DRotation(innerCube, 1, 4)
                    self.do2DRotation(innerCube, 2, 1)
                    self.do2DRotation(innerCube, 3, 2)
                    self.do2DRotation(innerCube, 4, 3)
            self.flag = False

    #DONE
    def bottomRotate(self, counterClockwise):
        for cornerCube in self.cornerCubes:
            if cornerCube.face1 == 5 or cornerCube.face2 == 5 or cornerCube.face3 == 5:
                if counterClockwise:
                    self.do3DRotation(cornerCube, 1, 4, 4, 3)
                    self.do3DRotation(cornerCube, 4, 3, 3, 2)
                    self.do3DRotation(cornerCube, 3, 2, 2, 1)
                    self.do3DRotation(cornerCube, 2, 1, 1, 4)

                    
                else:
                    self.do3DRotation(cornerCube, 1, 4, 2, 1)
                    self.do3DRotation(cornerCube, 4, 3, 1, 4)
                    self.do3DRotation(cornerCube, 3, 2, 4, 3)
                    self.do3DRotation(cornerCube, 2, 1, 3, 2)
            self.flag = False

        for innerCube in self.innerCubes:
            if innerCube.face1 == 5 or innerCube.face2 == 5:
                if counterClockwise:
                    self.do2DRotation(innerCube, 1, 4)
                    self.do2DRotation(innerCube, 4, 3)
                    self.do2DRotation(innerCube, 3, 2)
                    self.do2DRotation(innerCube, 2, 1)
                else:
                    self.do2DRotation(innerCube, 1, 2)
                    self.do2DRotation(innerCube, 4, 1)
                    self.do2DRotation(innerCube, 3, 4)
                    self.do2DRotation(innerCube, 2, 3)
            self.flag = False

    #DONE
    def frontRotate(self, counterClockwise):
        for cornerCube in self.cornerCubes:
            if cornerCube.face1 == 1 or cornerCube.face2 == 1 or cornerCube.face3 == 1:
                if counterClockwise:
                    self.do3DRotation(cornerCube, 0, 4, 4, 5)
                    self.do3DRotation(cornerCube, 4, 5, 5, 2)
                    self.do3DRotation(cornerCube, 5, 2, 2, 0)
                    self.do3DRotation(cornerCube, 2, 0, 0, 4)

                    
                else:
                    self.do3DRotation(cornerCube, 0, 4, 2, 0)
                    self.do3DRotation(cornerCube, 4, 5, 0, 4)
                    self.do3DRotation(cornerCube, 5, 2, 4, 5)
                    self.do3DRotation(cornerCube, 2, 0, 5, 2)
            self.flag = False

        for innerCube in self.innerCubes:
            if innerCube.face1 == 1 or innerCube.face2 == 1:
                if counterClockwise:
                    self.do2DRotation(innerCube, 0, 4)
                    self.do2DRotation(innerCube, 4, 5)
                    self.do2DRotation(innerCube, 5, 2)
                    self.do2DRotation(innerCube, 2, 0)
                else:
                    self.do2DRotation(innerCube, 0, 2)
                    self.do2DRotation(innerCube, 4, 0)
                    self.do2DRotation(innerCube, 5, 4)
                    self.do2DRotation(innerCube, 2, 5)
            self.flag = False

    def backRotate(self, counterClockwise):
        for cornerCube in self.cornerCubes:
            if cornerCube.face1 == 3 or cornerCube.face2 == 3 or cornerCube.face3 == 3:
                if counterClockwise:
                    self.do3DRotation(cornerCube, 0, 2, 2, 5)
                    self.do3DRotation(cornerCube, 2, 5, 5, 4)
                    self.do3DRotation(cornerCube, 5, 4, 4, 0)
                    self.do3DRotation(cornerCube, 4, 0, 0, 2)

                    
                else:
                    self.do3DRotation(cornerCube, 0, 2, 4, 0)
                    self.do3DRotation(cornerCube, 2, 5, 0, 2)
                    self.do3DRotation(cornerCube, 5, 4, 2, 5)
                    self.do3DRotation(cornerCube, 4, 0, 5, 4)
            self.flag = False

        for innerCube in self.innerCubes:
            if innerCube.face1 == 3 or innerCube.face2 == 3:
                if counterClockwise:
                    self.do2DRotation(innerCube, 0, 2)
                    self.do2DRotation(innerCube, 2, 5)
                    self.do2DRotation(innerCube, 5, 4)
                    self.do2DRotation(innerCube, 4, 0)
                else:
                    self.do2DRotation(innerCube, 0, 4)
                    self.do2DRotation(innerCube, 2, 0)
                    self.do2DRotation(innerCube, 5, 2)
                    self.do2DRotation(innerCube, 4, 5)
            self.flag = False
