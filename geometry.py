import numpy as np

class StewartPlatform:
    def __init__(self):
        self.base_radius=250.0
        self.platform_radius=150.0
        self.height=450.0
        base_angles_deg=np.array([10,50,130,170,250,290])
        platform_angles_deg=np.array([70,110,190,230,310,350])

        self.leg_pairing = np.array([1,0,3,2,5,4])

        self.base_angles=np.deg2rad(base_angles_deg)
        self.platform_angles=np.deg2rad(platform_angles_deg)

        self.B=self.generate_points(self.base_radius,self.base_angles)
        self.P=self.generate_points(self.platform_radius,self.platform_angles)

    
    @property
    def num_legs(self):
        return len(self.B)
    @staticmethod

    def generate_points(radius,angles):
        points=np.zeros((len(angles),3))
        for i,theta in enumerate(angles):
            x=radius*np.cos(theta)
            y=radius*np.sin(theta)
            points[i]=[x,y,0]
        return points


    def print_geometry(self):
        print("\nBase Attachment Points (mm)\n")
        print(np.round(self.B, 2))

        print("\nPlatform Attachment Points (mm)\n")
        print(np.round(self.P, 2))
        
    

    