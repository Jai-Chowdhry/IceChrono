#Parameters specific to the Vostok ice core
self.udepth_top=0.
self.age_top=-50.
self.depth=np.arange(0., 3501+0.01, 1.)
self.age_bot=800000.+self.age_top
self.corr_a=np.zeros(81)
self.corr_LID=np.zeros(81)
self.cT2=0.000084
self.thickness=3767.
self.sigmabA=0.6
self.cA1=1.
self.sigmabL=0.7
self.restart=False

